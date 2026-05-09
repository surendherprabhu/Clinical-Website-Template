import { href, imageTag, list, text } from "../utils/dom.js";
import { icon } from "./icons.js";

export function renderHero(content) {
  const { hero = {} } = content;

  return `
    <div class="container hero-layout">
      <div class="hero-copy" data-reveal>
        ${hero.eyebrow ? `<p class="eyebrow">${text(hero.eyebrow)}</p>` : ""}
        <h1 id="hero-title" class="hero-title">${text(hero.title || "")}</h1>
        ${hero.summary ? `<p class="hero-text">${text(hero.summary)}</p>` : ""}
        <div class="button-row hero-actions">
          ${list(hero.actions, (action, index) => `
            <a class="button ${index === 0 ? "button-primary" : "button-secondary"}" href="${href(action.href)}">
              ${text(action.label)}
              ${icon(index === 0 ? "calendar" : "arrowRight")}
            </a>
          `)}
        </div>
        <div class="trust-strip">
          ${list(hero.trustItems, (item) => `
            <article class="trust-item" data-reveal>
              <span class="trust-icon">${icon(item.icon || "shield")}</span>
              <div>
                <strong>${text(item.value)}</strong>
                <span>${text(item.label)}</span>
              </div>
            </article>
          `)}
        </div>
      </div>

      <div class="hero-visual" data-reveal>
        <div class="hero-image-shell">
          ${imageTag(hero.image, "hero-image", "eager")}
          ${hero.imageNote ? `
            <aside class="hero-note">
              <strong>${text(hero.imageNote.title)}</strong>
              <span>${text(hero.imageNote.body)}</span>
            </aside>
          ` : ""}
        </div>
      </div>
    </div>
  `;
}
