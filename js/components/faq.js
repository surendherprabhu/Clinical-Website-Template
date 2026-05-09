import { attr, list, text } from "../utils/dom.js";
import { icon } from "./icons.js";

export function renderFaq(content) {
  const faq = content.faq || {};

  return `
    <div class="container">
      <div class="section-heading centered" data-reveal>
        ${faq.eyebrow ? `<p class="eyebrow">${text(faq.eyebrow)}</p>` : ""}
        <h2 class="section-title">${text(faq.title || "")}</h2>
        ${faq.summary ? `<p class="section-copy">${text(faq.summary)}</p>` : ""}
      </div>

      <div class="faq-list" data-faq-list>
        ${list(faq.items, (item, index) => {
          const panelId = `faq-panel-${index}`;
          const buttonId = `faq-button-${index}`;
          return `
            <article class="faq-item" data-faq-item data-reveal>
              <button
                id="${attr(buttonId)}"
                class="faq-question"
                type="button"
                aria-expanded="false"
                aria-controls="${attr(panelId)}"
                data-faq-button
              >
                <span>${text(item.question)}</span>
                ${icon("plus")}
              </button>
              <div id="${attr(panelId)}" class="faq-answer" role="region" aria-labelledby="${attr(buttonId)}">
                <div class="faq-answer-inner">
                  <p>${text(item.answer)}</p>
                </div>
              </div>
            </article>
          `;
        })}
      </div>
    </div>
  `;
}
