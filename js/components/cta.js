import { href, list, text } from "../utils/dom.js";
import { icon } from "./icons.js";

export function renderAppointment(content) {
  const appointment = content.appointment || {};

  return `
    <div class="container">
      <article class="appointment-panel" data-reveal>
        <div class="appointment-inner">
          <div>
            <h2>${text(appointment.title || "")}</h2>
            ${appointment.summary ? `<p>${text(appointment.summary)}</p>` : ""}
          </div>
          <div class="button-row appointment-actions">
            ${list(appointment.actions, (action, index) => `
              <a class="button ${index === 0 ? "button-primary" : "button-secondary"}" href="${href(action.href)}">
                ${text(action.label)}
                ${icon(index === 0 ? "calendar" : "phone")}
              </a>
            `)}
          </div>
        </div>
      </article>
    </div>
  `;
}
