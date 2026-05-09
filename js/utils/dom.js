const HTML_ESCAPE_MAP = {
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  "\"": "&quot;",
  "'": "&#39;",
};

const SAFE_PROTOCOLS = new Set(["http:", "https:", "mailto:", "tel:", "sms:"]);

export function escapeHTML(value = "") {
  return String(value).replace(/[&<>"']/g, (char) => HTML_ESCAPE_MAP[char]);
}

export function escapeAttr(value = "") {
  return escapeHTML(value).replace(/`/g, "&#96;");
}

export function safeUrl(value = "#") {
  const url = String(value || "#").trim();

  if (
    url.startsWith("#") ||
    url.startsWith("/") ||
    url.startsWith("./") ||
    url.startsWith("../")
  ) {
    return url;
  }

  try {
    const parsed = new URL(url, window.location.href);
    return SAFE_PROTOCOLS.has(parsed.protocol) ? parsed.href : "#";
  } catch {
    return "#";
  }
}

export function text(value) {
  return escapeHTML(value);
}

export function attr(value) {
  return escapeAttr(value);
}

export function href(value) {
  return escapeAttr(safeUrl(value));
}

export function list(items, renderItem) {
  return Array.isArray(items) ? items.map(renderItem).join("") : "";
}

export function imageTag(image = {}, className = "", loading = "lazy") {
  if (!image.src) {
    return "";
  }

  const width = image.width ? ` width="${attr(image.width)}"` : "";
  const height = image.height ? ` height="${attr(image.height)}"` : "";
  const fetchPriority = loading === "eager" ? " fetchpriority=\"high\"" : "";

  return `
    <img
      class="${attr(className)}"
      src="${href(image.src)}"
      alt="${attr(image.alt || "")}"
      loading="${attr(loading)}"
      decoding="async"${width}${height}${fetchPriority}
    >
  `;
}

export function initials(value = "") {
  return String(value)
    .split(/\s+/)
    .filter(Boolean)
    .slice(0, 2)
    .map((part) => part[0])
    .join("")
    .toUpperCase();
}

export function setMeta(name, content) {
  if (!content) {
    return;
  }

  let tag = document.querySelector(`meta[name="${CSS.escape(name)}"]`);
  if (!tag) {
    tag = document.createElement("meta");
    tag.setAttribute("name", name);
    document.head.append(tag);
  }
  tag.setAttribute("content", content);
}

export function setPropertyMeta(property, content) {
  if (!content) {
    return;
  }

  let tag = document.querySelector(`meta[property="${CSS.escape(property)}"]`);
  if (!tag) {
    tag = document.createElement("meta");
    tag.setAttribute("property", property);
    document.head.append(tag);
  }
  tag.setAttribute("content", content);
}

export function getSection(id) {
  return document.querySelector(`[data-render="${id}"]`);
}
