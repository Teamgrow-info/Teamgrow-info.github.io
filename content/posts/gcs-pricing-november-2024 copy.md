---
title: "GCP Spot Pricing Report - November 2024"
date: 2024-11-27
draft: false
tags: ["gcp", "spot-pricing", "cloud-costs"]
---

<style>
    .pricing-table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
        font-size: 14px;
    }
    .pricing-table th, .pricing-table td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }
    .pricing-table th {
        background-color: #f2f2f2;
        cursor: pointer;
    }
    .pricing-table th:hover {
        background-color: #ddd;
    }
    .savings-positive {
        color: green;
    }
    .savings-negative {
        color: red;
    }
    .trend-up {
        color: green;
        font-weight: bold;
    }
    .trend-down {
        color: red;
        font-weight: bold;
    }
    .trend-same {
        color: gray;
    }
    .filter-group {
        margin-bottom: 20px;
    }
    .filter-group label {
        margin-right: 10px;
        font-weight: bold;
    }
    .sort-indicator {
        opacity: 0.7;
        font-size: 1.2em;
        margin-left: 5px;
        font-weight: bold;
    }
    th:hover .sort-indicator {
        opacity: 1;
    }
    .active-sort .sort-indicator {
        opacity: 1;
    }
</style>

This report shows the current GCP spot pricing as of 2024-11-27.

<div class="filter-group">
    <label for="machineType">Machine Type:</label>
    <select id="machineType" onchange="filterTable()">
        <option value="">All</option>
        <option value="a2">a2</option><option value="c2d">c2d</option><option value="e2">e2</option><option value="g2">g2</option><option value="m3">m3</option><option value="n1">n1</option><option value="n2">n2</option><option value="n2d">n2d</option><option value="t2a">t2a</option><option value="t2d">t2d</option>
    </select>
</div>

