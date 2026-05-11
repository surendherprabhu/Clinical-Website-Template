import { renderAppointment } from "./components/cta.js";
import { renderAbout } from "./components/about.js";
import { renderContact } from "./components/contact.js";
import { renderDoctors } from "./components/doctors.js";
import { renderFaq } from "./components/faq.js";
import { renderFloatingContact } from "./components/floatingContact.js";
import { renderFooter } from "./components/footer.js";
import { renderHero } from "./components/hero.js";
import { renderNavbar } from "./components/navbar.js";
import { renderServices } from "./components/services.js";
import { renderTestimonials } from "./components/testimonials.js";
import { getSection, safeUrl, setMeta, setPropertyMeta } from "./utils/dom.js";

const SECTION_RENDERERS = {
  navbar: renderNavbar,
  hero: renderHero,
  services: renderServices,
  about: renderAbout,
  doctors: renderDoctors,
  testimonials: renderTestimonials,
  faq: renderFaq,
  contact: renderContact,
  appointment: renderAppointment,
  footer: renderFooter,
  "floating-contact": renderFloatingContact,
};

export async function fetchClinicData(url) {
  const response = await fetch(url, {
    headers: { Accept: "application/json" },
    cache: "no-cache",
  });

  if (!response.ok) {
    throw new Error(`Data request failed with status ${response.status}`);
  }

  return response.json();
}

export function resolveClinicContent(data) {
  const params = new URLSearchParams(window.location.search);
  const locale = params.get("lang") || data.defaultLocale;
  const content = data.locales?.[locale] || data.locales?.[data.defaultLocale];

  if (!content) {
    throw new Error("No locale content was found in the clinic data.");
  }

  return {
    data,
    locale,
    content,
  };
}

export function renderSite(state) {
  const { content, locale } = state;

  document.documentElement.lang = locale || "en";
  document.documentElement.dir = content.site?.direction || "ltr";

  applyTheme(content.branding?.theme || {});
  applySeo(content);

  Object.entries(SECTION_RENDERERS).forEach(([name, renderer]) => {
    const target = getSection(name);
    if (target) {
      target.innerHTML = renderer(content);
    }
  });

  renderStructuredData(content);
}

function applyTheme(theme) {
  const root = document.documentElement;
  const cssVars = {
    primary: "--color-primary",
    primaryDark: "--color-primary-dark",
    secondary: "--color-secondary",
    accent: "--color-accent",
    ink: "--color-ink",
    muted: "--color-muted",
    soft: "--color-soft",
    surface: "--color-surface",
    surfaceAlt: "--color-surface-alt",
    border: "--color-border",
  };

  Object.entries(cssVars).forEach(([key, variable]) => {
    if (theme[key]) {
      root.style.setProperty(variable, theme[key]);
    }
  });
}

function applySeo(content) {
  const seo = content.seo || {};

  if (seo.title) {
    document.title = seo.title;
  }

  setMeta("description", seo.description);
  setMeta("theme-color", content.branding?.theme?.primary);
  setPropertyMeta("og:title", seo.title);
  setPropertyMeta("og:description", seo.description);
  setPropertyMeta("og:image", seo.image ? new URL(safeUrl(seo.image), window.location.href).href : "");
  setPropertyMeta("og:url", seo.canonical || window.location.href);

  if (seo.canonical) {
    let canonical = document.querySelector('link[rel="canonical"]');
    if (!canonical) {
      canonical = document.createElement("link");
      canonical.setAttribute("rel", "canonical");
      document.head.append(canonical);
    }
    canonical.setAttribute("href", safeUrl(seo.canonical));
  }
}

function renderStructuredData(content) {
  const contact = content.contact || {};
  const structured = {
    "@context": "https://schema.org",
    "@type": "MedicalClinic",
    name: content.branding?.name,
    description: content.seo?.description,
    image: content.seo?.image ? new URL(safeUrl(content.seo.image), window.location.href).href : undefined,
    telephone: contact.schema?.telephone,
    email: contact.schema?.email,
    address: contact.schema?.address,
    medicalSpecialty: content.services?.items?.map((service) => service.title),
    url: content.seo?.canonical || window.location.href,
  };

  let script = document.querySelector("#structured-data");
  if (!script) {
    script = document.createElement("script");
    script.id = "structured-data";
    script.type = "application/ld+json";
    document.head.append(script);
  }

  script.textContent = JSON.stringify(removeEmpty(structured));
}

function removeEmpty(value) {
  if (Array.isArray(value)) {
    return value.map(removeEmpty).filter(Boolean);
  }

  if (value && typeof value === "object") {
    return Object.fromEntries(
      Object.entries(value)
        .map(([key, child]) => [key, removeEmpty(child)])
        .filter(([, child]) => child !== undefined && child !== "" && child !== null),
    );
  }

  return value;
}
