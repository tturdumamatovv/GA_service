// How long you want the animation to take, in ms
const animationDuration = 2000;
// Calculate how long each ‘frame’ should last if we want to update the animation 60 times per second
const frameDuration = 1000 / 60;
// Use that to calculate how many frames we need to complete the animation
const totalFrames = Math.round(animationDuration / frameDuration);
// An ease-out function that slows the count as it progresses
const easeOutQuad = t => t * (2 - t);

// The animation function, which takes an Element
const animateCountUp = (el) => {
    let frame = 0;
    const countTo = parseInt(el.innerHTML, 10);

    if (isNaN(countTo)) return; // Handle non-numeric innerHTML

    const counter = setInterval(() => {
        frame++;
        // Calculate our progress as a value between 0 and 1
        const progress = easeOutQuad(frame / totalFrames);
        // Use the progress value to calculate the current count
        const currentCount = Math.round(countTo * progress);

        // If the current count has changed, update the element
        if (parseInt(el.innerHTML, 10) !== currentCount) {
            el.innerHTML = currentCount;
        }

        // If we’ve reached our last frame, stop the animation
        if (frame === totalFrames) {
            clearInterval(counter);
        }
    }, frameDuration);
};

// Observe when elements are in the viewport and animate them
const runAnimations = (entries, observer) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            animateCountUp(entry.target);
            observer.unobserve(entry.target); // Unobserve to prevent reanimation
        }
    });
};

// Use IntersectionObserver for better performance
const initCounterObserver = () => {
    const observer = new IntersectionObserver(runAnimations, {
        threshold: 0.1 // Trigger when 10% of the element is visible
    });

    const countupEls = document.querySelectorAll('.counter');
    countupEls.forEach((el) => {
        observer.observe(el);
    });
};

// Initialize observer when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    initCounterObserver();
});