<table id="pricingTable" class="pricing-table">
    <thead>
        <tr>
            <th onclick="sortTable(0)">Machine Type</th>
            <th>Region</th>
            <th onclick="sortTable(2)">CPU On-Demand <span class="sort-indicator">↕</span></th>
            <th onclick="sortTable(3)">CPU Spot <span class="sort-indicator">↕</span></th>
            <th onclick="sortTable(4)">CPU Savings <span class="sort-indicator">↕</span></th>
            <th onclick="sortTable(5)">Trend</th>
            <th onclick="sortTable(6)">RAM On-Demand <span class="sort-indicator">↕</span></th>
            <th onclick="sortTable(7)">RAM Spot <span class="sort-indicator">↕</span></th>
            <th onclick="sortTable(8)">RAM Savings <span class="sort-indicator">↕</span></th>
            <th onclick="sortTable(9)">Trend</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>a2</td>
            <td>africa-south1</td>
            <td data-value="0.04134719">$0.041347</td>
            <td data-value="0.01240416">$0.012404</td>
            <td class="savings-positive" data-value="69.99999274436787">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005541996">$0.005542</td>
            <td data-value="0.001662599">$0.001663</td>
            <td class="savings-positive" data-value="69.99999639119191">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>asia-east1</td>
            <td data-value="0.036602">$0.036602</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="74.09076006775587">-74.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004906">$0.004906</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="74.0909090909091">-74.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>asia-east2</td>
            <td data-value="0.044231">$0.044231</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="78.55960751509123">-78.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005928">$0.005928</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="78.5576923076923">-78.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>asia-northeast1</td>
            <td data-value="0.040618">$0.040618</td>
            <td data-value="0.01625">$0.016250</td>
            <td class="savings-positive" data-value="59.99310650450539">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005419">$0.005419</td>
            <td data-value="0.002168">$0.002168</td>
            <td class="savings-positive" data-value="59.99261856431076">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>asia-northeast2</td>
            <td data-value="0.040618">$0.040618</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="76.65246934856468">-76.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005419">$0.005419</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="76.54364273851264">-76.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>asia-northeast3</td>
            <td data-value="0.040618">$0.040618</td>
            <td data-value="0.015">$0.015000</td>
            <td class="savings-positive" data-value="63.07055985031267">-63.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005419">$0.005419</td>
            <td data-value="0.002002">$0.002002</td>
            <td class="savings-positive" data-value="63.05591437534601">-63.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>asia-south1</td>
            <td data-value="0.03797">$0.037970</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="75.02422965499078">-75.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005088">$0.005088</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="75.01768867924528">-75.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>asia-south2</td>
            <td data-value="0.03797">$0.037970</td>
            <td data-value="0.01137996">$0.011380</td>
            <td class="savings-positive" data-value="70.02907558598893">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005088">$0.005088</td>
            <td data-value="0.00152532">$0.001525</td>
            <td class="savings-positive" data-value="70.02122641509433">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>asia-southeast1</td>
            <td data-value="0.038999">$0.038999</td>
            <td data-value="0.01372">$0.013720</td>
            <td class="savings-positive" data-value="64.81961075925024">-64.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005226">$0.005226</td>
            <td data-value="0.00184">$0.001840</td>
            <td class="savings-positive" data-value="64.79142747799463">-64.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>asia-southeast2</td>
            <td data-value="0.0425089">$0.042509</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="77.69102470306218">-77.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0056963">$0.005696</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="77.68551515896284">-77.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>australia-southeast1</td>
            <td data-value="0.044856">$0.044856</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="78.85834670947031">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006011">$0.006011</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="78.85376809183164">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>australia-southeast2</td>
            <td data-value="0.044856">$0.044856</td>
            <td data-value="0.013466286">$0.013466</td>
            <td class="savings-positive" data-value="69.97885232744783">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006011">$0.006011</td>
            <td data-value="0.001804962">$0.001805</td>
            <td class="savings-positive" data-value="69.97235069040093">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-central2</td>
            <td data-value="0.04073">$0.040730</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="76.71667075865456">-76.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005458">$0.005458</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="76.71124954195676">-76.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-north1</td>
            <td data-value="0.034806">$0.034806</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="72.75383554559558">-72.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004664">$0.004664</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="72.74656946826758">-72.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-north2</td>
            <td data-value="0.03319155">$0.033192</td>
            <td data-value="0.013272">$0.013272</td>
            <td class="savings-positive" data-value="60.01391920533992">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00444885">$0.004449</td>
            <td data-value="0.00177975">$0.001780</td>
            <td class="savings-positive" data-value="59.99527967901817">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-southwest1</td>
            <td data-value="0.03730098">$0.037301</td>
            <td data-value="0.01119029">$0.011190</td>
            <td class="savings-positive" data-value="70.00001072357884">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00499966">$0.005000</td>
            <td data-value="0.001499898">$0.001500</td>
            <td class="savings-positive" data-value="70.0">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-west1</td>
            <td data-value="0.034773">$0.034773</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="72.72797860408939">-72.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004661">$0.004661</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="72.72902810555675">-72.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-west10</td>
            <td data-value="0.04868094">$0.048681</td>
            <td data-value="0.01460428">$0.014604</td>
            <td class="savings-positive" data-value="70.00000410838409">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00652498">$0.006525</td>
            <td data-value="0.001957494">$0.001957</td>
            <td class="savings-positive" data-value="69.99999999999999">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-west12</td>
            <td data-value="0.04077819">$0.040778</td>
            <td data-value="0.01223346">$0.012233</td>
            <td class="savings-positive" data-value="69.99999264312613">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00546573">$0.005466</td>
            <td data-value="0.001639719">$0.001640</td>
            <td class="savings-positive" data-value="70.0">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-west2</td>
            <td data-value="0.04073">$0.040730</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="76.71667075865456">-76.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005458">$0.005458</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="76.71124954195676">-76.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-west3</td>
            <td data-value="0.04073">$0.040730</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="76.71667075865456">-76.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005458">$0.005458</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="76.71124954195676">-76.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-west4</td>
            <td data-value="0.034802">$0.034802</td>
            <td data-value="0.01392">$0.013920</td>
            <td class="savings-positive" data-value="60.00229871846445">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004664">$0.004664</td>
            <td data-value="0.001866">$0.001866</td>
            <td class="savings-positive" data-value="59.99142367066895">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-west6</td>
            <td data-value="0.044231">$0.044231</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="78.55960751509123">-78.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005928">$0.005928</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="78.5576923076923">-78.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-west8</td>
            <td data-value="0.03666876">$0.036669</td>
            <td data-value="0.01100063">$0.011001</td>
            <td class="savings-positive" data-value="69.99999454576593">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00491492">$0.004915</td>
            <td data-value="0.001474476">$0.001474</td>
            <td class="savings-positive" data-value="70.0">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>europe-west9</td>
            <td data-value="0.03666876">$0.036669</td>
            <td data-value="0.01100063">$0.011001</td>
            <td class="savings-positive" data-value="69.99999454576593">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00491492">$0.004915</td>
            <td data-value="0.001474476">$0.001474</td>
            <td class="savings-positive" data-value="70.0">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>me-central1</td>
            <td data-value="0.03840737">$0.038407</td>
            <td data-value="0.01152221">$0.011522</td>
            <td class="savings-positive" data-value="70.00000260366696">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005147955">$0.005148</td>
            <td data-value="0.001544387">$0.001544</td>
            <td class="savings-positive" data-value="69.9999902874054">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>me-central2</td>
            <td data-value="0.0505776">$0.050578</td>
            <td data-value="0.01517328">$0.015173</td>
            <td class="savings-positive" data-value="70.0">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0067792">$0.006779</td>
            <td data-value="0.00203376">$0.002034</td>
            <td class="savings-positive" data-value="70.0">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>me-west1</td>
            <td data-value="0.0347721">$0.034772</td>
            <td data-value="0.01391">$0.013910</td>
            <td class="savings-positive" data-value="59.99666399210862">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0046607">$0.004661</td>
            <td data-value="0.001864">$0.001864</td>
            <td class="savings-positive" data-value="60.0060076812496">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>northamerica-northeast1</td>
            <td data-value="0.034802">$0.034802</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="72.75070398252974">-72.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004664">$0.004664</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="72.74656946826758">-72.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>northamerica-northeast2</td>
            <td data-value="0.034802">$0.034802</td>
            <td data-value="0.01043163">$0.010432</td>
            <td class="savings-positive" data-value="70.0257743807827">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004664">$0.004664</td>
            <td data-value="0.00139821">$0.001398</td>
            <td class="savings-positive" data-value="70.02122641509433">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>southamerica-east1</td>
            <td data-value="0.05018">$0.050180</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="81.10143483459545">-81.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006725">$0.006725</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="81.09888475836432">-81.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>southamerica-west1</td>
            <td data-value="0.04520373">$0.045204</td>
            <td data-value="0.013561119">$0.013561</td>
            <td class="savings-positive" data-value="70.0">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00605891">$0.006059</td>
            <td data-value="0.001817673">$0.001818</td>
            <td class="savings-positive" data-value="70.0">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>us-central1</td>
            <td data-value="0.031611">$0.031611</td>
            <td data-value="0.01264">$0.012640</td>
            <td class="savings-positive" data-value="60.01391920533992">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004237">$0.004237</td>
            <td data-value="0.001695">$0.001695</td>
            <td class="savings-positive" data-value="59.995279679018175">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>us-east4</td>
            <td data-value="0.035605">$0.035605</td>
            <td data-value="0.01424">$0.014240</td>
            <td class="savings-positive" data-value="60.00561718859711">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004771">$0.004771</td>
            <td data-value="0.001908">$0.001908</td>
            <td class="savings-positive" data-value="60.00838398658562">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>us-east5</td>
            <td data-value="0.031611">$0.031611</td>
            <td data-value="0.00894">$0.008940</td>
            <td class="savings-positive" data-value="71.71870551390339">-71.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004237">$0.004237</td>
            <td data-value="0.001198">$0.001198</td>
            <td class="savings-positive" data-value="71.72527731885768">-71.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>us-south1</td>
            <td data-value="0.03730098">$0.037301</td>
            <td data-value="0.01119029">$0.011190</td>
            <td class="savings-positive" data-value="70.00001072357884">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00499966">$0.005000</td>
            <td data-value="0.001499898">$0.001500</td>
            <td class="savings-positive" data-value="70.0">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>us-west2</td>
            <td data-value="0.03797">$0.037970</td>
            <td data-value="0.0094833">$0.009483</td>
            <td class="savings-positive" data-value="75.02422965499078">-75.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005089">$0.005089</td>
            <td data-value="0.0012711">$0.001271</td>
            <td class="savings-positive" data-value="75.02259775987424">-75.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>us-west3</td>
            <td data-value="0.03797">$0.037970</td>
            <td data-value="0.01519">$0.015190</td>
            <td class="savings-positive" data-value="59.99473268369765">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005089">$0.005089</td>
            <td data-value="0.002035">$0.002035</td>
            <td class="savings-positive" data-value="60.011790135586565">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>us-west4</td>
            <td data-value="0.035605">$0.035605</td>
            <td data-value="0.01424">$0.014240</td>
            <td class="savings-positive" data-value="60.00561718859711">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004771">$0.004771</td>
            <td data-value="0.001908">$0.001908</td>
            <td class="savings-positive" data-value="60.00838398658562">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>a2</td>
            <td>us-west8</td>
            <td data-value="0.031611">$0.031611</td>
            <td data-value="0.01252">$0.012520</td>
            <td class="savings-positive" data-value="60.393533896428465">-60.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004237">$0.004237</td>
            <td data-value="0.001678">$0.001678</td>
            <td class="savings-positive" data-value="60.39650696247345">-60.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>africa-south1</td>
            <td data-value="0.0386684">$0.038668</td>
            <td data-value="0.008197236">$0.008197</td>
            <td class="savings-positive" data-value="78.80120201508208">-78.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005178372">$0.005178</td>
            <td data-value="0.001097412">$0.001097</td>
            <td class="savings-positive" data-value="78.80777974235919">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>asia-east1</td>
            <td data-value="0.034231">$0.034231</td>
            <td data-value="0.01211">$0.012110</td>
            <td class="savings-positive" data-value="64.62271040869388">-64.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004584">$0.004584</td>
            <td data-value="0.00162">$0.001620</td>
            <td class="savings-positive" data-value="64.65968586387434">-64.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>asia-east2</td>
            <td data-value="0.041355">$0.041355</td>
            <td data-value="0.010008">$0.010008</td>
            <td class="savings-positive" data-value="75.79978237214362">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005538">$0.005538</td>
            <td data-value="0.00134">$0.001340</td>
            <td class="savings-positive" data-value="75.80353918382087">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>asia-northeast1</td>
            <td data-value="0.037964">$0.037964</td>
            <td data-value="0.009187">$0.009187</td>
            <td class="savings-positive" data-value="75.80075861342324">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005084">$0.005084</td>
            <td data-value="0.00123">$0.001230</td>
            <td class="savings-positive" data-value="75.80645161290323">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>asia-northeast2</td>
            <td data-value="0.037964">$0.037964</td>
            <td data-value="0.009187">$0.009187</td>
            <td class="savings-positive" data-value="75.80075861342324">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005084">$0.005084</td>
            <td data-value="0.00123">$0.001230</td>
            <td class="savings-positive" data-value="75.80645161290323">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>asia-northeast3</td>
            <td data-value="0.037964">$0.037964</td>
            <td data-value="0.009187">$0.009187</td>
            <td class="savings-positive" data-value="75.80075861342324">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005084">$0.005084</td>
            <td data-value="0.00123">$0.001230</td>
            <td class="savings-positive" data-value="75.80645161290323">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>asia-south1</td>
            <td data-value="0.019512">$0.019512</td>
            <td data-value="0.00307">$0.003070</td>
            <td class="savings-positive" data-value="84.26609266092662">-84.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.002613">$0.002613</td>
            <td data-value="0.00041">$0.000410</td>
            <td class="savings-positive" data-value="84.30922311519328">-84.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>asia-south2</td>
            <td data-value="0.035508">$0.035508</td>
            <td data-value="0.0073">$0.007300</td>
            <td class="savings-positive" data-value="79.44125267545341">-79.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004755">$0.004755</td>
            <td data-value="0.000978">$0.000978</td>
            <td class="savings-positive" data-value="79.43217665615143">-79.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>asia-southeast1</td>
            <td data-value="0.036471">$0.036471</td>
            <td data-value="0.00668">$0.006680</td>
            <td class="savings-positive" data-value="81.68407776041239">-81.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004884">$0.004884</td>
            <td data-value="0.000898">$0.000898</td>
            <td class="savings-positive" data-value="81.61343161343162">-81.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>asia-southeast2</td>
            <td data-value="0.039753">$0.039753</td>
            <td data-value="0.00962">$0.009620</td>
            <td class="savings-positive" data-value="75.80056851055265">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005323">$0.005323</td>
            <td data-value="0.001288">$0.001288</td>
            <td class="savings-positive" data-value="75.80311854217547">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>australia-southeast1</td>
            <td data-value="0.041964">$0.041964</td>
            <td data-value="0.010155">$0.010155</td>
            <td class="savings-positive" data-value="75.80068630254505">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005619">$0.005619</td>
            <td data-value="0.00136">$0.001360</td>
            <td class="savings-positive" data-value="75.79640505428011">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>australia-southeast2</td>
            <td data-value="0.041964">$0.041964</td>
            <td data-value="0.010155">$0.010155</td>
            <td class="savings-positive" data-value="75.80068630254505">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005619">$0.005619</td>
            <td data-value="0.00136">$0.001360</td>
            <td class="savings-positive" data-value="75.79640505428011">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-central2</td>
            <td data-value="0.038088">$0.038088</td>
            <td data-value="0.009217">$0.009217</td>
            <td class="savings-positive" data-value="75.80077714765805">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0051">$0.005100</td>
            <td data-value="0.001234">$0.001234</td>
            <td class="savings-positive" data-value="75.80392156862746">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-north1</td>
            <td data-value="0.032551">$0.032551</td>
            <td data-value="0.007877">$0.007877</td>
            <td class="savings-positive" data-value="75.80105065896592">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004359">$0.004359</td>
            <td data-value="0.001055">$0.001055</td>
            <td class="savings-positive" data-value="75.79720119293415">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-north2</td>
            <td data-value="0.03104115">$0.031041</td>
            <td data-value="0.007728">$0.007728</td>
            <td class="savings-positive" data-value="75.10401515407774">-75.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00415695">$0.004157</td>
            <td data-value="0.00103635">$0.001036</td>
            <td class="savings-positive" data-value="75.06946198534983">-75.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-southwest1</td>
            <td data-value="0.03488434">$0.034884</td>
            <td data-value="0.00844172">$0.008442</td>
            <td class="savings-positive" data-value="75.80083212123262">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00467162">$0.004672</td>
            <td data-value="0.00113044">$0.001130</td>
            <td class="savings-positive" data-value="75.80197019449356">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-west1</td>
            <td data-value="0.032551">$0.032551</td>
            <td data-value="0.00511">$0.005110</td>
            <td class="savings-positive" data-value="84.30155755583546">-84.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004359">$0.004359</td>
            <td data-value="0.000684">$0.000684</td>
            <td class="savings-positive" data-value="84.30832759807295">-84.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-west10</td>
            <td data-value="0.04552702">$0.045527</td>
            <td data-value="0.00965118">$0.009651</td>
            <td class="savings-positive" data-value="78.80120420796266">-78.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00609686">$0.006097</td>
            <td data-value="0.00129206">$0.001292</td>
            <td class="savings-positive" data-value="78.80777974235917">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-west12</td>
            <td data-value="0.03813627">$0.038136</td>
            <td data-value="0.00808443">$0.008084</td>
            <td class="savings-positive" data-value="78.80120420796266">-78.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00510711">$0.005107</td>
            <td data-value="0.00108231">$0.001082</td>
            <td class="savings-positive" data-value="78.80777974235919">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-west2</td>
            <td data-value="0.038088">$0.038088</td>
            <td data-value="0.0086">$0.008600</td>
            <td class="savings-positive" data-value="77.42070993488763">-77.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0051">$0.005100</td>
            <td data-value="0.001149">$0.001149</td>
            <td class="savings-positive" data-value="77.47058823529413">-77.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-west3</td>
            <td data-value="0.038088">$0.038088</td>
            <td data-value="0.00924">$0.009240</td>
            <td class="savings-positive" data-value="75.74039067422811">-75.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0051">$0.005100</td>
            <td data-value="0.001238">$0.001238</td>
            <td class="savings-positive" data-value="75.72549019607844">-75.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-west4</td>
            <td data-value="0.032551">$0.032551</td>
            <td data-value="0.00888">$0.008880</td>
            <td class="savings-positive" data-value="72.71973211268471">-72.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004359">$0.004359</td>
            <td data-value="0.001193">$0.001193</td>
            <td class="savings-positive" data-value="72.63133746272081">-72.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-west6</td>
            <td data-value="0.041355">$0.041355</td>
            <td data-value="0.010008">$0.010008</td>
            <td class="savings-positive" data-value="75.79978237214362">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005538">$0.005538</td>
            <td data-value="0.00134">$0.001340</td>
            <td class="savings-positive" data-value="75.80353918382087">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-west8</td>
            <td data-value="0.03429308">$0.034293</td>
            <td data-value="0.00829864">$0.008299</td>
            <td class="savings-positive" data-value="75.80083212123262">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00459244">$0.004592</td>
            <td data-value="0.00111128">$0.001111</td>
            <td class="savings-positive" data-value="75.80197019449355">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>europe-west9</td>
            <td data-value="0.03429308">$0.034293</td>
            <td data-value="0.00829864">$0.008299</td>
            <td class="savings-positive" data-value="75.80083212123262">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00459244">$0.004592</td>
            <td data-value="0.00111128">$0.001111</td>
            <td class="savings-positive" data-value="75.80197019449355">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>me-central1</td>
            <td data-value="0.03591905">$0.035919</td>
            <td data-value="0.007614405">$0.007614</td>
            <td class="savings-positive" data-value="78.8012071588753">-78.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004810185">$0.004810</td>
            <td data-value="0.001019385">$0.001019</td>
            <td class="savings-positive" data-value="78.80777974235917">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>me-central2</td>
            <td data-value="0.0473008">$0.047301</td>
            <td data-value="0.0100272">$0.010027</td>
            <td class="savings-positive" data-value="78.80120420796266">-78.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0063344">$0.006334</td>
            <td data-value="0.0013424">$0.001342</td>
            <td class="savings-positive" data-value="78.80777974235919">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>me-west1</td>
            <td data-value="0.0325193">$0.032519</td>
            <td data-value="0.0078694">$0.007869</td>
            <td class="savings-positive" data-value="75.80083212123263">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0043549">$0.004355</td>
            <td data-value="0.0010538">$0.001054</td>
            <td class="savings-positive" data-value="75.80197019449356">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>northamerica-northeast1</td>
            <td data-value="0.032551">$0.032551</td>
            <td data-value="0.007877">$0.007877</td>
            <td class="savings-positive" data-value="75.80105065896592">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004359">$0.004359</td>
            <td data-value="0.001055">$0.001055</td>
            <td class="savings-positive" data-value="75.79720119293415">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>northamerica-northeast2</td>
            <td data-value="0.032551">$0.032551</td>
            <td data-value="0.0067">$0.006700</td>
            <td class="savings-positive" data-value="79.41691499493102">-79.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004359">$0.004359</td>
            <td data-value="0.000897">$0.000897</td>
            <td class="savings-positive" data-value="79.42188575361321">-79.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>southamerica-east1</td>
            <td data-value="0.046942">$0.046942</td>
            <td data-value="0.00966">$0.009660</td>
            <td class="savings-positive" data-value="79.42141365940948">-79.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006286">$0.006286</td>
            <td data-value="0.001293">$0.001293</td>
            <td class="savings-positive" data-value="79.43048043270761">-79.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>southamerica-west1</td>
            <td data-value="0.04227509">$0.042275</td>
            <td data-value="0.01023022">$0.010230</td>
            <td class="savings-positive" data-value="75.80083212123263">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00566137">$0.005661</td>
            <td data-value="0.00136994">$0.001370</td>
            <td class="savings-positive" data-value="75.80197019449356">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>us-central1</td>
            <td data-value="0.029563">$0.029563</td>
            <td data-value="0.00736">$0.007360</td>
            <td class="savings-positive" data-value="75.10401515407774">-75.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003959">$0.003959</td>
            <td data-value="0.000987">$0.000987</td>
            <td class="savings-positive" data-value="75.06946198534983">-75.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>us-east4</td>
            <td data-value="0.033296">$0.033296</td>
            <td data-value="0.01186">$0.011860</td>
            <td class="savings-positive" data-value="64.38010571840461">-64.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004458">$0.004458</td>
            <td data-value="0.001589">$0.001589</td>
            <td class="savings-positive" data-value="64.35621354867654">-64.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>us-east5</td>
            <td data-value="0.029563">$0.029563</td>
            <td data-value="0.007154">$0.007154</td>
            <td class="savings-positive" data-value="75.80083212123262">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003959">$0.003959</td>
            <td data-value="0.000958">$0.000958</td>
            <td class="savings-positive" data-value="75.80197019449355">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>us-south1</td>
            <td data-value="0.03488434">$0.034884</td>
            <td data-value="0.00844172">$0.008442</td>
            <td class="savings-positive" data-value="75.80083212123262">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00467162">$0.004672</td>
            <td data-value="0.00113044">$0.001130</td>
            <td class="savings-positive" data-value="75.80197019449356">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>us-west2</td>
            <td data-value="0.035537">$0.035537</td>
            <td data-value="0.0086">$0.008600</td>
            <td class="savings-positive" data-value="75.79987055744716">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004759">$0.004759</td>
            <td data-value="0.001152">$0.001152</td>
            <td class="savings-positive" data-value="75.79323387266233">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>us-west3</td>
            <td data-value="0.035537">$0.035537</td>
            <td data-value="0.0086">$0.008600</td>
            <td class="savings-positive" data-value="75.79987055744716">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004759">$0.004759</td>
            <td data-value="0.001152">$0.001152</td>
            <td class="savings-positive" data-value="75.79323387266233">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>us-west4</td>
            <td data-value="0.033296">$0.033296</td>
            <td data-value="0.00846">$0.008460</td>
            <td class="savings-positive" data-value="74.59154252763093">-74.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004458">$0.004458</td>
            <td data-value="0.001133">$0.001133</td>
            <td class="savings-positive" data-value="74.58501570210856">-74.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>c2d</td>
            <td>us-west8</td>
            <td data-value="0.029563">$0.029563</td>
            <td data-value="0.00793">$0.007930</td>
            <td class="savings-positive" data-value="73.17592937117342">-73.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003959">$0.003959</td>
            <td data-value="0.001062">$0.001062</td>
            <td class="savings-positive" data-value="73.17504420308158">-73.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>africa-south1</td>
            <td data-value="0.02852956">$0.028530</td>
            <td data-value="0.00913">$0.009130</td>
            <td class="savings-positive" data-value="67.99810442222032">-68.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003823977">$0.003824</td>
            <td data-value="0.001225">$0.001225</td>
            <td class="savings-positive" data-value="67.96528849415151">-68.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>asia-east1</td>
            <td data-value="0.02525538">$0.025255</td>
            <td data-value="0.010605">$0.010605</td>
            <td class="savings-positive" data-value="58.00894700455903">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00338514">$0.003385</td>
            <td data-value="0.0014217">$0.001422</td>
            <td class="savings-positive" data-value="58.00173700349174">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>asia-east2</td>
            <td data-value="0.03051939">$0.030519</td>
            <td data-value="0.0061">$0.006100</td>
            <td class="savings-positive" data-value="80.01270667598533">-80.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00409032">$0.004090</td>
            <td data-value="0.000815">$0.000815</td>
            <td class="savings-positive" data-value="80.07490856461109">-80.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>asia-northeast1</td>
            <td data-value="0.02802642">$0.028026</td>
            <td data-value="0.01121">$0.011210</td>
            <td class="savings-positive" data-value="60.00202665913091">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00373911">$0.003739</td>
            <td data-value="0.001496">$0.001496</td>
            <td class="savings-positive" data-value="59.99047901773417">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>asia-northeast2</td>
            <td data-value="0.02802642">$0.028026</td>
            <td data-value="0.01121">$0.011210</td>
            <td class="savings-positive" data-value="60.00202665913091">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00373911">$0.003739</td>
            <td data-value="0.001496">$0.001496</td>
            <td class="savings-positive" data-value="59.99047901773417">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>asia-northeast3</td>
            <td data-value="0.02802642">$0.028026</td>
            <td data-value="0.01121">$0.011210</td>
            <td class="savings-positive" data-value="60.00202665913091">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00373911">$0.003739</td>
            <td data-value="0.001496">$0.001496</td>
            <td class="savings-positive" data-value="59.99047901773417">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>asia-south1</td>
            <td data-value="0.0261993">$0.026199</td>
            <td data-value="0.01048">$0.010480</td>
            <td class="savings-positive" data-value="59.99893126915604">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00351072">$0.003511</td>
            <td data-value="0.001403">$0.001403</td>
            <td class="savings-positive" data-value="60.03668763102726">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>asia-south2</td>
            <td data-value="0.0261993">$0.026199</td>
            <td data-value="0.011004">$0.011004</td>
            <td class="savings-positive" data-value="57.99887783261385">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00351072">$0.003511</td>
            <td data-value="0.00147525">$0.001475</td>
            <td class="savings-positive" data-value="57.97870522286027">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>asia-southeast1</td>
            <td data-value="0.02690931">$0.026909</td>
            <td data-value="0.011298">$0.011298</td>
            <td class="savings-positive" data-value="58.01453103033857">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00360594">$0.003606</td>
            <td data-value="0.0015141">$0.001514</td>
            <td class="savings-positive" data-value="58.01094860147423">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>asia-southeast2</td>
            <td data-value="0.029331147">$0.029331</td>
            <td data-value="0.0123165">$0.012316</td>
            <td class="savings-positive" data-value="58.00880204241587">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003930474">$0.003930</td>
            <td data-value="0.0016506">$0.001651</td>
            <td class="savings-positive" data-value="58.00506503795726">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>australia-southeast1</td>
            <td data-value="0.03095064">$0.030951</td>
            <td data-value="0.01126">$0.011260</td>
            <td class="savings-positive" data-value="63.61949219789963">-63.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00414759">$0.004148</td>
            <td data-value="0.001509">$0.001509</td>
            <td class="savings-positive" data-value="63.6174260233051">-63.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>australia-southeast2</td>
            <td data-value="0.026308">$0.026308</td>
            <td data-value="0.01028">$0.010280</td>
            <td class="savings-positive" data-value="60.92443363235518">-60.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003525">$0.003525</td>
            <td data-value="0.001379">$0.001379</td>
            <td class="savings-positive" data-value="60.87943262411347">-60.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-central2</td>
            <td data-value="0.0281037">$0.028104</td>
            <td data-value="0.00499">$0.004990</td>
            <td class="savings-positive" data-value="82.24433081765035">-82.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00376602">$0.003766</td>
            <td data-value="0.000666">$0.000666</td>
            <td class="savings-positive" data-value="82.31554797903358">-82.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-north1</td>
            <td data-value="0.02401614">$0.024016</td>
            <td data-value="0.0100905">$0.010091</td>
            <td class="savings-positive" data-value="57.98450542010497">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00321816">$0.003218</td>
            <td data-value="0.0013524">$0.001352</td>
            <td class="savings-positive" data-value="57.97598627787307">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-north2</td>
            <td data-value="0.02290217">$0.022902</td>
            <td data-value="0.007214184">$0.007214</td>
            <td class="savings-positive" data-value="68.4999980351207">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003069707">$0.003070</td>
            <td data-value="0.000966957">$0.000967</td>
            <td class="savings-positive" data-value="68.50002296636129">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-southwest1</td>
            <td data-value="0.025738">$0.025738</td>
            <td data-value="0.01081">$0.010810</td>
            <td class="savings-positive" data-value="57.999844587769054">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00345">$0.003450</td>
            <td data-value="0.001449">$0.001449</td>
            <td class="savings-positive" data-value="58.00000000000001">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-west1</td>
            <td data-value="0.02399337">$0.023993</td>
            <td data-value="0.00909">$0.009090</td>
            <td class="savings-positive" data-value="62.114534140056186">-62.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00321609">$0.003216</td>
            <td data-value="0.001217">$0.001217</td>
            <td class="savings-positive" data-value="62.15901918167713">-62.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-west10</td>
            <td data-value="0.03358985">$0.033590</td>
            <td data-value="0.01138">$0.011380</td>
            <td class="savings-positive" data-value="66.12071801451927">-66.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004502236">$0.004502</td>
            <td data-value="0.001525">$0.001525</td>
            <td class="savings-positive" data-value="66.12794176049411">-66.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-west12</td>
            <td data-value="0.02813695">$0.028137</td>
            <td data-value="0.00794">$0.007940</td>
            <td class="savings-positive" data-value="71.78087887990702">-71.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003771354">$0.003771</td>
            <td data-value="0.001063">$0.001063</td>
            <td class="savings-positive" data-value="71.81383662207261">-71.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-west2</td>
            <td data-value="0.0281037">$0.028104</td>
            <td data-value="0.01069">$0.010690</td>
            <td class="savings-positive" data-value="61.96230389592829">-62.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00376602">$0.003766</td>
            <td data-value="0.001432">$0.001432</td>
            <td class="savings-positive" data-value="61.975772831795894">-62.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-west3</td>
            <td data-value="0.0281037">$0.028104</td>
            <td data-value="0.01115">$0.011150</td>
            <td class="savings-positive" data-value="60.32550874084195">-60.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00376602">$0.003766</td>
            <td data-value="0.001493">$0.001493</td>
            <td class="savings-positive" data-value="60.35602572477045">-60.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-west4</td>
            <td data-value="0.02401338">$0.024013</td>
            <td data-value="0.010038">$0.010038</td>
            <td class="savings-positive" data-value="58.198304445271766">-58.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00321816">$0.003218</td>
            <td data-value="0.0013419">$0.001342</td>
            <td class="savings-positive" data-value="58.30225967633679">-58.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-west6</td>
            <td data-value="0.03051939">$0.030519</td>
            <td data-value="0.01282">$0.012820</td>
            <td class="savings-positive" data-value="57.993917964939676">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00409032">$0.004090</td>
            <td data-value="0.001718">$0.001718</td>
            <td class="savings-positive" data-value="57.99839621349919">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-west8</td>
            <td data-value="0.025302">$0.025302</td>
            <td data-value="0.00949">$0.009490</td>
            <td class="savings-positive" data-value="62.49308355070745">-62.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003391">$0.003391</td>
            <td data-value="0.00127">$0.001270</td>
            <td class="savings-positive" data-value="62.54792096726628">-62.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>europe-west9</td>
            <td data-value="0.025302">$0.025302</td>
            <td data-value="0.01012">$0.010120</td>
            <td class="savings-positive" data-value="60.00316180539088">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003391">$0.003391</td>
            <td data-value="0.001351">$0.001351</td>
            <td class="savings-positive" data-value="60.15924506045415">-60.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>me-central1</td>
            <td data-value="0.02650108">$0.026501</td>
            <td data-value="0.00991">$0.009910</td>
            <td class="savings-positive" data-value="62.60529759541876">-62.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003552089">$0.003552</td>
            <td data-value="0.001328">$0.001328</td>
            <td class="savings-positive" data-value="62.613549378971086">-62.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>me-central2</td>
            <td data-value="0.03489854">$0.034899</td>
            <td data-value="0.01396">$0.013960</td>
            <td class="savings-positive" data-value="59.99832657755883">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004677648">$0.004678</td>
            <td data-value="0.001871">$0.001871</td>
            <td class="savings-positive" data-value="60.00126559330672">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>me-west1</td>
            <td data-value="0.02399275">$0.023993</td>
            <td data-value="0.0092">$0.009200</td>
            <td class="savings-positive" data-value="61.655083306415484">-61.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003215883">$0.003216</td>
            <td data-value="0.001237">$0.001237</td>
            <td class="savings-positive" data-value="61.53467026008097">-61.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>northamerica-northeast1</td>
            <td data-value="0.02401338">$0.024013</td>
            <td data-value="0.00919">$0.009190</td>
            <td class="savings-positive" data-value="61.72966904284195">-61.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00321816">$0.003218</td>
            <td data-value="0.001233">$0.001233</td>
            <td class="savings-positive" data-value="61.686180923260494">-61.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>northamerica-northeast2</td>
            <td data-value="0.02401338">$0.024013</td>
            <td data-value="0.0096">$0.009600</td>
            <td class="savings-positive" data-value="60.02228757467712">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00321816">$0.003218</td>
            <td data-value="0.001286">$0.001286</td>
            <td class="savings-positive" data-value="60.039277102443634">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>northamerica-south1</td>
            <td data-value="0.02377463">$0.023775</td>
            <td data-value="0.009047">$0.009047</td>
            <td class="savings-positive" data-value="61.94683155952375">-61.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003186648">$0.003187</td>
            <td data-value="0.00121208">$0.001212</td>
            <td class="savings-positive" data-value="61.96379393017365">-62.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>southamerica-east1</td>
            <td data-value="0.0346242">$0.034624</td>
            <td data-value="0.00692">$0.006920</td>
            <td class="savings-positive" data-value="80.01397866232288">-80.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00464025">$0.004640</td>
            <td data-value="0.000927">$0.000927</td>
            <td class="savings-positive" data-value="80.0226280911589">-80.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>southamerica-west1</td>
            <td data-value="0.031190573">$0.031191</td>
            <td data-value="0.00739">$0.007390</td>
            <td class="savings-positive" data-value="76.30694376791347">-76.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004180647">$0.004181</td>
            <td data-value="0.000996">$0.000996</td>
            <td class="savings-positive" data-value="76.17593640410205">-76.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>us-central1</td>
            <td data-value="0.02181159">$0.021812</td>
            <td data-value="0.00916">$0.009160</td>
            <td class="savings-positive" data-value="58.00397861870684">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00292353">$0.002924</td>
            <td data-value="0.001228">$0.001228</td>
            <td class="savings-positive" data-value="57.995984306643">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>us-east4</td>
            <td data-value="0.02456745">$0.024567</td>
            <td data-value="0.01028">$0.010280</td>
            <td class="savings-positive" data-value="58.1560153780714">-58.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00329199">$0.003292</td>
            <td data-value="0.001378">$0.001378</td>
            <td class="savings-positive" data-value="58.14082059787544">-58.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>us-east5</td>
            <td data-value="0.02181159">$0.021812</td>
            <td data-value="0.00531">$0.005310</td>
            <td class="savings-positive" data-value="75.65514481062591">-75.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00292353">$0.002924</td>
            <td data-value="0.000712">$0.000712</td>
            <td class="savings-positive" data-value="75.64588015173437">-75.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>us-south1</td>
            <td data-value="0.02573768">$0.025738</td>
            <td data-value="0.00873">$0.008730</td>
            <td class="savings-positive" data-value="66.08085888083151">-66.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003449765">$0.003450</td>
            <td data-value="0.001173">$0.001173</td>
            <td class="savings-positive" data-value="65.99768390020769">-66.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>us-west2</td>
            <td data-value="0.0261993">$0.026199</td>
            <td data-value="0.011004">$0.011004</td>
            <td class="savings-positive" data-value="57.99887783261385">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00351141">$0.003511</td>
            <td data-value="0.00147525">$0.001475</td>
            <td class="savings-positive" data-value="57.98696250224269">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>us-west3</td>
            <td data-value="0.0261993">$0.026199</td>
            <td data-value="0.011004">$0.011004</td>
            <td class="savings-positive" data-value="57.99887783261385">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00351141">$0.003511</td>
            <td data-value="0.0014742">$0.001474</td>
            <td class="savings-positive" data-value="58.01686502003469">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>us-west4</td>
            <td data-value="0.02456745">$0.024567</td>
            <td data-value="0.00309">$0.003090</td>
            <td class="savings-positive" data-value="87.42238205430355">-87.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00329199">$0.003292</td>
            <td data-value="0.000415">$0.000415</td>
            <td class="savings-positive" data-value="87.39364335857643">-87.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>e2</td>
            <td>us-west8</td>
            <td data-value="0.02181159">$0.021812</td>
            <td data-value="0.006543477">$0.006543</td>
            <td class="savings-positive" data-value="70.0">-70.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00292353">$0.002924</td>
            <td data-value="0.000877059">$0.000877</td>
            <td class="savings-positive" data-value="70.0">-70.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>africa-south1</td>
            <td data-value="0.03268458">$0.032685</td>
            <td data-value="0.01029564">$0.010296</td>
            <td class="savings-positive" data-value="68.50000826077618">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003829103">$0.003829</td>
            <td data-value="0.001206167">$0.001206</td>
            <td class="savings-positive" data-value="68.50001162152076">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>asia-east1</td>
            <td data-value="0.02893385">$0.028934</td>
            <td data-value="0.00636">$0.006360</td>
            <td class="savings-positive" data-value="78.01882570069313">-78.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003389693">$0.003390</td>
            <td data-value="0.000746">$0.000746</td>
            <td class="savings-positive" data-value="77.99210724983058">-78.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>asia-east2</td>
            <td data-value="0.03495601">$0.034956</td>
            <td data-value="0.01101114">$0.011011</td>
            <td class="savings-positive" data-value="68.50000901132594">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004095208">$0.004095</td>
            <td data-value="0.00128999">$0.001290</td>
            <td class="savings-positive" data-value="68.50001269776773">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>asia-northeast1</td>
            <td data-value="0.03208986">$0.032090</td>
            <td data-value="0.01010831">$0.010108</td>
            <td class="savings-positive" data-value="68.49998722337834">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003759429">$0.003759</td>
            <td data-value="0.00118422">$0.001184</td>
            <td class="savings-positive" data-value="68.50000359097088">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>asia-northeast2</td>
            <td data-value="0.03208986">$0.032090</td>
            <td data-value="0.01010831">$0.010108</td>
            <td class="savings-positive" data-value="68.49998722337834">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003759429">$0.003759</td>
            <td data-value="0.00118422">$0.001184</td>
            <td class="savings-positive" data-value="68.50000359097088">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>asia-northeast3</td>
            <td data-value="0.03208986">$0.032090</td>
            <td data-value="0.0059">$0.005900</td>
            <td class="savings-positive" data-value="81.61412982169446">-81.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003759429">$0.003759</td>
            <td data-value="0.000691">$0.000691</td>
            <td class="savings-positive" data-value="81.61954913897829">-81.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>asia-south1</td>
            <td data-value="0.026011561">$0.026012</td>
            <td data-value="0.01092">$0.010920</td>
            <td class="savings-positive" data-value="58.01866716111348">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003047337">$0.003047</td>
            <td data-value="0.00128">$0.001280</td>
            <td class="savings-positive" data-value="57.99611267148988">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>asia-south2</td>
            <td data-value="0.03001334">$0.030013</td>
            <td data-value="0.009454203">$0.009454</td>
            <td class="savings-positive" data-value="68.4999970013334">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003516159">$0.003516</td>
            <td data-value="0.00110759">$0.001108</td>
            <td class="savings-positive" data-value="68.50000241741058">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>asia-southeast1</td>
            <td data-value="0.03082796">$0.030828</td>
            <td data-value="0.01295">$0.012950</td>
            <td class="savings-positive" data-value="57.992679372880986">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003611593">$0.003612</td>
            <td data-value="0.001517">$0.001517</td>
            <td class="savings-positive" data-value="57.99637445304607">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>asia-southeast2</td>
            <td data-value="0.03360165">$0.033602</td>
            <td data-value="0.01058452">$0.010585</td>
            <td class="savings-positive" data-value="68.49999925598893">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00393654">$0.003937</td>
            <td data-value="0.00124001">$0.001240</td>
            <td class="savings-positive" data-value="68.50000254030189">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>australia-southeast1</td>
            <td data-value="0.031224269">$0.031224</td>
            <td data-value="0.01117329">$0.011173</td>
            <td class="savings-positive" data-value="64.21600774705085">-64.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003658022">$0.003658</td>
            <td data-value="0.001308987">$0.001309</td>
            <td class="savings-positive" data-value="64.21598885955306">-64.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>australia-southeast2</td>
            <td data-value="0.03247324">$0.032473</td>
            <td data-value="0.01117329">$0.011173</td>
            <td class="savings-positive" data-value="65.59231539569195">-65.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003804342">$0.003804</td>
            <td data-value="0.001308987">$0.001309</td>
            <td class="savings-positive" data-value="65.59228902133405">-65.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-central2</td>
            <td data-value="0.03219481">$0.032195</td>
            <td data-value="0.01014137">$0.010141</td>
            <td class="savings-positive" data-value="68.49998493546009">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003771725">$0.003772</td>
            <td data-value="0.001188093">$0.001188</td>
            <td class="savings-positive" data-value="68.50000994240035">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-north1</td>
            <td data-value="0.02751452">$0.027515</td>
            <td data-value="0.008667074">$0.008667</td>
            <td class="savings-positive" data-value="68.49999927311107">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003223414">$0.003223</td>
            <td data-value="0.001015375">$0.001015</td>
            <td class="savings-positive" data-value="68.5000127194335">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-north2</td>
            <td data-value="0.02623762">$0.026238</td>
            <td data-value="0.009975">$0.009975</td>
            <td class="savings-positive" data-value="61.98207002007041">-62.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003073821">$0.003074</td>
            <td data-value="0.0011676">$0.001168</td>
            <td class="savings-positive" data-value="62.01470417438101">-62.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-southwest1</td>
            <td data-value="0.02948609">$0.029486</td>
            <td data-value="0.009288119">$0.009288</td>
            <td class="savings-positive" data-value="68.49999779557074">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003454389">$0.003454</td>
            <td data-value="0.001088133">$0.001088</td>
            <td class="savings-positive" data-value="68.49998653886404">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-west1</td>
            <td data-value="0.02751452">$0.027515</td>
            <td data-value="0.00989">$0.009890</td>
            <td class="savings-positive" data-value="64.05534241556822">-64.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003223414">$0.003223</td>
            <td data-value="0.001158">$0.001158</td>
            <td class="savings-positive" data-value="64.07535612862635">-64.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-west10</td>
            <td data-value="0.03848185">$0.038482</td>
            <td data-value="0.01212178">$0.012122</td>
            <td class="savings-positive" data-value="68.50000714622608">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004508271">$0.004508</td>
            <td data-value="0.001420105">$0.001420</td>
            <td class="savings-positive" data-value="68.50000809623023">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-west12</td>
            <td data-value="0.03223479">$0.032235</td>
            <td data-value="0.01015396">$0.010154</td>
            <td class="savings-positive" data-value="68.49999643242596">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003776409">$0.003776</td>
            <td data-value="0.001189569">$0.001190</td>
            <td class="savings-positive" data-value="68.49999563076986">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-west2</td>
            <td data-value="0.028451227">$0.028451</td>
            <td data-value="0.01014137">$0.010141</td>
            <td class="savings-positive" data-value="64.35524555759933">-64.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003333152">$0.003333</td>
            <td data-value="0.001188093">$0.001188</td>
            <td class="savings-positive" data-value="64.3552709267384">-64.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-west3</td>
            <td data-value="0.029449516">$0.029450</td>
            <td data-value="0.01028">$0.010280</td>
            <td class="savings-positive" data-value="65.09280492080073">-65.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003450105">$0.003450</td>
            <td data-value="0.001204">$0.001204</td>
            <td class="savings-positive" data-value="65.10251137284227">-65.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-west4</td>
            <td data-value="0.02626386">$0.026264</td>
            <td data-value="0.01103">$0.011030</td>
            <td class="savings-positive" data-value="58.00312673003892">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003076895">$0.003077</td>
            <td data-value="0.001292">$0.001292</td>
            <td class="savings-positive" data-value="58.00961683775364">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-west6</td>
            <td data-value="0.03495601">$0.034956</td>
            <td data-value="0.01267">$0.012670</td>
            <td class="savings-positive" data-value="63.754444514691464">-63.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004095208">$0.004095</td>
            <td data-value="0.001484">$0.001484</td>
            <td class="savings-positive" data-value="63.762524394365315">-63.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-west8</td>
            <td data-value="0.02898633">$0.028986</td>
            <td data-value="0.009130693">$0.009131</td>
            <td class="savings-positive" data-value="68.50000327740698">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00339584">$0.003396</td>
            <td data-value="0.00106969">$0.001070</td>
            <td class="savings-positive" data-value="68.49998822088203">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>europe-west9</td>
            <td data-value="0.02898633">$0.028986</td>
            <td data-value="0.009130693">$0.009131</td>
            <td class="savings-positive" data-value="68.50000327740698">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00339584">$0.003396</td>
            <td data-value="0.00106969">$0.001070</td>
            <td class="savings-positive" data-value="68.49998822088203">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>me-central1</td>
            <td data-value="0.03036068">$0.030361</td>
            <td data-value="0.009563614">$0.009564</td>
            <td class="savings-positive" data-value="68.50000065874679">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00355685">$0.003557</td>
            <td data-value="0.001120408">$0.001120</td>
            <td class="savings-positive" data-value="68.49999297130887">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>me-central2</td>
            <td data-value="0.03998114">$0.039981</td>
            <td data-value="0.01196">$0.011960</td>
            <td class="savings-positive" data-value="70.08589549972812">-70.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004683918">$0.004684</td>
            <td data-value="0.001402">$0.001402</td>
            <td class="savings-positive" data-value="70.06779367187896">-70.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>me-west1</td>
            <td data-value="0.02748703">$0.027487</td>
            <td data-value="0.008658416">$0.008658</td>
            <td class="savings-positive" data-value="68.4999943609768">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003220193">$0.003220</td>
            <td data-value="0.001014361">$0.001014</td>
            <td class="savings-positive" data-value="68.49999363392195">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>northamerica-northeast1</td>
            <td data-value="0.02751452">$0.027515</td>
            <td data-value="0.008667074">$0.008667</td>
            <td class="savings-positive" data-value="68.49999927311107">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003223414">$0.003223</td>
            <td data-value="0.001015375">$0.001015</td>
            <td class="savings-positive" data-value="68.5000127194335">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>northamerica-northeast2</td>
            <td data-value="0.02751452">$0.027515</td>
            <td data-value="0.008667074">$0.008667</td>
            <td class="savings-positive" data-value="68.49999927311107">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003223414">$0.003223</td>
            <td data-value="0.000993">$0.000993</td>
            <td class="savings-positive" data-value="69.19415253516924">-69.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>southamerica-east1</td>
            <td data-value="0.03967878">$0.039679</td>
            <td data-value="0.01249882">$0.012499</td>
            <td class="savings-positive" data-value="68.49998916297325">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004648496">$0.004648</td>
            <td data-value="0.001464276">$0.001464</td>
            <td class="savings-positive" data-value="68.50000516296024">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>southamerica-west1</td>
            <td data-value="0.03573314">$0.035733</td>
            <td data-value="0.01125594">$0.011256</td>
            <td class="savings-positive" data-value="68.49999748132966">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004186251">$0.004186</td>
            <td data-value="0.001318669">$0.001319</td>
            <td class="savings-positive" data-value="68.50000155270195">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>us-central1</td>
            <td data-value="0.024988212">$0.024988</td>
            <td data-value="0.00884">$0.008840</td>
            <td class="savings-positive" data-value="64.62331918746327">-64.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.002927448">$0.002927</td>
            <td data-value="0.001034">$0.001034</td>
            <td class="savings-positive" data-value="64.67913349784521">-64.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>us-east4</td>
            <td data-value="0.024906389">$0.024906</td>
            <td data-value="0.01046">$0.010460</td>
            <td class="savings-positive" data-value="58.0027437939719">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.002917862">$0.002918</td>
            <td data-value="0.001225">$0.001225</td>
            <td class="savings-positive" data-value="58.01720574859264">-58.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>us-east5</td>
            <td data-value="0.02814422">$0.028144</td>
            <td data-value="0.008865431">$0.008865</td>
            <td class="savings-positive" data-value="68.49999395968337">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003297185">$0.003297</td>
            <td data-value="0.001038613">$0.001039</td>
            <td class="savings-positive" data-value="68.50000834044798">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>us-south1</td>
            <td data-value="0.02948609">$0.029486</td>
            <td data-value="0.009288119">$0.009288</td>
            <td class="savings-positive" data-value="68.49999779557074">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003454389">$0.003454</td>
            <td data-value="0.001088133">$0.001088</td>
            <td class="savings-positive" data-value="68.49998653886404">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>us-west2</td>
            <td data-value="0.03003833">$0.030038</td>
            <td data-value="0.009462074">$0.009462</td>
            <td class="savings-positive" data-value="68.49999983354601">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003519086">$0.003519</td>
            <td data-value="0.001108512">$0.001109</td>
            <td class="savings-positive" data-value="68.50000255748225">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>us-west3</td>
            <td data-value="0.03003833">$0.030038</td>
            <td data-value="0.009462074">$0.009462</td>
            <td class="savings-positive" data-value="68.49999983354601">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003519086">$0.003519</td>
            <td data-value="0.001108512">$0.001109</td>
            <td class="savings-positive" data-value="68.50000255748225">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>us-west4</td>
            <td data-value="0.02814422">$0.028144</td>
            <td data-value="0.008865431">$0.008865</td>
            <td class="savings-positive" data-value="68.49999395968337">-68.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003297185">$0.003297</td>
            <td data-value="0.001038613">$0.001039</td>
            <td class="savings-positive" data-value="68.50000834044798">-68.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>g2</td>
            <td>us-west8</td>
            <td data-value="0.02498821">$0.024988</td>
            <td data-value="0.01">$0.010000</td>
            <td class="savings-positive" data-value="59.981127099540146">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.002927449">$0.002927</td>
            <td data-value="0.001171">$0.001171</td>
            <td class="savings-positive" data-value="59.999303147552695">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>africa-south1</td>
            <td data-value="0.0455184">$0.045518</td>
            <td data-value="0.00958764">$0.009588</td>
            <td class="savings-positive" data-value="78.93678160919539">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0066708">$0.006671</td>
            <td data-value="0.00141264">$0.001413</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>asia-east1</td>
            <td data-value="0.04029492">$0.040295</td>
            <td data-value="0.00721">$0.007210</td>
            <td class="savings-positive" data-value="82.10692563727636">-82.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00590529">$0.005905</td>
            <td data-value="0.001063">$0.001063</td>
            <td class="savings-positive" data-value="81.99919055626397">-82.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>asia-east2</td>
            <td data-value="0.04868172">$0.048682</td>
            <td data-value="0.01025394">$0.010254</td>
            <td class="savings-positive" data-value="78.93677544671797">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00713439">$0.007134</td>
            <td data-value="0.001510812">$0.001511</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>asia-northeast1</td>
            <td data-value="0.04469016">$0.044690</td>
            <td data-value="0.008">$0.008000</td>
            <td class="savings-positive" data-value="82.09896764746422">-82.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00654942">$0.006549</td>
            <td data-value="0.001386936">$0.001387</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>asia-northeast2</td>
            <td data-value="0.04469016">$0.044690</td>
            <td data-value="0.009413186">$0.009413</td>
            <td class="savings-positive" data-value="78.9367816091954">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00654942">$0.006549</td>
            <td data-value="0.001386936">$0.001387</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>asia-northeast3</td>
            <td data-value="0.04469016">$0.044690</td>
            <td data-value="0.009413186">$0.009413</td>
            <td class="savings-positive" data-value="78.9367816091954">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00654942">$0.006549</td>
            <td data-value="0.001386936">$0.001387</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>asia-south1</td>
            <td data-value="0.036225176">$0.036225</td>
            <td data-value="0.00768">$0.007680</td>
            <td class="savings-positive" data-value="78.79927484686341">-78.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005308862">$0.005309</td>
            <td data-value="0.001133">$0.001133</td>
            <td class="savings-positive" data-value="78.65832639838821">-78.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>asia-south2</td>
            <td data-value="0.04179828">$0.041798</td>
            <td data-value="0.00748">$0.007480</td>
            <td class="savings-positive" data-value="82.1045267891406">-82.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00612561">$0.006126</td>
            <td data-value="0.001103">$0.001103</td>
            <td class="savings-positive" data-value="81.9936300221529">-82.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>asia-southeast1</td>
            <td data-value="0.04293276">$0.042933</td>
            <td data-value="0.00589">$0.005890</td>
            <td class="savings-positive" data-value="86.28087269488381">-86.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00629187">$0.006292</td>
            <td data-value="0.000867">$0.000867</td>
            <td class="savings-positive" data-value="86.2203128799546">-86.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>asia-southeast2</td>
            <td data-value="0.04679556">$0.046796</td>
            <td data-value="0.009856651">$0.009857</td>
            <td class="savings-positive" data-value="78.9367816091954">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00685797">$0.006858</td>
            <td data-value="0.001452276">$0.001452</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>australia-southeast1</td>
            <td data-value="0.043484683">$0.043485</td>
            <td data-value="0.01040493">$0.010405</td>
            <td class="savings-positive" data-value="76.07219535209674">-76.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006372755">$0.006373</td>
            <td data-value="0.001303">$0.001303</td>
            <td class="savings-positive" data-value="79.55358396800129">-79.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>australia-southeast2</td>
            <td data-value="0.04522407">$0.045224</td>
            <td data-value="0.01040493">$0.010405</td>
            <td class="savings-positive" data-value="76.99249536806396">-77.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006627665">$0.006628</td>
            <td data-value="0.00153306">$0.001533</td>
            <td class="savings-positive" data-value="76.86877656007056">-76.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-central2</td>
            <td data-value="0.04483632">$0.044836</td>
            <td data-value="0.009443972">$0.009444</td>
            <td class="savings-positive" data-value="78.93678160919539">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00657084">$0.006571</td>
            <td data-value="0.001391472">$0.001391</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-north1</td>
            <td data-value="0.03831828">$0.038318</td>
            <td data-value="0.00686">$0.006860</td>
            <td class="savings-positive" data-value="82.09731752051502">-82.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00561561">$0.005616</td>
            <td data-value="0.001011">$0.001011</td>
            <td class="savings-positive" data-value="81.9966130126558">-82.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-north2</td>
            <td data-value="0.03654">$0.036540</td>
            <td data-value="0.012852">$0.012852</td>
            <td class="savings-positive" data-value="64.82758620689654">-64.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005355">$0.005355</td>
            <td data-value="0.00188475">$0.001885</td>
            <td class="savings-positive" data-value="64.80392156862746">-64.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-southwest1</td>
            <td data-value="0.041064">$0.041064</td>
            <td data-value="0.00735">$0.007350</td>
            <td class="savings-positive" data-value="82.10111046171829">-82.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006018">$0.006018</td>
            <td data-value="0.001083">$0.001083</td>
            <td class="savings-positive" data-value="82.00398803589233">-82.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-west1</td>
            <td data-value="0.03831828">$0.038318</td>
            <td data-value="0.00619">$0.006190</td>
            <td class="savings-positive" data-value="83.84583024081456">-83.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00561561">$0.005616</td>
            <td data-value="0.00113">$0.001130</td>
            <td class="savings-positive" data-value="79.87751998447186">-79.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-west10</td>
            <td data-value="0.053592">$0.053592</td>
            <td data-value="0.0112882">$0.011288</td>
            <td class="savings-positive" data-value="78.9367816091954">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.007854">$0.007854</td>
            <td data-value="0.0016632">$0.001663</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-west12</td>
            <td data-value="0.044892">$0.044892</td>
            <td data-value="0.0094557">$0.009456</td>
            <td class="savings-positive" data-value="78.9367816091954">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006579">$0.006579</td>
            <td data-value="0.0013932">$0.001393</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-west2</td>
            <td data-value="0.039622794">$0.039623</td>
            <td data-value="0.009443972">$0.009444</td>
            <td class="savings-positive" data-value="76.16530525333474">-76.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005806788">$0.005807</td>
            <td data-value="0.001183">$0.001183</td>
            <td class="savings-positive" data-value="79.62729137003107">-79.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-west3</td>
            <td data-value="0.041013067">$0.041013</td>
            <td data-value="0.009443972">$0.009444</td>
            <td class="savings-positive" data-value="76.97326074150952">-77.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006010535">$0.006011</td>
            <td data-value="0.001391472">$0.001391</td>
            <td class="savings-positive" data-value="76.8494485099912">-76.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-west4</td>
            <td data-value="0.03657654">$0.036577</td>
            <td data-value="0.00545">$0.005450</td>
            <td class="savings-positive" data-value="85.09973879432007">-85.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005360355">$0.005360</td>
            <td data-value="0.000803">$0.000803</td>
            <td class="savings-positive" data-value="85.01964888519511">-85.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-west6</td>
            <td data-value="0.04868172">$0.048682</td>
            <td data-value="0.01025394">$0.010254</td>
            <td class="savings-positive" data-value="78.93677544671797">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00713439">$0.007134</td>
            <td data-value="0.001510812">$0.001511</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-west8</td>
            <td data-value="0.040368">$0.040368</td>
            <td data-value="0.00723">$0.007230</td>
            <td class="savings-positive" data-value="82.089774078478">-82.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005916">$0.005916</td>
            <td data-value="0.001065">$0.001065</td>
            <td class="savings-positive" data-value="81.99797160243408">-82.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>europe-west9</td>
            <td data-value="0.040368">$0.040368</td>
            <td data-value="0.0085028">$0.008503</td>
            <td class="savings-positive" data-value="78.9367816091954">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005916">$0.005916</td>
            <td data-value="0.0012528">$0.001253</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>me-central1</td>
            <td data-value="0.042282">$0.042282</td>
            <td data-value="0.00757">$0.007570</td>
            <td class="savings-positive" data-value="82.09640035949104">-82.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0061965">$0.006196</td>
            <td data-value="0.001115">$0.001115</td>
            <td class="savings-positive" data-value="82.00597111272492">-82.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>me-central2</td>
            <td data-value="0.05568">$0.055680</td>
            <td data-value="0.011728">$0.011728</td>
            <td class="savings-positive" data-value="78.93678160919539">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00816">$0.008160</td>
            <td data-value="0.001728">$0.001728</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>me-west1</td>
            <td data-value="0.03828">$0.038280</td>
            <td data-value="0.008063">$0.008063</td>
            <td class="savings-positive" data-value="78.9367816091954">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00561">$0.005610</td>
            <td data-value="0.001188">$0.001188</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>northamerica-northeast1</td>
            <td data-value="0.03831828">$0.038318</td>
            <td data-value="0.00686">$0.006860</td>
            <td class="savings-positive" data-value="82.09731752051502">-82.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00561561">$0.005616</td>
            <td data-value="0.001189188">$0.001189</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>northamerica-northeast2</td>
            <td data-value="0.03831828">$0.038318</td>
            <td data-value="0.00686">$0.006860</td>
            <td class="savings-positive" data-value="82.09731752051502">-82.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00561561">$0.005616</td>
            <td data-value="0.001189188">$0.001189</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>southamerica-east1</td>
            <td data-value="0.05525892">$0.055259</td>
            <td data-value="0.00989">$0.009890</td>
            <td class="savings-positive" data-value="82.1024370364097">-82.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00809829">$0.008098</td>
            <td data-value="0.001458">$0.001458</td>
            <td class="savings-positive" data-value="81.99619919760838">-82.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>southamerica-west1</td>
            <td data-value="0.049764">$0.049764</td>
            <td data-value="0.0104819">$0.010482</td>
            <td class="savings-positive" data-value="78.93678160919539">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.007293">$0.007293</td>
            <td data-value="0.0015444">$0.001544</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>us-central1</td>
            <td data-value="0.0348">$0.034800</td>
            <td data-value="0.01256">$0.012560</td>
            <td class="savings-positive" data-value="63.90804597701148">-63.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0051">$0.005100</td>
            <td data-value="0.001843">$0.001843</td>
            <td class="savings-positive" data-value="63.86274509803922">-63.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>us-east4</td>
            <td data-value="0.034686053">$0.034686</td>
            <td data-value="0.00807">$0.008070</td>
            <td class="savings-positive" data-value="76.73416459347507">-76.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0050833">$0.005083</td>
            <td data-value="0.001189">$0.001189</td>
            <td class="savings-positive" data-value="76.60968268644385">-76.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>us-east5</td>
            <td data-value="0.03919524">$0.039195</td>
            <td data-value="0.008255779">$0.008256</td>
            <td class="savings-positive" data-value="78.9367816091954">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00574413">$0.005744</td>
            <td data-value="0.001216404">$0.001216</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>us-south1</td>
            <td data-value="0.041064">$0.041064</td>
            <td data-value="0.0086494">$0.008649</td>
            <td class="savings-positive" data-value="78.9367816091954">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006018">$0.006018</td>
            <td data-value="0.0012744">$0.001274</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>us-west2</td>
            <td data-value="0.04183308">$0.041833</td>
            <td data-value="0.008811393">$0.008811</td>
            <td class="savings-positive" data-value="78.9367816091954">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00613071">$0.006131</td>
            <td data-value="0.001298268">$0.001298</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>us-west3</td>
            <td data-value="0.04183308">$0.041833</td>
            <td data-value="0.008811393">$0.008811</td>
            <td class="savings-positive" data-value="78.9367816091954">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00613071">$0.006131</td>
            <td data-value="0.001298268">$0.001298</td>
            <td class="savings-positive" data-value="78.82352941176471">-78.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>us-west4</td>
            <td data-value="0.03919524">$0.039195</td>
            <td data-value="0.00869">$0.008690</td>
            <td class="savings-positive" data-value="77.82894045297337">-77.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00574413">$0.005744</td>
            <td data-value="0.001282">$0.001282</td>
            <td class="savings-positive" data-value="77.68156361363687">-77.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>m3</td>
            <td>us-west8</td>
            <td data-value="0.0348">$0.034800</td>
            <td data-value="0.01392">$0.013920</td>
            <td class="savings-positive" data-value="59.999999999999986">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0051">$0.005100</td>
            <td data-value="0.00204">$0.002040</td>
            <td class="savings-positive" data-value="60.0">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>africa-south1</td>
            <td data-value="0.04134719">$0.041347</td>
            <td data-value="0.00870474">$0.008705</td>
            <td class="savings-positive" data-value="78.94720294172348">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005541996">$0.005542</td>
            <td data-value="0.001166736">$0.001167</td>
            <td class="savings-positive" data-value="78.94736842105263">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>asia-east1</td>
            <td data-value="0.036602">$0.036602</td>
            <td data-value="0.00703">$0.007030</td>
            <td class="savings-positive" data-value="80.79339926779957">-80.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004906">$0.004906</td>
            <td data-value="0.000941">$0.000941</td>
            <td class="savings-positive" data-value="80.8194048104362">-80.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>asia-east2</td>
            <td data-value="0.044231">$0.044231</td>
            <td data-value="0.00717">$0.007170</td>
            <td class="savings-positive" data-value="83.7896497931315">-83.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005928">$0.005928</td>
            <td data-value="0.000967">$0.000967</td>
            <td class="savings-positive" data-value="83.68758434547908">-83.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>asia-northeast1</td>
            <td data-value="0.040618">$0.040618</td>
            <td data-value="0.00917">$0.009170</td>
            <td class="savings-positive" data-value="77.42380225515781">-77.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005419">$0.005419</td>
            <td data-value="0.001224">$0.001224</td>
            <td class="savings-positive" data-value="77.41280679092083">-77.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>asia-northeast2</td>
            <td data-value="0.040618">$0.040618</td>
            <td data-value="0.01107">$0.011070</td>
            <td class="savings-positive" data-value="72.74607316953076">-72.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005419">$0.005419</td>
            <td data-value="0.001477">$0.001477</td>
            <td class="savings-positive" data-value="72.74404871747555">-72.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>asia-northeast3</td>
            <td data-value="0.040618">$0.040618</td>
            <td data-value="0.00709">$0.007090</td>
            <td class="savings-positive" data-value="82.54468462258112">-82.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005419">$0.005419</td>
            <td data-value="0.000947">$0.000947</td>
            <td class="savings-positive" data-value="82.5244510057206">-82.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>asia-south1</td>
            <td data-value="0.03797">$0.037970</td>
            <td data-value="0.00717">$0.007170</td>
            <td class="savings-positive" data-value="81.11667105609692">-81.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005088">$0.005088</td>
            <td data-value="0.00096">$0.000960</td>
            <td class="savings-positive" data-value="81.13207547169812">-81.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>asia-south2</td>
            <td data-value="0.03797">$0.037970</td>
            <td data-value="0.01074">$0.010740</td>
            <td class="savings-positive" data-value="71.71451145641295">-71.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005088">$0.005088</td>
            <td data-value="0.001437">$0.001437</td>
            <td class="savings-positive" data-value="71.75707547169812">-71.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>asia-southeast1</td>
            <td data-value="0.038999">$0.038999</td>
            <td data-value="0.00668">$0.006680</td>
            <td class="savings-positive" data-value="82.87135567578656">-82.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005226">$0.005226</td>
            <td data-value="0.000895">$0.000895</td>
            <td class="savings-positive" data-value="82.87409108304631">-82.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>asia-southeast2</td>
            <td data-value="0.04250891">$0.042509</td>
            <td data-value="0.00906">$0.009060</td>
            <td class="savings-positive" data-value="78.68682118642892">-78.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00569634">$0.005696</td>
            <td data-value="0.001213">$0.001213</td>
            <td class="savings-positive" data-value="78.70562501536075">-78.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>australia-southeast1</td>
            <td data-value="0.044856">$0.044856</td>
            <td data-value="0.01395">$0.013950</td>
            <td class="savings-positive" data-value="68.90048154093098">-68.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006011">$0.006011</td>
            <td data-value="0.001941">$0.001941</td>
            <td class="savings-positive" data-value="67.709199800366">-67.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>australia-southeast2</td>
            <td data-value="0.044856">$0.044856</td>
            <td data-value="0.01684">$0.016840</td>
            <td class="savings-positive" data-value="62.45764223292313">-62.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006011">$0.006011</td>
            <td data-value="0.002255">$0.002255</td>
            <td class="savings-positive" data-value="62.48544335385127">-62.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-central2</td>
            <td data-value="0.04073">$0.040730</td>
            <td data-value="0.0061">$0.006100</td>
            <td class="savings-positive" data-value="85.02332433095998">-85.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005458">$0.005458</td>
            <td data-value="0.000818">$0.000818</td>
            <td class="savings-positive" data-value="85.01282521069989">-85.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-north1</td>
            <td data-value="0.034806">$0.034806</td>
            <td data-value="0.00864">$0.008640</td>
            <td class="savings-positive" data-value="75.17669367350456">-75.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004664">$0.004664</td>
            <td data-value="0.001158">$0.001158</td>
            <td class="savings-positive" data-value="75.17152658662091">-75.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-north2</td>
            <td data-value="0.03319155">$0.033192</td>
            <td data-value="0.006636">$0.006636</td>
            <td class="savings-positive" data-value="80.00695960266995">-80.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00444885">$0.004449</td>
            <td data-value="0.00088935">$0.000889</td>
            <td class="savings-positive" data-value="80.00944064196365">-80.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-southwest1</td>
            <td data-value="0.03730098">$0.037301</td>
            <td data-value="0.0078529">$0.007853</td>
            <td class="savings-positive" data-value="78.9472019233811">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00499966">$0.005000</td>
            <td data-value="0.00105256">$0.001053</td>
            <td class="savings-positive" data-value="78.94736842105263">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-west1</td>
            <td data-value="0.034773">$0.034773</td>
            <td data-value="0.00955">$0.009550</td>
            <td class="savings-positive" data-value="72.53616311506053">-72.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004661">$0.004661</td>
            <td data-value="0.001279">$0.001279</td>
            <td class="savings-positive" data-value="72.55953658013303">-72.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-west10</td>
            <td data-value="0.04868094">$0.048681</td>
            <td data-value="0.0102487">$0.010249</td>
            <td class="savings-positive" data-value="78.9472019233811">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00652498">$0.006525</td>
            <td data-value="0.00137368">$0.001374</td>
            <td class="savings-positive" data-value="78.94736842105262">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-west12</td>
            <td data-value="0.04077819">$0.040778</td>
            <td data-value="0.00858495">$0.008585</td>
            <td class="savings-positive" data-value="78.9472019233811">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00546573">$0.005466</td>
            <td data-value="0.00115068">$0.001151</td>
            <td class="savings-positive" data-value="78.94736842105263">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-west2</td>
            <td data-value="0.04073">$0.040730</td>
            <td data-value="0.00848">$0.008480</td>
            <td class="savings-positive" data-value="79.17996562730174">-79.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005458">$0.005458</td>
            <td data-value="0.001134">$0.001134</td>
            <td class="savings-positive" data-value="79.22315866617808">-79.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-west3</td>
            <td data-value="0.04073">$0.040730</td>
            <td data-value="0.00843">$0.008430</td>
            <td class="savings-positive" data-value="79.30272526393321">-79.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005458">$0.005458</td>
            <td data-value="0.001132">$0.001132</td>
            <td class="savings-positive" data-value="79.25980212532062">-79.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-west4</td>
            <td data-value="0.034802">$0.034802</td>
            <td data-value="0.00777">$0.007770</td>
            <td class="savings-positive" data-value="77.67369691397047">-77.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004664">$0.004664</td>
            <td data-value="0.001047">$0.001047</td>
            <td class="savings-positive" data-value="77.55145797598627">-77.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-west6</td>
            <td data-value="0.044231">$0.044231</td>
            <td data-value="0.00977">$0.009770</td>
            <td class="savings-positive" data-value="77.91141959259342">-77.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005928">$0.005928</td>
            <td data-value="0.001317">$0.001317</td>
            <td class="savings-positive" data-value="77.78340080971661">-77.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-west8</td>
            <td data-value="0.03666876">$0.036669</td>
            <td data-value="0.0077198">$0.007720</td>
            <td class="savings-positive" data-value="78.9472019233811">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00491492">$0.004915</td>
            <td data-value="0.00103472">$0.001035</td>
            <td class="savings-positive" data-value="78.94736842105262">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>europe-west9</td>
            <td data-value="0.03666876">$0.036669</td>
            <td data-value="0.0077198">$0.007720</td>
            <td class="savings-positive" data-value="78.9472019233811">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00491492">$0.004915</td>
            <td data-value="0.00103472">$0.001035</td>
            <td class="savings-positive" data-value="78.94736842105262">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>me-central1</td>
            <td data-value="0.03840737">$0.038407</td>
            <td data-value="0.008085825">$0.008086</td>
            <td class="savings-positive" data-value="78.94720466410485">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005147955">$0.005148</td>
            <td data-value="0.00108378">$0.001084</td>
            <td class="savings-positive" data-value="78.94736842105262">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>me-central2</td>
            <td data-value="0.0505776">$0.050578</td>
            <td data-value="0.010648">$0.010648</td>
            <td class="savings-positive" data-value="78.9472019233811">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0067792">$0.006779</td>
            <td data-value="0.0014272">$0.001427</td>
            <td class="savings-positive" data-value="78.94736842105263">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>me-west1</td>
            <td data-value="0.0347721">$0.034772</td>
            <td data-value="0.00611">$0.006110</td>
            <td class="savings-positive" data-value="82.42844119279538">-82.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0046607">$0.004661</td>
            <td data-value="0.000818">$0.000818</td>
            <td class="savings-positive" data-value="82.44898834938958">-82.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>northamerica-northeast1</td>
            <td data-value="0.034802">$0.034802</td>
            <td data-value="0.00788">$0.007880</td>
            <td class="savings-positive" data-value="77.35762312510775">-77.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004664">$0.004664</td>
            <td data-value="0.001061">$0.001061</td>
            <td class="savings-positive" data-value="77.25128644939964">-77.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>northamerica-northeast2</td>
            <td data-value="0.034802">$0.034802</td>
            <td data-value="0.00989">$0.009890</td>
            <td class="savings-positive" data-value="71.5820929831619">-71.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004664">$0.004664</td>
            <td data-value="0.001325">$0.001325</td>
            <td class="savings-positive" data-value="71.5909090909091">-71.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>northamerica-south1</td>
            <td data-value="0">N/A</td>
            <td data-value="0.00872">$0.008720</td>
            <td class="savings-negative" data-value="0">N/A</td>
            <td class="trend-same">→</td>
            <td data-value="0.00461833">$0.004618</td>
            <td data-value="0.00111725">$0.001117</td>
            <td class="savings-positive" data-value="75.80835496813783">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>southamerica-east1</td>
            <td data-value="0.05018">$0.050180</td>
            <td data-value="0.0052">$0.005200</td>
            <td class="savings-positive" data-value="89.63730569948187">-89.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006725">$0.006725</td>
            <td data-value="0.000696">$0.000696</td>
            <td class="savings-positive" data-value="89.65055762081784">-89.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>southamerica-west1</td>
            <td data-value="0.04520373">$0.045204</td>
            <td data-value="0.00951665">$0.009517</td>
            <td class="savings-positive" data-value="78.9472019233811">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00605891">$0.006059</td>
            <td data-value="0.00127556">$0.001276</td>
            <td class="savings-positive" data-value="78.94736842105262">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>us-central1</td>
            <td data-value="0.031611">$0.031611</td>
            <td data-value="0.00836">$0.008360</td>
            <td class="savings-positive" data-value="73.55350985416469">-73.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004237">$0.004237</td>
            <td data-value="0.001072">$0.001072</td>
            <td class="savings-positive" data-value="74.69907953740854">-74.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>us-east4</td>
            <td data-value="0.035605">$0.035605</td>
            <td data-value="0.00881">$0.008810</td>
            <td class="savings-positive" data-value="75.25628422974302">-75.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004771">$0.004771</td>
            <td data-value="0.001027">$0.001027</td>
            <td class="savings-positive" data-value="78.47411444141689">-78.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>us-east5</td>
            <td data-value="0.031611">$0.031611</td>
            <td data-value="0.006655">$0.006655</td>
            <td class="savings-positive" data-value="78.9472019233811">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004237">$0.004237</td>
            <td data-value="0.000892">$0.000892</td>
            <td class="savings-positive" data-value="78.94736842105263">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>us-south1</td>
            <td data-value="0.03730098">$0.037301</td>
            <td data-value="0.0078529">$0.007853</td>
            <td class="savings-positive" data-value="78.9472019233811">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00499966">$0.005000</td>
            <td data-value="0.00105256">$0.001053</td>
            <td class="savings-positive" data-value="78.94736842105263">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>us-west2</td>
            <td data-value="0.03797">$0.037970</td>
            <td data-value="0.01016">$0.010160</td>
            <td class="savings-positive" data-value="73.24203318409269">-73.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005089">$0.005089</td>
            <td data-value="0.00137">$0.001370</td>
            <td class="savings-positive" data-value="73.07919041068973">-73.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>us-west3</td>
            <td data-value="0.03797">$0.037970</td>
            <td data-value="0.011">$0.011000</td>
            <td class="savings-positive" data-value="71.02976033710824">-71.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005089">$0.005089</td>
            <td data-value="0.001474">$0.001474</td>
            <td class="savings-positive" data-value="71.03556690901945">-71.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>us-west4</td>
            <td data-value="0.035605">$0.035605</td>
            <td data-value="0.00649">$0.006490</td>
            <td class="savings-positive" data-value="81.7722230023873">-81.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004771">$0.004771</td>
            <td data-value="0.000868">$0.000868</td>
            <td class="savings-positive" data-value="81.80674910920143">-81.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n1</td>
            <td>us-west8</td>
            <td data-value="0.031611">$0.031611</td>
            <td data-value="0.006655">$0.006655</td>
            <td class="savings-positive" data-value="78.9472019233811">-78.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004237">$0.004237</td>
            <td data-value="0.000892">$0.000892</td>
            <td class="savings-positive" data-value="78.94736842105263">-78.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>africa-south1</td>
            <td data-value="0.04134719">$0.041347</td>
            <td data-value="0.00785">$0.007850</td>
            <td class="savings-positive" data-value="81.01442927560494">-81.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005541996">$0.005542</td>
            <td data-value="0.002369">$0.002369</td>
            <td class="savings-positive" data-value="57.25366817298316">-57.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>asia-east1</td>
            <td data-value="0.036602">$0.036602</td>
            <td data-value="0.00688">$0.006880</td>
            <td class="savings-positive" data-value="81.20321293918366">-81.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004906">$0.004906</td>
            <td data-value="0.002397">$0.002397</td>
            <td class="savings-positive" data-value="51.14145943742356">-51.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>asia-east2</td>
            <td data-value="0.044231">$0.044231</td>
            <td data-value="0.01858">$0.018580</td>
            <td class="savings-positive" data-value="57.993262643847075">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005928">$0.005928</td>
            <td data-value="0.005093">$0.005093</td>
            <td class="savings-positive" data-value="14.085695006747635">-14.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>asia-northeast1</td>
            <td data-value="0.040618">$0.040618</td>
            <td data-value="0.010149">$0.010149</td>
            <td class="savings-positive" data-value="75.01354079472155">-75.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005419">$0.005419</td>
            <td data-value="0.003046">$0.003046</td>
            <td class="savings-positive" data-value="43.790367226425545">-43.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>asia-northeast2</td>
            <td data-value="0.040595">$0.040595</td>
            <td data-value="0.01379">$0.013790</td>
            <td class="savings-positive" data-value="66.0302992979431">-66.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005441">$0.005441</td>
            <td data-value="0.003969">$0.003969</td>
            <td class="savings-positive" data-value="27.05385039514794">-27.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>asia-northeast3</td>
            <td data-value="0.040595">$0.040595</td>
            <td data-value="0.01576">$0.015760</td>
            <td class="savings-positive" data-value="61.17748491193497">-61.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005441">$0.005441</td>
            <td data-value="0.004746">$0.004746</td>
            <td class="savings-positive" data-value="12.77338724499172">-12.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>asia-south1</td>
            <td data-value="0.03797">$0.037970</td>
            <td data-value="0.00814">$0.008140</td>
            <td class="savings-positive" data-value="78.56202264946009">-78.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005088">$0.005088</td>
            <td data-value="0.002878">$0.002878</td>
            <td class="savings-positive" data-value="43.435534591194966">-43.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>asia-south2</td>
            <td data-value="0.03797">$0.037970</td>
            <td data-value="0.005">$0.005000</td>
            <td class="savings-positive" data-value="86.83170924414011">-86.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005088">$0.005088</td>
            <td data-value="0.001739">$0.001739</td>
            <td class="savings-positive" data-value="65.82154088050314">-65.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>asia-southeast1</td>
            <td data-value="0.038999">$0.038999</td>
            <td data-value="0.01461">$0.014610</td>
            <td class="savings-positive" data-value="62.53750096156312">-62.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005226">$0.005226</td>
            <td data-value="0.00441">$0.004410</td>
            <td class="savings-positive" data-value="15.614236509758896">-15.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>asia-southeast2</td>
            <td data-value="0.04250891">$0.042509</td>
            <td data-value="0.01683">$0.016830</td>
            <td class="savings-positive" data-value="60.408300283399406">-60.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00569634">$0.005696</td>
            <td data-value="0.005078">$0.005078</td>
            <td class="savings-positive" data-value="10.85504025391743">-10.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>australia-southeast1</td>
            <td data-value="0.044856">$0.044856</td>
            <td data-value="0.0103">$0.010300</td>
            <td class="savings-positive" data-value="77.03763153201356">-77.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006011">$0.006011</td>
            <td data-value="0.003095">$0.003095</td>
            <td class="savings-positive" data-value="48.51106305107303">-48.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>australia-southeast2</td>
            <td data-value="0.038128">$0.038128</td>
            <td data-value="0.01021">$0.010210</td>
            <td class="savings-positive" data-value="73.22177926982795">-73.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005109">$0.005109</td>
            <td data-value="0.003082">$0.003082</td>
            <td class="savings-positive" data-value="39.67508318653357">-39.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-central2</td>
            <td data-value="0.04073">$0.040730</td>
            <td data-value="0.01163">$0.011630</td>
            <td class="savings-positive" data-value="71.44610851951879">-71.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005458">$0.005458</td>
            <td data-value="0.003502">$0.003502</td>
            <td class="savings-positive" data-value="35.83730304140712">-35.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-north1</td>
            <td data-value="0.034806">$0.034806</td>
            <td data-value="0.01067">$0.010670</td>
            <td class="savings-positive" data-value="69.34436591392289">-69.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004664">$0.004664</td>
            <td data-value="0.003235">$0.003235</td>
            <td class="savings-positive" data-value="30.638936535162948">-30.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-north2</td>
            <td data-value="0.03319155">$0.033192</td>
            <td data-value="0.0089985">$0.008998</td>
            <td class="savings-positive" data-value="72.88918414475974">-72.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00444885">$0.004449</td>
            <td data-value="0.0027951">$0.002795</td>
            <td class="savings-positive" data-value="37.172527731885765">-37.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-southwest1</td>
            <td data-value="0.03730098">$0.037301</td>
            <td data-value="0.00654">$0.006540</td>
            <td class="savings-positive" data-value="82.46694858955448">-82.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00499966">$0.005000</td>
            <td data-value="0.001972">$0.001972</td>
            <td class="savings-positive" data-value="60.55731789761705">-60.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-west1</td>
            <td data-value="0.034773">$0.034773</td>
            <td data-value="0.00443">$0.004430</td>
            <td class="savings-positive" data-value="87.26023063871395">-87.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004661">$0.004661</td>
            <td data-value="0.001338">$0.001338</td>
            <td class="savings-positive" data-value="71.2937137953229">-71.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-west10</td>
            <td data-value="0.04868094">$0.048681</td>
            <td data-value="0.00851">$0.008510</td>
            <td class="savings-positive" data-value="82.51882564305456">-82.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00652498">$0.006525</td>
            <td data-value="0.002291">$0.002291</td>
            <td class="savings-positive" data-value="64.88878126829508">-64.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-west12</td>
            <td data-value="0.04077819">$0.040778</td>
            <td data-value="0.01314">$0.013140</td>
            <td class="savings-positive" data-value="67.7768925006235">-67.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00546573">$0.005466</td>
            <td data-value="0.003962">$0.003962</td>
            <td class="savings-positive" data-value="27.511970038768833">-27.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-west2</td>
            <td data-value="0.04073">$0.040730</td>
            <td data-value="0.00555">$0.005550</td>
            <td class="savings-positive" data-value="86.37368033390621">-86.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005458">$0.005458</td>
            <td data-value="0.001484">$0.001484</td>
            <td class="savings-positive" data-value="72.81055331623305">-72.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-west3</td>
            <td data-value="0.04073">$0.040730</td>
            <td data-value="0.01711">$0.017110</td>
            <td class="savings-positive" data-value="57.99165234470907">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005458">$0.005458</td>
            <td data-value="0.004684">$0.004684</td>
            <td class="savings-positive" data-value="14.181018688164167">-14.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-west4</td>
            <td data-value="0.034802">$0.034802</td>
            <td data-value="0.01126">$0.011260</td>
            <td class="savings-positive" data-value="67.64553761278088">-67.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004664">$0.004664</td>
            <td data-value="0.003413">$0.003413</td>
            <td class="savings-positive" data-value="26.82246998284734">-26.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-west6</td>
            <td data-value="0.044221">$0.044221</td>
            <td data-value="0.01157">$0.011570</td>
            <td class="savings-positive" data-value="73.83596029035978">-73.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005927">$0.005927</td>
            <td data-value="0.003486">$0.003486</td>
            <td class="savings-positive" data-value="41.18441032562848">-41.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-west8</td>
            <td data-value="0.03666876">$0.036669</td>
            <td data-value="0.00623">$0.006230</td>
            <td class="savings-positive" data-value="83.01006088016067">-83.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00491492">$0.004915</td>
            <td data-value="0.001681">$0.001681</td>
            <td class="savings-positive" data-value="65.79801909288452">-65.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>europe-west9</td>
            <td data-value="0.03666876">$0.036669</td>
            <td data-value="0.01319">$0.013190</td>
            <td class="savings-positive" data-value="64.02932632573341">-64.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00491492">$0.004915</td>
            <td data-value="0.003975">$0.003975</td>
            <td class="savings-positive" data-value="19.123810763959526">-19.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>me-central1</td>
            <td data-value="0.03840737">$0.038407</td>
            <td data-value="0.00903">$0.009030</td>
            <td class="savings-positive" data-value="76.48888741926353">-76.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005147955">$0.005148</td>
            <td data-value="0.002722">$0.002722</td>
            <td class="savings-positive" data-value="47.12463492784999">-47.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>me-central2</td>
            <td data-value="0.0505776">$0.050578</td>
            <td data-value="0.00632">$0.006320</td>
            <td class="savings-positive" data-value="87.50434975166871">-87.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0067792">$0.006779</td>
            <td data-value="0.001905">$0.001905</td>
            <td class="savings-positive" data-value="71.89933915506255">-71.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>me-west1</td>
            <td data-value="0.0347721">$0.034772</td>
            <td data-value="0.01273">$0.012730</td>
            <td class="savings-positive" data-value="63.39018926093046">-63.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0046607">$0.004661</td>
            <td data-value="0.003839">$0.003839</td>
            <td class="savings-positive" data-value="17.63039886712297">-17.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>northamerica-northeast1</td>
            <td data-value="0.034802">$0.034802</td>
            <td data-value="0.01017">$0.010170</td>
            <td class="savings-positive" data-value="70.77754152060227">-70.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004664">$0.004664</td>
            <td data-value="0.003081">$0.003081</td>
            <td class="savings-positive" data-value="33.940823327615774">-33.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>northamerica-northeast2</td>
            <td data-value="0.034802">$0.034802</td>
            <td data-value="0.00371">$0.003710</td>
            <td class="savings-positive" data-value="89.33969312108499">-89.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004664">$0.004664</td>
            <td data-value="0.001117">$0.001117</td>
            <td class="savings-positive" data-value="76.05060034305318">-76.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>southamerica-east1</td>
            <td data-value="0.05018">$0.050180</td>
            <td data-value="0.01292">$0.012920</td>
            <td class="savings-positive" data-value="74.25269031486647">-74.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.006725">$0.006725</td>
            <td data-value="0.003897">$0.003897</td>
            <td class="savings-positive" data-value="42.05204460966543">-42.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>southamerica-west1</td>
            <td data-value="0.04520373">$0.045204</td>
            <td data-value="0.01214">$0.012140</td>
            <td class="savings-positive" data-value="73.14380915026261">-73.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00605891">$0.006059</td>
            <td data-value="0.003662">$0.003662</td>
            <td class="savings-positive" data-value="39.560085890036326">-39.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>us-central1</td>
            <td data-value="0.031611">$0.031611</td>
            <td data-value="0.01025">$0.010250</td>
            <td class="savings-positive" data-value="67.57457846952009">-67.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004237">$0.004237</td>
            <td data-value="0.003086">$0.003086</td>
            <td class="savings-positive" data-value="27.165447250413028">-27.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>us-east4</td>
            <td data-value="0.035605">$0.035605</td>
            <td data-value="0.01308">$0.013080</td>
            <td class="savings-positive" data-value="63.26358657491925">-63.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004771">$0.004771</td>
            <td data-value="0.003939">$0.003939</td>
            <td class="savings-positive" data-value="17.43869209809265">-17.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>us-east5</td>
            <td data-value="0.031611">$0.031611</td>
            <td data-value="0.00868">$0.008680</td>
            <td class="savings-positive" data-value="72.54120401126191">-72.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004237">$0.004237</td>
            <td data-value="0.002616">$0.002616</td>
            <td class="savings-positive" data-value="38.25820155770593">-38.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>us-south1</td>
            <td data-value="0.03730098">$0.037301</td>
            <td data-value="0.00943">$0.009430</td>
            <td class="savings-positive" data-value="74.71916287454108">-74.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00499966">$0.005000</td>
            <td data-value="0.002855">$0.002855</td>
            <td class="savings-positive" data-value="42.89611693595165">-42.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>us-west2</td>
            <td data-value="0.03797">$0.037970</td>
            <td data-value="0.0106">$0.010600</td>
            <td class="savings-positive" data-value="72.08322359757705">-72.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005089">$0.005089</td>
            <td data-value="0.003215">$0.003215</td>
            <td class="savings-positive" data-value="36.82452348202004">-36.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>us-west3</td>
            <td data-value="0.03797">$0.037970</td>
            <td data-value="0.01296">$0.012960</td>
            <td class="savings-positive" data-value="65.86779036081116">-65.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005089">$0.005089</td>
            <td data-value="0.003907">$0.003907</td>
            <td class="savings-positive" data-value="23.22656710552171">-23.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>us-west4</td>
            <td data-value="0.035603">$0.035603</td>
            <td data-value="0.01495">$0.014950</td>
            <td class="savings-positive" data-value="58.00915653175295">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004771">$0.004771</td>
            <td data-value="0.004302">$0.004302</td>
            <td class="savings-positive" data-value="9.83022427164116">-9.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2</td>
            <td>us-west8</td>
            <td data-value="0.031611">$0.031611</td>
            <td data-value="0.00877">$0.008770</td>
            <td class="savings-positive" data-value="72.2564929929455">-72.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004237">$0.004237</td>
            <td data-value="0.002662">$0.002662</td>
            <td class="savings-positive" data-value="37.17252773188577">-37.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>africa-south1</td>
            <td data-value="0.03597262">$0.035973</td>
            <td data-value="0.00613">$0.006130</td>
            <td class="savings-positive" data-value="82.95926179410897">-83.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004821288">$0.004821</td>
            <td data-value="0.001853">$0.001853</td>
            <td class="savings-positive" data-value="61.56628685114849">-61.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>asia-east1</td>
            <td data-value="0.031844">$0.031844</td>
            <td data-value="0.01337">$0.013370</td>
            <td class="savings-positive" data-value="58.0140685843487">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004268">$0.004268</td>
            <td data-value="0.003848">$0.003848</td>
            <td class="savings-positive" data-value="9.840674789128402">-9.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>asia-east2</td>
            <td data-value="0.038481">$0.038481</td>
            <td data-value="0.00838">$0.008380</td>
            <td class="savings-positive" data-value="78.22301915230894">-78.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005157">$0.005157</td>
            <td data-value="0.00252">$0.002520</td>
            <td class="savings-positive" data-value="51.13438045375218">-51.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>asia-northeast1</td>
            <td data-value="0.035338">$0.035338</td>
            <td data-value="0.00977">$0.009770</td>
            <td class="savings-positive" data-value="72.35270813288811">-72.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004715">$0.004715</td>
            <td data-value="0.00293">$0.002930</td>
            <td class="savings-positive" data-value="37.857900318133616">-37.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>asia-northeast2</td>
            <td data-value="0.035318">$0.035318</td>
            <td data-value="0.00454">$0.004540</td>
            <td class="savings-positive" data-value="87.14536496970385">-87.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004734">$0.004734</td>
            <td data-value="0.001367">$0.001367</td>
            <td class="savings-positive" data-value="71.12378538234051">-71.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>asia-northeast3</td>
            <td data-value="0.035318">$0.035318</td>
            <td data-value="0.00577">$0.005770</td>
            <td class="savings-positive" data-value="83.66272155841214">-83.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004734">$0.004734</td>
            <td data-value="0.001552">$0.001552</td>
            <td class="savings-positive" data-value="67.21588508660751">-67.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>asia-south1</td>
            <td data-value="0.018151">$0.018151</td>
            <td data-value="0.00648">$0.006480</td>
            <td class="savings-positive" data-value="64.29948763153546">-64.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.002433">$0.002433</td>
            <td data-value="0.001954">$0.001954</td>
            <td class="savings-positive" data-value="19.687628442252358">-19.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>asia-south2</td>
            <td data-value="0.033034">$0.033034</td>
            <td data-value="0.00573">$0.005730</td>
            <td class="savings-positive" data-value="82.65423503057457">-82.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004427">$0.004427</td>
            <td data-value="0.001729">$0.001729</td>
            <td class="savings-positive" data-value="60.94420600858369">-60.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>asia-southeast1</td>
            <td data-value="0.033929">$0.033929</td>
            <td data-value="0.00747">$0.007470</td>
            <td class="savings-positive" data-value="77.98343599870317">-78.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004547">$0.004547</td>
            <td data-value="0.002245">$0.002245</td>
            <td class="savings-positive" data-value="50.626786892456565">-50.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>asia-southeast2</td>
            <td data-value="0.03698261">$0.036983</td>
            <td data-value="0.00705">$0.007050</td>
            <td class="savings-positive" data-value="80.93698632952082">-80.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00495623">$0.004956</td>
            <td data-value="0.002123">$0.002123</td>
            <td class="savings-positive" data-value="57.16502260790964">-57.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>australia-southeast1</td>
            <td data-value="0.039025">$0.039025</td>
            <td data-value="0.01165">$0.011650</td>
            <td class="savings-positive" data-value="70.14734144778988">-70.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00523">$0.005230</td>
            <td data-value="0.0035">$0.003500</td>
            <td class="savings-positive" data-value="33.07839388145315">-33.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>australia-southeast2</td>
            <td data-value="0.033171">$0.033171</td>
            <td data-value="0.00943">$0.009430</td>
            <td class="savings-positive" data-value="71.57155346537638">-71.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004446">$0.004446</td>
            <td data-value="0.002843">$0.002843</td>
            <td class="savings-positive" data-value="36.0548807917229">-36.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-central2</td>
            <td data-value="0.035435">$0.035435</td>
            <td data-value="0.012">$0.012000</td>
            <td class="savings-positive" data-value="66.13517708480316">-66.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004748">$0.004748</td>
            <td data-value="0.003609">$0.003609</td>
            <td class="savings-positive" data-value="23.989048020219037">-24.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-north1</td>
            <td data-value="0.030281">$0.030281</td>
            <td data-value="0.00602">$0.006020</td>
            <td class="savings-positive" data-value="80.119546910604">-80.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004058">$0.004058</td>
            <td data-value="0.001897">$0.001897</td>
            <td class="savings-positive" data-value="53.25283390832922">-53.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-north2</td>
            <td data-value="0.0288771">$0.028877</td>
            <td data-value="0.0054915">$0.005491</td>
            <td class="savings-positive" data-value="80.98320122172933">-81.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0038703">$0.003870</td>
            <td data-value="0.00079275">$0.000793</td>
            <td class="savings-positive" data-value="79.51709169831796">-79.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-southwest1</td>
            <td data-value="0.03245236">$0.032452</td>
            <td data-value="0.0086">$0.008600</td>
            <td class="savings-positive" data-value="73.49961605257677">-73.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00434948">$0.004349</td>
            <td data-value="0.002601">$0.002601</td>
            <td class="savings-positive" data-value="40.199748015854766">-40.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-west1</td>
            <td data-value="0.030253">$0.030253</td>
            <td data-value="0.01065">$0.010650</td>
            <td class="savings-positive" data-value="64.79687964829934">-64.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004055">$0.004055</td>
            <td data-value="0.003061">$0.003061</td>
            <td class="savings-positive" data-value="24.51294697903822">-24.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-west10</td>
            <td data-value="0.04235308">$0.042353</td>
            <td data-value="0.00721">$0.007210</td>
            <td class="savings-positive" data-value="82.97644468832019">-83.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00567644">$0.005676</td>
            <td data-value="0.002175">$0.002175</td>
            <td class="savings-positive" data-value="61.68373135274926">-61.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-west12</td>
            <td data-value="0.03547758">$0.035478</td>
            <td data-value="0.00335">$0.003350</td>
            <td class="savings-positive" data-value="90.55741682493564">-90.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00475494">$0.004755</td>
            <td data-value="0.001013">$0.001013</td>
            <td class="savings-positive" data-value="78.6958405363685">-78.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-west2</td>
            <td data-value="0.035435">$0.035435</td>
            <td data-value="0.00962">$0.009620</td>
            <td class="savings-positive" data-value="72.8517002963172">-72.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004748">$0.004748</td>
            <td data-value="0.002904">$0.002904</td>
            <td class="savings-positive" data-value="38.83740522325189">-38.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-west3</td>
            <td data-value="0.035435">$0.035435</td>
            <td data-value="0.01488">$0.014880</td>
            <td class="savings-positive" data-value="58.00761958515592">-58.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004748">$0.004748</td>
            <td data-value="0.004075">$0.004075</td>
            <td class="savings-positive" data-value="14.174389216512218">-14.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-west4</td>
            <td data-value="0.030278">$0.030278</td>
            <td data-value="0.00478">$0.004780</td>
            <td class="savings-positive" data-value="84.21295990488143">-84.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004058">$0.004058</td>
            <td data-value="0.001784">$0.001784</td>
            <td class="savings-positive" data-value="56.03745687530803">-56.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-west6</td>
            <td data-value="0.038473">$0.038473</td>
            <td data-value="0.00929">$0.009290</td>
            <td class="savings-positive" data-value="75.8531957476672">-75.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005156">$0.005156</td>
            <td data-value="0.002801">$0.002801</td>
            <td class="savings-positive" data-value="45.67494181536074">-45.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-west8</td>
            <td data-value="0.03190232">$0.031902</td>
            <td data-value="0.00403">$0.004030</td>
            <td class="savings-positive" data-value="87.36768987333838">-87.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00427576">$0.004276</td>
            <td data-value="0.001214">$0.001214</td>
            <td class="savings-positive" data-value="71.6073867569742">-71.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>europe-west9</td>
            <td data-value="0.03190232">$0.031902</td>
            <td data-value="0.00787">$0.007870</td>
            <td class="savings-positive" data-value="75.33094771790891">-75.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00427576">$0.004276</td>
            <td data-value="0.002369">$0.002369</td>
            <td class="savings-positive" data-value="44.59464516249743">-44.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>me-central1</td>
            <td data-value="0.03341493">$0.033415</td>
            <td data-value="0.00506">$0.005060</td>
            <td class="savings-positive" data-value="84.85706838230695">-84.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00447849">$0.004478</td>
            <td data-value="0.001524">$0.001524</td>
            <td class="savings-positive" data-value="65.97067315099508">-66.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>me-central2</td>
            <td data-value="0.0440032">$0.044003</td>
            <td data-value="0.00524">$0.005240</td>
            <td class="savings-positive" data-value="88.09177514362591">-88.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0058976">$0.005898</td>
            <td data-value="0.001583">$0.001583</td>
            <td class="savings-positive" data-value="73.15857297883885">-73.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>me-west1</td>
            <td data-value="0.0302522">$0.030252</td>
            <td data-value="0.0054">$0.005400</td>
            <td class="savings-positive" data-value="82.15005850814156">-82.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0040546">$0.004055</td>
            <td data-value="0.001632">$0.001632</td>
            <td class="savings-positive" data-value="59.74942041138461">-59.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>northamerica-northeast1</td>
            <td data-value="0.030278">$0.030278</td>
            <td data-value="0.01211">$0.012110</td>
            <td class="savings-positive" data-value="60.00396327366405">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004058">$0.004058</td>
            <td data-value="0.003259">$0.003259</td>
            <td class="savings-positive" data-value="19.689502217841294">-19.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>northamerica-northeast2</td>
            <td data-value="0.030278">$0.030278</td>
            <td data-value="0.00657">$0.006570</td>
            <td class="savings-positive" data-value="78.30107668934541">-78.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004058">$0.004058</td>
            <td data-value="0.001982">$0.001982</td>
            <td class="savings-positive" data-value="51.1582060128142">-51.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>southamerica-east1</td>
            <td data-value="0.043657">$0.043657</td>
            <td data-value="0.00873">$0.008730</td>
            <td class="savings-positive" data-value="80.00320681677623">-80.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005851">$0.005851</td>
            <td data-value="0.002639">$0.002639</td>
            <td class="savings-positive" data-value="54.8965988719877">-54.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>southamerica-west1</td>
            <td data-value="0.03932786">$0.039328</td>
            <td data-value="0.00552">$0.005520</td>
            <td class="savings-positive" data-value="85.96414857050448">-86.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00527098">$0.005271</td>
            <td data-value="0.001665">$0.001665</td>
            <td class="savings-positive" data-value="68.41194616560867">-68.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>us-central1</td>
            <td data-value="0.027502">$0.027502</td>
            <td data-value="0.00573">$0.005730</td>
            <td class="savings-positive" data-value="79.16515162533634">-79.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003686">$0.003686</td>
            <td data-value="0.000766">$0.000766</td>
            <td class="savings-positive" data-value="79.2186652197504">-79.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>us-east4</td>
            <td data-value="0.030976">$0.030976</td>
            <td data-value="0.00777">$0.007770</td>
            <td class="savings-positive" data-value="74.91606404958678">-74.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004151">$0.004151</td>
            <td data-value="0.002868">$0.002868</td>
            <td class="savings-positive" data-value="30.908214887978808">-30.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>us-east5</td>
            <td data-value="0.027502">$0.027502</td>
            <td data-value="0.00352">$0.003520</td>
            <td class="savings-positive" data-value="87.20093084139336">-87.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003686">$0.003686</td>
            <td data-value="0.001064">$0.001064</td>
            <td class="savings-positive" data-value="71.1340206185567">-71.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>us-south1</td>
            <td data-value="0.03245236">$0.032452</td>
            <td data-value="0.00527">$0.005270</td>
            <td class="savings-positive" data-value="83.76081123221854">-83.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00434948">$0.004349</td>
            <td data-value="0.00099002">$0.000990</td>
            <td class="savings-positive" data-value="77.23819858925664">-77.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>us-west2</td>
            <td data-value="0.033034">$0.033034</td>
            <td data-value="0.00972">$0.009720</td>
            <td class="savings-positive" data-value="70.57577041835684">-70.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004427">$0.004427</td>
            <td data-value="0.003088">$0.003088</td>
            <td class="savings-positive" data-value="30.24621639936752">-30.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>us-west3</td>
            <td data-value="0.033034">$0.033034</td>
            <td data-value="0.00764">$0.007640</td>
            <td class="savings-positive" data-value="76.8723133740994">-76.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004427">$0.004427</td>
            <td data-value="0.002113">$0.002113</td>
            <td class="savings-positive" data-value="52.270160379489504">-52.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>us-west4</td>
            <td data-value="0.030976">$0.030976</td>
            <td data-value="0.00901">$0.009010</td>
            <td class="savings-positive" data-value="70.91296487603306">-70.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004151">$0.004151</td>
            <td data-value="0.002716">$0.002716</td>
            <td class="savings-positive" data-value="34.56998313659359">-34.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>n2d</td>
            <td>us-west8</td>
            <td data-value="0.027502">$0.027502</td>
            <td data-value="0.0048">$0.004800</td>
            <td class="savings-positive" data-value="82.5467238746273">-82.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003686">$0.003686</td>
            <td data-value="0.000839">$0.000839</td>
            <td class="savings-positive" data-value="77.23819858925664">-77.2%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2a</td>
            <td>asia-southeast1</td>
            <td data-value="0.03072">$0.030720</td>
            <td data-value="0.00915">$0.009150</td>
            <td class="savings-positive" data-value="70.21484375">-70.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00419">$0.004190</td>
            <td data-value="0.001246">$0.001246</td>
            <td class="savings-positive" data-value="70.26252983293557">-70.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2a</td>
            <td>europe-west4</td>
            <td data-value="0.02616409">$0.026164</td>
            <td data-value="0.008223">$0.008223</td>
            <td class="savings-positive" data-value="68.57142747941931">-68.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00357">$0.003570</td>
            <td data-value="0.001122">$0.001122</td>
            <td class="savings-positive" data-value="68.57142857142856">-68.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2a</td>
            <td>us-central1</td>
            <td data-value="0.0249">$0.024900</td>
            <td data-value="0.00596">$0.005960</td>
            <td class="savings-positive" data-value="76.06425702811245">-76.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0034">$0.003400</td>
            <td data-value="0.000813">$0.000813</td>
            <td class="savings-positive" data-value="76.08823529411765">-76.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>africa-south1</td>
            <td data-value="0.03597262">$0.035973</td>
            <td data-value="0.00385">$0.003850</td>
            <td class="savings-positive" data-value="89.29741564556599">-89.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004821288">$0.004821</td>
            <td data-value="0.000516">$0.000516</td>
            <td class="savings-positive" data-value="89.29746573944556">-89.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>asia-east1</td>
            <td data-value="0.031844">$0.031844</td>
            <td data-value="0.00682">$0.006820</td>
            <td class="savings-positive" data-value="78.58309257630951">-78.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004268">$0.004268</td>
            <td data-value="0.000915">$0.000915</td>
            <td class="savings-positive" data-value="78.56138706654171">-78.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>asia-east2</td>
            <td data-value="0.038481">$0.038481</td>
            <td data-value="0.00636">$0.006360</td>
            <td class="savings-positive" data-value="83.47236298432993">-83.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005157">$0.005157</td>
            <td data-value="0.000853">$0.000853</td>
            <td class="savings-positive" data-value="83.45937560597247">-83.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>asia-northeast1</td>
            <td data-value="0.035338">$0.035338</td>
            <td data-value="0.00652">$0.006520</td>
            <td class="savings-positive" data-value="81.54960665572473">-81.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004715">$0.004715</td>
            <td data-value="0.000868">$0.000868</td>
            <td class="savings-positive" data-value="81.59066808059386">-81.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>asia-northeast2</td>
            <td data-value="0.035318">$0.035318</td>
            <td data-value="0.01413">$0.014130</td>
            <td class="savings-positive" data-value="59.99207203125885">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004734">$0.004734</td>
            <td data-value="0.001894">$0.001894</td>
            <td class="savings-positive" data-value="59.991550485847064">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>asia-northeast3</td>
            <td data-value="0.035318">$0.035318</td>
            <td data-value="0.00812">$0.008120</td>
            <td class="savings-positive" data-value="77.00889065065971">-77.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004734">$0.004734</td>
            <td data-value="0.001089">$0.001089</td>
            <td class="savings-positive" data-value="76.9961977186312">-77.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>asia-south1</td>
            <td data-value="0.018151">$0.018151</td>
            <td data-value="0.00726">$0.007260</td>
            <td class="savings-positive" data-value="60.00220373533139">-60.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.002433">$0.002433</td>
            <td data-value="0.000974">$0.000974</td>
            <td class="savings-positive" data-value="59.96711878339498">-60.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>asia-south2</td>
            <td data-value="0.033034">$0.033034</td>
            <td data-value="0.00802">$0.008020</td>
            <td class="savings-positive" data-value="75.72198341103106">-75.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004427">$0.004427</td>
            <td data-value="0.001074">$0.001074</td>
            <td class="savings-positive" data-value="75.73977863112718">-75.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>asia-southeast1</td>
            <td data-value="0.033929">$0.033929</td>
            <td data-value="0.0087">$0.008700</td>
            <td class="savings-positive" data-value="74.35821863302779">-74.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004547">$0.004547</td>
            <td data-value="0.001164">$0.001164</td>
            <td class="savings-positive" data-value="74.40070376072136">-74.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>asia-southeast2</td>
            <td data-value="0.03698261">$0.036983</td>
            <td data-value="0.00728">$0.007280</td>
            <td class="savings-positive" data-value="80.31507240835624">-80.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00495623">$0.004956</td>
            <td data-value="0.000976">$0.000976</td>
            <td class="savings-positive" data-value="80.30761284282609">-80.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>australia-southeast1</td>
            <td data-value="0.039025">$0.039025</td>
            <td data-value="0.00965">$0.009650</td>
            <td class="savings-positive" data-value="75.27226137091608">-75.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00523">$0.005230</td>
            <td data-value="0.00129">$0.001290</td>
            <td class="savings-positive" data-value="75.33460803059275">-75.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>australia-southeast2</td>
            <td data-value="0.039025">$0.039025</td>
            <td data-value="0.00903">$0.009030</td>
            <td class="savings-positive" data-value="76.86098654708519">-76.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00523">$0.005230</td>
            <td data-value="0.00121">$0.001210</td>
            <td class="savings-positive" data-value="76.8642447418738">-76.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-central2</td>
            <td data-value="0.035435">$0.035435</td>
            <td data-value="0.00889">$0.008890</td>
            <td class="savings-positive" data-value="74.91181035699167">-74.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004748">$0.004748</td>
            <td data-value="0.001189">$0.001189</td>
            <td class="savings-positive" data-value="74.95787700084246">-75.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-north1</td>
            <td data-value="0.030281">$0.030281</td>
            <td data-value="0.00468">$0.004680</td>
            <td class="savings-positive" data-value="84.5447640434596">-84.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004058">$0.004058</td>
            <td data-value="0.000625">$0.000625</td>
            <td class="savings-positive" data-value="84.59832429768358">-84.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-north2</td>
            <td data-value="0.0288771">$0.028877</td>
            <td data-value="0.0041055">$0.004105</td>
            <td class="savings-positive" data-value="85.78285215620681">-85.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0038703">$0.003870</td>
            <td data-value="0.0005502">$0.000550</td>
            <td class="savings-positive" data-value="85.78404774823657">-85.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-southwest1</td>
            <td data-value="0.03245236">$0.032452</td>
            <td data-value="0.00332">$0.003320</td>
            <td class="savings-positive" data-value="89.76961922029707">-89.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00434948">$0.004349</td>
            <td data-value="0.000444">$0.000444</td>
            <td class="savings-positive" data-value="89.79188316764302">-89.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-west1</td>
            <td data-value="0.030253">$0.030253</td>
            <td data-value="0.01089">$0.010890</td>
            <td class="savings-positive" data-value="64.00356989389482">-64.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004055">$0.004055</td>
            <td data-value="0.00146">$0.001460</td>
            <td class="savings-positive" data-value="63.995067817509245">-64.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-west10</td>
            <td data-value="0.04235308">$0.042353</td>
            <td data-value="0.00546">$0.005460</td>
            <td class="savings-positive" data-value="87.10837558921335">-87.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00567644">$0.005676</td>
            <td data-value="0.00073">$0.000730</td>
            <td class="savings-positive" data-value="87.13982707471585">-87.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-west12</td>
            <td data-value="0.03547758">$0.035478</td>
            <td data-value="0.00437">$0.004370</td>
            <td class="savings-positive" data-value="87.6823616492444">-87.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00475494">$0.004755</td>
            <td data-value="0.000585">$0.000585</td>
            <td class="savings-positive" data-value="87.69700564044973">-87.7%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-west2</td>
            <td data-value="0.035435">$0.035435</td>
            <td data-value="0.0064">$0.006400</td>
            <td class="savings-positive" data-value="81.93876111189502">-81.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004748">$0.004748</td>
            <td data-value="0.000857">$0.000857</td>
            <td class="savings-positive" data-value="81.9502948609941">-82.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-west3</td>
            <td data-value="0.035435">$0.035435</td>
            <td data-value="0.01228">$0.012280</td>
            <td class="savings-positive" data-value="65.34499788344857">-65.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004748">$0.004748</td>
            <td data-value="0.001642">$0.001642</td>
            <td class="savings-positive" data-value="65.41701769165964">-65.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-west4</td>
            <td data-value="0.030278">$0.030278</td>
            <td data-value="0.00682">$0.006820</td>
            <td class="savings-positive" data-value="77.47539467600237">-77.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004058">$0.004058</td>
            <td data-value="0.000914">$0.000914</td>
            <td class="savings-positive" data-value="77.47658945293249">-77.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-west6</td>
            <td data-value="0.038473">$0.038473</td>
            <td data-value="0.00756">$0.007560</td>
            <td class="savings-positive" data-value="80.34985574298858">-80.3%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005156">$0.005156</td>
            <td data-value="0.001014">$0.001014</td>
            <td class="savings-positive" data-value="80.33359193173001">-80.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-west8</td>
            <td data-value="0.03190232">$0.031902</td>
            <td data-value="0.00349">$0.003490</td>
            <td class="savings-positive" data-value="89.06035673894563">-89.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00427576">$0.004276</td>
            <td data-value="0.000468">$0.000468</td>
            <td class="savings-positive" data-value="89.05457743184837">-89.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>europe-west9</td>
            <td data-value="0.03190232">$0.031902</td>
            <td data-value="0.00346">$0.003460</td>
            <td class="savings-positive" data-value="89.15439378703492">-89.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00427576">$0.004276</td>
            <td data-value="0.000466">$0.000466</td>
            <td class="savings-positive" data-value="89.10135274196868">-89.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>me-central1</td>
            <td data-value="0.03341493">$0.033415</td>
            <td data-value="0.00364">$0.003640</td>
            <td class="savings-positive" data-value="89.10666579280579">-89.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00447849">$0.004478</td>
            <td data-value="0.000488">$0.000488</td>
            <td class="savings-positive" data-value="89.10347014283832">-89.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>me-central2</td>
            <td data-value="0.0440032">$0.044003</td>
            <td data-value="0.00593">$0.005930</td>
            <td class="savings-positive" data-value="86.52370736673697">-86.5%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0058976">$0.005898</td>
            <td data-value="0.000794">$0.000794</td>
            <td class="savings-positive" data-value="86.53689636462289">-86.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>me-west1</td>
            <td data-value="0.0302522">$0.030252</td>
            <td data-value="0.00491">$0.004910</td>
            <td class="savings-positive" data-value="83.76977542129167">-83.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.0040546">$0.004055</td>
            <td data-value="0.000658">$0.000658</td>
            <td class="savings-positive" data-value="83.7715187688058">-83.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>northamerica-northeast1</td>
            <td data-value="0.030278">$0.030278</td>
            <td data-value="0.00448">$0.004480</td>
            <td class="savings-positive" data-value="85.20377832089306">-85.2%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004058">$0.004058</td>
            <td data-value="0.000603">$0.000603</td>
            <td class="savings-positive" data-value="85.14046328240512">-85.1%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>northamerica-northeast2</td>
            <td data-value="0.030278">$0.030278</td>
            <td data-value="0.00556">$0.005560</td>
            <td class="savings-positive" data-value="81.6368320232512">-81.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004058">$0.004058</td>
            <td data-value="0.000749">$0.000749</td>
            <td class="savings-positive" data-value="81.54263183834401">-81.5%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>southamerica-east1</td>
            <td data-value="0.043657">$0.043657</td>
            <td data-value="0.01443">$0.014430</td>
            <td class="savings-positive" data-value="66.94688137068512">-66.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.005851">$0.005851</td>
            <td data-value="0.001936">$0.001936</td>
            <td class="savings-positive" data-value="66.91163903606221">-66.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>southamerica-west1</td>
            <td data-value="0.03932786">$0.039328</td>
            <td data-value="0.00497">$0.004970</td>
            <td class="savings-positive" data-value="87.36264826003753">-87.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00527098">$0.005271</td>
            <td data-value="0.000666">$0.000666</td>
            <td class="savings-positive" data-value="87.36477846624346">-87.4%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>us-central1</td>
            <td data-value="0.027502">$0.027502</td>
            <td data-value="0.0045">$0.004500</td>
            <td class="savings-positive" data-value="83.6375536324631">-83.6%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003686">$0.003686</td>
            <td data-value="0.000603">$0.000603</td>
            <td class="savings-positive" data-value="83.64080303852414">-83.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>us-east4</td>
            <td data-value="0.030976">$0.030976</td>
            <td data-value="0.00749">$0.007490</td>
            <td class="savings-positive" data-value="75.81998966942149">-75.8%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004151">$0.004151</td>
            <td data-value="0.001004">$0.001004</td>
            <td class="savings-positive" data-value="75.813057094676">-75.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>us-east5</td>
            <td data-value="0.027502">$0.027502</td>
            <td data-value="0.00248">$0.002480</td>
            <td class="savings-positive" data-value="90.98247400189076">-91.0%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003686">$0.003686</td>
            <td data-value="0.000332">$0.000332</td>
            <td class="savings-positive" data-value="90.99294628323386">-91.0%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>us-south1</td>
            <td data-value="0.03245236">$0.032452</td>
            <td data-value="0.00489476">$0.004895</td>
            <td class="savings-positive" data-value="84.9170907755245">-84.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.00434948">$0.004349</td>
            <td data-value="0.00065643">$0.000656</td>
            <td class="savings-positive" data-value="84.90785105345927">-84.9%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>us-west2</td>
            <td data-value="0.033034">$0.033034</td>
            <td data-value="0.00679">$0.006790</td>
            <td class="savings-positive" data-value="79.44541987043652">-79.4%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004427">$0.004427</td>
            <td data-value="0.000915">$0.000915</td>
            <td class="savings-positive" data-value="79.33137564942399">-79.3%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>us-west3</td>
            <td data-value="0.033034">$0.033034</td>
            <td data-value="0.00763">$0.007630</td>
            <td class="savings-positive" data-value="76.9025852152328">-76.9%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004427">$0.004427</td>
            <td data-value="0.001028">$0.001028</td>
            <td class="savings-positive" data-value="76.77885701377907">-76.8%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>us-west4</td>
            <td data-value="0.030976">$0.030976</td>
            <td data-value="0.00785">$0.007850</td>
            <td class="savings-positive" data-value="74.65779958677686">-74.7%</td>
            <td class="trend-same">→</td>
            <td data-value="0.004151">$0.004151</td>
            <td data-value="0.001053">$0.001053</td>
            <td class="savings-positive" data-value="74.63261864610938">-74.6%</td>
            <td class="trend-same">→</td>
        </tr>        <tr>
            <td>t2d</td>
            <td>us-west8</td>
            <td data-value="0.027502">$0.027502</td>
            <td data-value="0.00601">$0.006010</td>
            <td class="savings-positive" data-value="78.14704385135626">-78.1%</td>
            <td class="trend-same">→</td>
            <td data-value="0.003686">$0.003686</td>
            <td data-value="0.000806">$0.000806</td>
            <td class="savings-positive" data-value="78.13347802495932">-78.1%</td>
            <td class="trend-same">→</td>
        </tr>    </tbody>
