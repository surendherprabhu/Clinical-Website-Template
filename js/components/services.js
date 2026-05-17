import { attr, imageTag, list, text } from "../utils/dom.js";
import { icon } from "./icons.js";

export function renderServices(content) {
  const services = content.services || {};

  return `
    <div class="container">
      <div class="section-heading centered" data-reveal>
        ${services.eyebrow ? `<p class="eyebrow">${text(services.eyebrow)}</p>` : ""}
        <h2 class="section-title">${text(services.title || "")}</h2>
        ${services.summary ? `<p class="section-copy">${text(services.summary)}</p>` : ""}
      </div>

      <div class="service-grid">
        ${list(services.items, (item) => `
          <article class="card service-card" data-reveal>
            <h3>${text(item.title)}</h3>
            <div class="service-card-media">
              ${item.image?.src
                ? imageTag(item.image, "service-image", "lazy")
                : `<span class="service-image-placeholder" aria-label="${attr(item.title)} image placeholder">${icon("image")}</span>`}
            </div>
          </article>
        `)}
      </div>
    </div>
  `;
}
