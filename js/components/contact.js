import { href, imageTag, list, text } from "../utils/dom.js";
import { icon } from "./icons.js";

export function renderContact(content) {
  const contact = content.contact || {};
  const form = contact.form || {};
  const formLink = form.externalUrl || "";

  return `
    <div class="container contact-layout">
      <div>
        <div class="section-heading" data-reveal>
          ${contact.eyebrow ? `<p class="eyebrow">${text(contact.eyebrow)}</p>` : ""}
          <h2 class="section-title">${text(contact.title || "")}</h2>
          ${contact.summary ? `<p class="section-copy">${text(contact.summary)}</p>` : ""}
        </div>

        <div class="contact-methods">
          ${list(contact.methods, (method) => `
            <a class="contact-method" href="${href(method.href)}" data-reveal>
              <span class="contact-icon">${icon(method.icon || "phone")}</span>
              <span>
                <strong>${text(method.label)}</strong>
                <span>${text(method.value)}</span>
              </span>
            </a>
          `)}
        </div>
      </div>

      <aside class="contact-form">
        <div>
          <p class="doctor-kicker">${text(form.kicker || "")}</p>
          <h3 style="margin: 0; font-size: 1.45rem; line-height: 1.15;">${text(form.title || "")}</h3>
          ${form.note ? `<p class="form-note" style="margin-top: 0.65rem;">${text(form.note)}</p>` : ""}
        </div>
        <a class="button button-primary appointment-form-button" href="${href(formLink)}" target="_blank" rel="noopener noreferrer">
          ${text(form.submitLabel || "Open Form")}
          ${icon("arrowRight")}
        </a>
      </aside>

      <div class="branch-grid" style="grid-column: 1 / -1;">
        ${list(contact.branches, (branch) => `
          <article class="card branch-card" data-reveal>
            ${imageTag(branch.image, "", "lazy")}
            <h3>${text(branch.name)}</h3>
            <p class="branch-meta">${text(branch.address)}</p>
            <ul class="contact-list">
              <li>${icon("clock")}<span>${text(branch.hours)}</span></li>
              <li>${icon("phone")}<span>${text(branch.phone)}</span></li>
            </ul>
          </article>
        `)}
      </div>
    </div>
  `;
}
