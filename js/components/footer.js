import { href, imageTag, list, text } from "../utils/dom.js";

export function renderFooter(content) {
  const { branding = {}, footer = {} } = content;
  const brandMark = branding.logo?.src
    ? imageTag(branding.logo, "brand-mark-image", "lazy")
    : text(branding.logoText || "");

  return `
    <div class="container footer-main">
      <div class="footer-grid">
        <div class="footer-brand">
          <a class="brand" href="#hero" aria-label="${text(branding.name || "")}">
            <span class="brand-mark" aria-hidden="true">${brandMark}</span>
            <span class="brand-copy">
              <span class="brand-name">${text(branding.name || "")}</span>
              <span class="brand-tagline">${text(branding.tagline || "")}</span>
            </span>
          </a>
          ${footer.summary ? `<p class="footer-copy">${text(footer.summary)}</p>` : ""}
        </div>

        ${list(footer.columns, (column) => `
          <div class="footer-column">
            <h3>${text(column.title)}</h3>
            <ul class="footer-list">
              ${list(column.links, (link) => `
                <li><a href="${href(link.href)}">${text(link.label)}</a></li>
              `)}
            </ul>
          </div>
        `)}
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container footer-bottom-inner">
        <span>${text(footer.copyright || "")}</span>
        <span>${text(footer.disclaimer || "")}</span>
      </div>
    </div>
  `;
}
