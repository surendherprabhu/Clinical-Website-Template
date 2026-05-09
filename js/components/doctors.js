import { href, imageTag, list, text } from "../utils/dom.js";
import { icon } from "./icons.js";

export function renderDoctors(content) {
  const doctors = content.doctors || {};
  const featuredDoctors = Array.isArray(doctors.featuredDoctors)
    ? doctors.featuredDoctors
    : doctors.featured
      ? [doctors.featured]
      : [];

  return `
    <div class="container doctors-layout">
      <div class="section-heading" data-reveal>
        ${doctors.eyebrow ? `<p class="eyebrow">${text(doctors.eyebrow)}</p>` : ""}
        <h2 class="section-title">${text(doctors.title || "")}</h2>
        ${doctors.summary ? `<p class="section-copy">${text(doctors.summary)}</p>` : ""}
      </div>

      <div class="featured-doctor-list">
        ${list(featuredDoctors, (featured) => `
          <article class="featured-doctor" data-reveal>
            <div class="featured-doctor-media">
              ${imageTag(featured.image, "", "lazy")}
            </div>
            <div class="featured-doctor-copy">
              ${featured.kicker ? `<p class="doctor-kicker">${text(featured.kicker)}</p>` : ""}
              <h3>${text(featured.name || "")}</h3>
              ${featured.role ? `<p class="doctor-role">${text(featured.role)}</p>` : ""}
              ${featured.bio ? `<p class="doctor-bio">${text(featured.bio)}</p>` : ""}
              <div class="doctor-stat-grid">
                ${list(featured.stats, (stat) => `
                  <div class="doctor-stat">
                    <span class="doctor-stat-icon">${icon(stat.icon || "spark")}</span>
                    <div>
                      <strong>${text(stat.value)}</strong>
                      <span>${text(stat.label)}</span>
                    </div>
                  </div>
                `)}
              </div>
              ${featured.cta?.label ? `
                <div class="button-row" style="margin-top: 1.4rem;">
                  <a class="button button-secondary" href="${href(featured.cta.href)}">
                    ${text(featured.cta.label)}
                    ${icon("arrowRight")}
                  </a>
                </div>
              ` : ""}
            </div>
          </article>
        `)}
      </div>

      <div class="doctor-grid">
        ${list(doctors.items, (doctor) => `
          <article class="card doctor-card" data-reveal>
            <h3>${text(doctor.name)}</h3>
            <p class="doctor-role">${text(doctor.role)}</p>
            <p>${text(doctor.bio)}</p>
            <ul>
              ${list(doctor.focusAreas, (area) => `
                <li>${icon("check")}<span>${text(area)}</span></li>
              `)}
            </ul>
          </article>
        `)}
      </div>
    </div>
  `;
}
