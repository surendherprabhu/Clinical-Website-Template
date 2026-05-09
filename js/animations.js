export function initAnimations() {
  const revealItems = document.querySelectorAll("[data-reveal]");

  if (!("IntersectionObserver" in window)) {
    revealItems.forEach((item) => item.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.14,
      rootMargin: "0px 0px -8% 0px",
    },
  );

  revealItems.forEach((item) => {
    const bounds = item.getBoundingClientRect();
    const isInitiallyVisible = bounds.top < window.innerHeight * 0.96 && bounds.bottom > 0;

    if (isInitiallyVisible) {
      item.classList.add("is-visible");
      return;
    }

    observer.observe(item);
  });
}
