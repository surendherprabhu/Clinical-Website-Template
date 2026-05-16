import { attr, href, initials, list, text } from "../utils/dom.js";
import { icon } from "./icons.js";

export function renderTestimonials(content) {
  const testimonials = content.testimonials || {};
  const labels = testimonials.labels || {};
  const items = Array.isArray(testimonials.items) ? testimonials.items : [];
  const googleReviews = testimonials.googleReviews || {};

  return `
    <div class="container">
      <div class="section-heading centered" data-reveal>
        ${testimonials.eyebrow ? `<p class="eyebrow">${text(testimonials.eyebrow)}</p>` : ""}
        <h2 class="section-title">${text(testimonials.title || "")}</h2>
        ${testimonials.summary ? `<p class="section-copy">${text(testimonials.summary)}</p>` : ""}
      </div>

      ${items.length ? `
        <div class="testimonial-shell" data-carousel data-reveal>
          <div class="testimonial-viewport">
            <div class="testimonial-track" data-carousel-track>
              ${list(items, (item) => `
                <article class="testimonial-card" data-carousel-slide>
                  <div>
                    <span class="testimonial-rating">${text(item.ratingLabel || "")}</span>
                    <p class="testimonial-quote">${text(item.quote)}</p>
                  </div>
                  <footer class="testimonial-author">
                    <span class="testimonial-avatar" aria-hidden="true">${text(initials(item.name))}</span>
                    <div>
                      <strong>${text(item.name)}</strong>
                      <span>${text(item.context)}</span>
                    </div>
                  </footer>
                </article>
              `)}
            </div>
          </div>

          <div class="carousel-controls">
            <button class="carousel-button" type="button" data-carousel-prev aria-label="${attr(labels.previous || "")}">
              ${icon("chevronLeft")}
            </button>
            <div class="carousel-dots" data-carousel-dots aria-label="${attr(labels.pagination || "")}"></div>
            <button class="carousel-button" type="button" data-carousel-next aria-label="${attr(labels.next || "")}">
              ${icon("chevronRight")}
            </button>
          </div>
        </div>
      ` : ""}

      ${googleReviews.href ? `
        <div class="google-reviews-cta" data-reveal>
          <a class="button button-primary" href="${href(googleReviews.href)}" target="_blank" rel="noopener noreferrer">
            ${text(googleReviews.label || "View Google Reviews")}
            ${icon("arrowRight")}
          </a>
        </div>
      ` : ""}
    </div>
  `;
}
