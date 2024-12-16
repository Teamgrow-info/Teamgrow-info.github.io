function animateValue(element, start, end, duration) {
    // Clear any existing content (including noscript tag)
    element.textContent = start;
    
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        // Use easeOutQuart for faster start and smoother end
        const easing = 1 - Math.pow(1 - progress, 4);
        const current = Math.floor(easing * (end - start) + start);
        
        if (element.dataset.style === 'currency') {
            element.textContent = '$' + current.toLocaleString('en-US');
        } else {
            element.textContent = current + '%';
        }
        
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

// Intersection Observer to trigger animation when stats come into view
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const element = entry.target;
            const finalValue = parseInt(element.dataset.value);
            animateValue(element, 0, finalValue, 700); // Adjusted to 0.7 seconds
            observer.unobserve(element);
        }
    });
}, {
    threshold: 0.1
});

// Start observing stat numbers when the page loads
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.stat-number').forEach(statElement => {
        observer.observe(statElement);
    });
});
