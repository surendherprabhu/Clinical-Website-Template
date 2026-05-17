import { attr, href, imageTag, list, text } from "../utils/dom.js";
import { icon } from "./icons.js";

const inputTypes = new Set(["email", "tel", "text", "date", "time"]);

function renderField(field = {}) {
  const required = field.required ? " required" : "";
  const id = `field-${field.name}`;
  const common = `
    id="${attr(id)}"
    name="${attr(field.name)}"
    ${field.placeholder ? `placeholder="${attr(field.placeholder)}"` : ""}
    ${required}
  `;

  if (field.type === "textarea") {
    return `
      <div class="field">
        <label for="${attr(id)}">${text(field.label)}</label>
        <textarea ${common}></textarea>
      </div>
    `;
  }

  if (field.type === "select") {
    return `
      <div class="field">
        <label for="${attr(id)}">${text(field.label)}</label>
        <select ${common}>
          ${list(field.options, (option) => `<option value="${attr(option.value)}">${text(option.label)}</option>`)}
        </select>
      </div>
    `;
  }

  const type = inputTypes.has(field.type) ? field.type : "text";
  return `
    <div class="field">
      <label for="${attr(id)}">${text(field.label)}</label>
      <input type="${attr(type)}" ${common}>
    </div>
  `;
}

function renderHiddenField(field = {}) {
  if (!field.name) {
    return "";
  }

  return `<input type="hidden" name="${attr(field.name)}" value="${attr(field.value || "")}">`;
}

export function renderContact(content) {
  const contact = content.contact || {};
  const form = contact.form || {};
  const honeypot = form.honeypot || {};

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

      <form class="contact-form" data-appointment-form data-success-message="${attr(form.successMessage || "")}" data-error-message="${attr(form.errorMessage || "")}" data-endpoint="${attr(form.endpoint || "")}" data-submit-format="${attr(form.submitFormat || "json")}" novalidate>
        <div>
          <p class="doctor-kicker">${text(form.kicker || "")}</p>
          <h3 style="margin: 0; font-size: 1.45rem; line-height: 1.15;">${text(form.title || "")}</h3>
          ${form.note ? `<p class="form-note" style="margin-top: 0.65rem;">${text(form.note)}</p>` : ""}
        </div>
        ${list(form.hiddenFields, renderHiddenField)}
        ${honeypot.name ? `
          <div class="field field-honeypot" aria-hidden="true">
            <label for="field-${attr(honeypot.name)}">${text(honeypot.label || "")}</label>
            <input id="field-${attr(honeypot.name)}" type="text" name="${attr(honeypot.name)}" tabindex="-1" autocomplete="off">
          </div>
        ` : ""}
        <div class="form-grid">
          ${list(form.fields, renderField)}
        </div>
        <button class="button button-primary" type="submit">
          ${text(form.submitLabel || "")}
          ${icon("calendar")}
        </button>
        <p class="form-response" data-form-response aria-live="polite"></p>
      </form>

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
