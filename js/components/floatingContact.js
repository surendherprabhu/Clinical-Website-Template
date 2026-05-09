import { attr, href, text } from "../utils/dom.js";
import { icon } from "./icons.js";

export function renderFloatingContact(content) {
  const floating = content.floatingContact || {};

  if (!floating.label || !floating.href) {
    return "";
  }

  return `
    <a class="floating-contact" href="${href(floating.href)}" aria-label="${attr(floating.ariaLabel || floating.label)}" data-floating-contact>
      ${icon(floating.icon || "message")}
      <span>${text(floating.label)}</span>
    </a>
  `;
}
