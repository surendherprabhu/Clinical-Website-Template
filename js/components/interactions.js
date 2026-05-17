export function initNavbar() {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector("[data-nav-toggle]");
  const menu = document.querySelector("[data-nav-menu]");
  const links = document.querySelectorAll("[data-nav-link]");

  if (!header || !toggle || !menu) {
    return;
  }

  const setOpen = (open) => {
    document.body.classList.toggle("is-nav-open", open);
    toggle.setAttribute("aria-expanded", String(open));
  };

  toggle.addEventListener("click", () => {
    setOpen(!document.body.classList.contains("is-nav-open"));
  });

  links.forEach((link) => {
    link.addEventListener("click", () => setOpen(false));
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      setOpen(false);
    }
  });

  const updateHeader = () => {
    header.classList.toggle("is-scrolled", window.scrollY > 8);
  };

  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });
}

export function initSmoothScroll() {
  document.addEventListener("click", (event) => {
    const anchor = event.target.closest('a[href^="#"]');
    if (!anchor) {
      return;
    }

    const target = document.querySelector(anchor.getAttribute("href"));
    if (!target) {
      return;
    }

    event.preventDefault();
    target.scrollIntoView({ behavior: "smooth", block: "start" });
    target.focus({ preventScroll: true });
  });
}

export function initFaq() {
  document.querySelectorAll("[data-faq-item]").forEach((item) => {
    const button = item.querySelector("[data-faq-button]");
    if (!button) {
      return;
    }

    button.addEventListener("click", () => {
      const open = item.classList.toggle("is-open");
      button.setAttribute("aria-expanded", String(open));
    });
  });
}

export function initCarousel() {
  document.querySelectorAll("[data-carousel]").forEach((carousel) => {
    const track = carousel.querySelector("[data-carousel-track]");
    const slides = Array.from(carousel.querySelectorAll("[data-carousel-slide]"));
    const dots = carousel.querySelector("[data-carousel-dots]");
    const previous = carousel.querySelector("[data-carousel-prev]");
    const next = carousel.querySelector("[data-carousel-next]");
    let index = 0;

    if (!track || slides.length === 0 || !dots || !previous || !next) {
      return;
    }

    dots.innerHTML = slides
      .map((_, dotIndex) => `<button class="carousel-dot" type="button" data-carousel-dot="${dotIndex}" aria-label="${dotIndex + 1}"></button>`)
      .join("");

    const dotButtons = Array.from(dots.querySelectorAll("[data-carousel-dot]"));

    const update = () => {
      track.style.transform = `translateX(${-100 * index}%)`;
      dotButtons.forEach((dot, dotIndex) => {
        dot.classList.toggle("is-active", dotIndex === index);
        dot.setAttribute("aria-current", dotIndex === index ? "true" : "false");
      });
    };

    const move = (direction) => {
      index = (index + direction + slides.length) % slides.length;
      update();
    };

    previous.addEventListener("click", () => move(-1));
    next.addEventListener("click", () => move(1));
    dotButtons.forEach((dot) => {
      dot.addEventListener("click", () => {
        index = Number(dot.dataset.carouselDot);
        update();
      });
    });

    update();
  });
}

export function initAppointmentForms() {
  document.querySelectorAll("[data-appointment-form]").forEach((form) => {
    const response = form.querySelector("[data-form-response]");
    const submitButton = form.querySelector('button[type="submit"]');

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      if (response) {
        response.textContent = "";
      }

      if (!form.reportValidity()) {
        return;
      }

      const endpoint = form.dataset.endpoint;
      const success = form.dataset.successMessage;
      const error = form.dataset.errorMessage;
      const submitFormat = form.dataset.submitFormat || "json";

      if (submitButton) {
        submitButton.disabled = true;
        submitButton.setAttribute("aria-busy", "true");
      }

      try {
        if (endpoint) {
          const formData = new FormData(form);
          const request =
            submitFormat === "form-data"
              ? {
                  method: "POST",
                  headers: { Accept: "application/json" },
                  body: formData,
                }
              : {
                  method: "POST",
                  headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                  },
                  body: JSON.stringify(Object.fromEntries(formData.entries())),
                };

          const result = await fetch(endpoint, request);
          if (!result.ok) {
            throw new Error(`Appointment request failed with status ${result.status}`);
          }
        }

        form.reset();
        if (response) {
          response.textContent = success;
          response.classList.remove("is-error");
        }
      } catch {
        if (response) {
          response.textContent = error;
          response.classList.add("is-error");
        }
      } finally {
        if (submitButton) {
          submitButton.disabled = false;
          submitButton.removeAttribute("aria-busy");
        }
      }
    });
  });
}

export function initFloatingContact() {
  const floating = document.querySelector("[data-floating-contact]");
  if (!floating) {
    return;
  }

  const update = () => {
    floating.classList.toggle("is-visible", window.scrollY > window.innerHeight * 0.35);
  };

  update();
  window.addEventListener("scroll", update, { passive: true });
}
