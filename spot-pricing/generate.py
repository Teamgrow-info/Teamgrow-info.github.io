#!/usr/bin/env python3

from google.cloud import billing_v1
from google.api_core import retry
from collections import defaultdict
import re
import json
from datetime import datetime
import os
import pytz
import sys

def extract_machine_type(description):
    """Extract machine type from description."""
    # List of known machine type families
    families = ['e2', 'n2', 'n2d', 'n1', 'c2', 'c2d', 'm1', 'm2', 'm3', 'a2', 't2d', 't2a', 'g2']
    
    for family in families:
        if f"{family} " in description.lower():
            return family
    return None

def format_price(price):
    """Format price with 6 decimal places."""
    return f"${price:.6f}" if price is not None else "N/A"

def format_spot_savings(regular_price, spot_price):
    """Calculate and format spot savings percentage."""
    if regular_price is not None and spot_price is not None and regular_price > 0:
        savings = ((regular_price - spot_price) / regular_price) * 100
        if savings >= 0:
            return f"(-{savings:.1f}%)"
        else:
            return f"(+{-savings:.1f}%)"  # Show price increase with a plus
    return ""


def save_raw_data(prices):
    """Save essential pricing data to a JSON file."""
    now = datetime.now(pytz.UTC)
    filename = f'gcp_pricing_{now.strftime("%m_%Y")}.json'
    
    # Create a simplified data structure with only needed information
    simplified_data = {
        'metadata': {
            'month': now.month,
            'year': now.year,
            'capture_date': now.strftime('%Y-%m-%d'),
            'capture_timestamp': now.strftime('%Y-%m-%d %H:%M:%S %Z')
        },
        'prices': {}
    }
    
    for machine_type in prices.keys():
        simplified_data['prices'][machine_type] = {}
        for region in prices[machine_type].keys():
            simplified_data['prices'][machine_type][region] = {
                'regular': {
                    'cpu': prices[machine_type][region]['regular']['cpu'],
                    'ram': prices[machine_type][region]['regular']['ram']
                },
                'spot': {
                    'cpu': prices[machine_type][region]['spot']['cpu'],
                    'ram': prices[machine_type][region]['spot']['ram']
                }
            }
    
    with open(filename, 'w') as f:
        json.dump(simplified_data, f, indent=2)
    return filename

def get_compute_pricing():
    """Get pricing information for all machine types."""
    try:
        client = billing_v1.CloudCatalogClient()
        
        # Get the first page of the service
        service_name = "services/6F81-5844-456A"  # Compute Engine service
        request = billing_v1.ListSkusRequest(parent=service_name)
        
        prices = {}
        raw_data = []
        
        # Iterate through all pages
        sku_iter = client.list_skus(request=request)
        for sku in sku_iter:
            # Save raw data
            sku_dict = {
                'name': sku.name,
                'description': sku.description,
                'service_regions': list(sku.service_regions),
                'pricing_info': [{
                    'tiered_rates': [{
                        'unit_price': {
                            'units': rate.unit_price.units,
                            'nanos': rate.unit_price.nanos
                        }
                    } for rate in info.pricing_expression.tiered_rates]
                } for info in sku.pricing_info]
            }
            raw_data.append(sku_dict)
            
            description = sku.description.lower()
            
            # Skip irrelevant SKUs
            if not any(word in description for word in ['core', 'ram']):
                continue
                
            # Skip special SKUs
            if any(term in description for term in ['sole tenancy', 'commitment', 'premium']):
                continue
                
            # Extract machine type for compute resources
            machine_type = extract_machine_type(description)
            if not machine_type:
                continue
            
            # Get region from service regions
            region = sku.service_regions[0] if sku.service_regions else None
            if not region:
                continue
            
            # Initialize machine type prices if not exists
            if machine_type not in prices:
                prices[machine_type] = {}
            
            # Initialize region prices if not exists
            if region not in prices[machine_type]:
                prices[machine_type][region] = {
                    'regular': {'cpu': None, 'ram': None},
                    'spot': {'cpu': None, 'ram': None}
                }
            
            # Get the unit price
            pricing_info = sku.pricing_info[0]
            base_unit_price = pricing_info.pricing_expression.tiered_rates[0].unit_price
            unit_price = (base_unit_price.nanos / 1e9) + base_unit_price.units
            
            # Determine price category for compute resources
            price_category = None
            if 'spot' in description or 'preemptible' in description:
                price_category = 'spot'
            elif 'custom' not in description:  # Prefer non-custom instance pricing for regular
                price_category = 'regular'
            
            # Skip if no valid price category
            if not price_category:
                continue
            
            # Store CPU or RAM price, but only if it's higher than the existing price
            if 'core' in description:
                current_price = prices[machine_type][region][price_category]['cpu']
                if current_price is None or unit_price > current_price:
                    prices[machine_type][region][price_category]['cpu'] = unit_price
            elif 'ram' in description:
                current_price = prices[machine_type][region][price_category]['ram']
                if current_price is None or unit_price > current_price:
                    prices[machine_type][region][price_category]['ram'] = unit_price
        
        return prices, raw_data
    except Exception as e:
        print(f"Error fetching pricing data: {e}")
        return None, None

def print_pricing_info(prices):
    """Print pricing information in a formatted table."""
    # Print header
    print("\nType    Region                   Core On-Demand      Core Spot           RAM On-Demand       RAM Spot")
    print("-" * 120)
    
    # Print data rows
    current_type = None
    for machine_type in sorted(prices.keys()):
        for region in sorted(prices[machine_type].keys()):
            pricing = prices[machine_type][region]
            
            # Get core prices
            core_standard = pricing['regular']['cpu']
            core_spot = pricing['spot']['cpu']
            
            # Calculate core savings
            core_savings = None
            if core_standard is not None and core_spot is not None and core_standard > 0:
                core_savings = ((core_standard - core_spot) / core_standard) * 100
            
            # Get RAM prices
            ram_standard = pricing['regular']['ram']
            ram_spot = pricing['spot']['ram']
            
            # Calculate RAM savings
            ram_savings = None
            if ram_standard is not None and ram_spot is not None and ram_standard > 0:
                ram_savings = ((ram_standard - ram_spot) / ram_standard) * 100
            
            # Format values
            core_standard_str = f"${core_standard:.6f}" if core_standard is not None else "N/A"
            core_spot_str = f"${core_spot:.6f}" if core_spot is not None else "N/A"
            ram_standard_str = f"${ram_standard:.6f}" if ram_standard is not None else "N/A"
            ram_spot_str = f"${ram_spot:.6f}" if ram_spot is not None else "N/A"
            
            # Format savings with parentheses
            core_savings_str = f"(-{core_savings:.1f}%)" if core_savings is not None else ""
            ram_savings_str = f"(-{ram_savings:.1f}%)" if ram_savings is not None else ""
            
            # Print row with fixed width columns
            print(f"{machine_type:<6} {region:<25} "
                  f"{core_standard_str:<16} {core_spot_str:<8} {core_savings_str:<8} "
                  f"{ram_standard_str:<16} {ram_spot_str:<8} {ram_savings_str:<8}")

def main():
    """Main function to get and process pricing data."""
    try:
        prices, raw_data = get_compute_pricing()
        
        # Save only processed pricing data
        filename = save_raw_data(prices)
        print(f"# Data saved to {filename}", file=sys.stderr)
        
        # Print pricing information
        print_pricing_info(prices)
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
