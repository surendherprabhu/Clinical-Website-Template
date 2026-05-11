import { list, text } from "../utils/dom.js";
import { icon } from "./icons.js";

export function renderAbout(content) {
  const about = content.about || {};

  return `
    <div class="container about-layout">
      <div class="section-heading" data-reveal>
        ${about.eyebrow ? `<p class="eyebrow">${text(about.eyebrow)}</p>` : ""}
        <h2 class="section-title">${text(about.title || "")}</h2>
        ${about.summary ? `<p class="section-copy">${text(about.summary)}</p>` : ""}
      </div>

      <div class="about-statement-grid">
        ${about.vision ? `
          <article class="card about-panel" data-reveal>
            <span class="service-icon">${icon("spark")}</span>
            <h3>${text(about.vision.title)}</h3>
            <p>${text(about.vision.body)}</p>
          </article>
        ` : ""}
        ${about.mission ? `
          <article class="card about-panel" data-reveal>
            <span class="service-icon">${icon("shield")}</span>
            <h3>${text(about.mission.title)}</h3>
            <p>${text(about.mission.body)}</p>
          </article>
        ` : ""}
      </div>

      <div>
        <div class="section-heading centered about-values-heading" data-reveal>
          <h3 class="section-title">${text(about.valuesTitle || "")}</h3>
          ${about.valuesSummary ? `<p class="section-copy">${text(about.valuesSummary)}</p>` : ""}
        </div>
        <div class="value-grid">
          ${list(about.values, (value) => `
            <article class="card value-card" data-reveal>
              <span class="service-icon">${icon(value.icon || "check")}</span>
              <h4>${text(value.title)}</h4>
              <p>${text(value.body)}</p>
            </article>
          `)}
        </div>
      </div>
    </div>
  `;
}
