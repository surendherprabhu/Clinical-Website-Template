import { list, text } from "../utils/dom.js";
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
            <span class="service-icon">${icon(item.icon || "stethoscope")}</span>
            <h3>${text(item.title)}</h3>
            <p>${text(item.description)}</p>
            <ul>
              ${list(item.highlights, (highlight) => `
                <li>${icon("check")}<span>${text(highlight)}</span></li>
              `)}
            </ul>
          </article>
        `)}
      </div>
    </div>
  `;
}
