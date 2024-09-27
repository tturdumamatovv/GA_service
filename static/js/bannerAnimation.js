
// Function to handle visibility and animate only once
const handleBannerVisibility = (entries, observer) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            // Stop observing this banner after it's visible (animation triggers only once)
            observer.unobserve(entry.target);
        }
    });
};

// Initialize an observer for all `.banner-bg` elements
const initBannerObserver = () => {
    const banners = document.querySelectorAll(".banner-bg");

    if (!banners.length) {
        console.error("No elements with class '.banner-bg' found in the DOM.");
        return; // Exit if no banner elements to observe
    }

    const observer = new IntersectionObserver(handleBannerVisibility, {
        root: null, // Default to viewport
        threshold: 0.5, // 50% of the element must be in view
        rootMargin: "-25% 0px 0px 0px", // Top and bottom margin to help center the trigger
    });

    // Observe each banner individually
    banners.forEach((banner) => {
        observer.observe(banner);
    });
};

// Initialize observers for both the counter and the banner when DOM is ready
document.addEventListener("DOMContentLoaded", () => {
    initCounterObserver(); // Your counter observer
    initBannerObserver(); // Observer for banner visibility
});
