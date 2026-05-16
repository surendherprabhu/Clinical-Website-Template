import { attr, href, imageTag, list, text } from "../utils/dom.js";
import { icon } from "./icons.js";

export function renderNavbar(content) {
  const { branding = {}, navigation = {} } = content;
  const labels = navigation.labels || {};
  const cta = navigation.cta || {};
  const brandMark = branding.logo?.src
    ? imageTag(branding.logo, "brand-mark-image", "eager")
    : text(branding.logoText || "");

  return `
    <div class="container navbar">
      <a class="brand" href="${href(navigation.homeHref || "#hero")}" aria-label="${attr(branding.name || "")}">
        <span class="brand-mark" aria-hidden="true">${brandMark}</span>
        <span class="brand-copy">
          <span class="brand-name">${text(branding.name || "")}</span>
          <span class="brand-tagline">${text(branding.tagline || "")}</span>
        </span>
      </a>

      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-menu" aria-label="${attr(labels.openMenu || "")}" data-nav-toggle>
        <span class="nav-toggle-lines" aria-hidden="true"></span>
      </button>

      <nav id="nav-menu" class="nav-menu" aria-label="${attr(navigation.ariaLabel || "")}" data-nav-menu>
        <ul class="nav-links">
          ${list(navigation.links, (item) => `
            <li>
              <a class="nav-link" href="${href(item.href)}" data-nav-link>${text(item.label)}</a>
            </li>
          `)}
        </ul>
        ${cta.label ? `
          <a class="button button-primary" href="${href(cta.href)}" data-nav-link>
            ${text(cta.label)}
            ${icon("arrowRight")}
          </a>
        ` : ""}
      </nav>
    </div>
  `;
}