</table>

<script>
    let currentSortColumn = -1;
    let sortAscending = true;
    
    function filterTable() {
        const machineType = document.getElementById('machineType').value.toLowerCase();
        const rows = document.querySelectorAll('#pricingTable tbody tr');
        
        rows.forEach(row => {
            const machineTypeCell = row.cells[0].textContent.toLowerCase();
            row.style.display = !machineType || machineTypeCell === machineType ? '' : 'none';
        });
    }
    
    function sortTable(column) {
        const table = document.getElementById('pricingTable');
        const headers = table.getElementsByTagName('th');
        const tbody = table.getElementsByTagName('tbody')[0];
        const rows = Array.from(tbody.getElementsByTagName('tr'));
        
        // Toggle sort direction if clicking the same column
        if (currentSortColumn === column) {
            sortAscending = !sortAscending;
        } else {
            sortAscending = true;
            currentSortColumn = column;
        }
        
        // Update active sort column style
        Array.from(headers).forEach(header => header.classList.remove('active-sort'));
        headers[column].classList.add('active-sort');
        
        // Sort rows
        rows.sort((a, b) => {
            let aValue = a.cells[column].getAttribute('data-value');
            let bValue = b.cells[column].getAttribute('data-value');
            
            // If no data-value attribute, use text content
            if (!aValue) aValue = a.cells[column].textContent.toLowerCase();
            if (!bValue) bValue = b.cells[column].textContent.toLowerCase();
            
            // Convert to numbers for numeric columns
            if (!isNaN(aValue)) {
                aValue = parseFloat(aValue);
                bValue = parseFloat(bValue);
            }
            
            if (aValue < bValue) return sortAscending ? -1 : 1;
            if (aValue > bValue) return sortAscending ? 1 : -1;
            return 0;
        });
        
        // Reorder rows
        rows.forEach(row => tbody.appendChild(row));
    }
</script>

