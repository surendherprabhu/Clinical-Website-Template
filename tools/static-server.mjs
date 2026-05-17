import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { randomUUID } from "node:crypto";
import { once } from "node:events";
import tls from "node:tls";
import path from "node:path";

const root = process.cwd();
const port = Number(process.argv[2] || 8000);

const mimeTypes = new Map([
  [".html", "text/html; charset=utf-8"],
  [".css", "text/css; charset=utf-8"],
  [".js", "text/javascript; charset=utf-8"],
  [".json", "application/json; charset=utf-8"],
  [".png", "image/png"],
  [".jpg", "image/jpeg"],
  [".jpeg", "image/jpeg"],
  [".webp", "image/webp"],
  [".svg", "image/svg+xml"],
]);

const appointmentRecipient = process.env.APPOINTMENT_TO_EMAIL || "surendherprabhu@gmail.com";
const smtpUser = process.env.GMAIL_USER || "";
const smtpPassword = process.env.GMAIL_APP_PASSWORD || "";

function resolveRequestPath(url = "/") {
  const requestUrl = new URL(url, `http://localhost:${port}`);
  const pathname = decodeURIComponent(requestUrl.pathname);
  const requested = pathname === "/" ? "/index.html" : pathname;
  const normalized = path.normalize(requested).replace(/^[/\\]+/, "");
  const filePath = path.join(root, normalized);

  if (!filePath.startsWith(root)) {
    return null;
  }

  return filePath;
}

function sendJson(response, status, payload) {
  response.writeHead(status, { "Content-Type": "application/json; charset=utf-8" });
  response.end(JSON.stringify(payload));
}

async function readJsonBody(request) {
  const chunks = [];
  let size = 0;

  for await (const chunk of request) {
    size += chunk.length;
    if (size > 64 * 1024) {
      throw new Error("Request body is too large.");
    }
    chunks.push(chunk);
  }

  if (chunks.length === 0) {
    return {};
  }

  return JSON.parse(Buffer.concat(chunks).toString("utf8"));
}

function clean(value = "") {
  return String(value || "").trim();
}

function formatAppointmentEmail(payload) {
  const fields = [
    ["Name", clean(payload.name)],
    ["Phone", clean(payload.phone)],
    ["Service", clean(payload.service)],
    ["Preferred date", clean(payload.date)],
    ["Message", clean(payload.message)],
    ["Source", clean(payload.source)],
  ];

  return fields
    .filter(([, value]) => value)
    .map(([label, value]) => `${label}: ${value}`)
    .join("\n");
}

function escapeHtml(value = "") {
  return String(value).replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    "\"": "&quot;",
    "'": "&#39;",
  })[char]);
}

function buildMimeMessage({ from, to, subject, text }) {
  const boundary = `oracare-${randomUUID()}`;
  const htmlRows = text
    .split("\n")
    .map((line) => {
      const [label, ...rest] = line.split(":");
      return `<tr><th align="left" style="padding:8px;border:1px solid #dce9e8;">${escapeHtml(label)}</th><td style="padding:8px;border:1px solid #dce9e8;">${escapeHtml(rest.join(":").trim())}</td></tr>`;
    })
    .join("");

  const html = `
    <h2>New OraCare appointment request</h2>
    <table style="border-collapse:collapse;font-family:Arial,sans-serif;font-size:14px;">${htmlRows}</table>
  `;

  return [
    `From: OraCare Website <${from}>`,
    `To: ${to}`,
    `Subject: ${subject}`,
    "MIME-Version: 1.0",
    `Content-Type: multipart/alternative; boundary="${boundary}"`,
    "",
    `--${boundary}`,
    "Content-Type: text/plain; charset=utf-8",
    "Content-Transfer-Encoding: 8bit",
    "",
    text,
    "",
    `--${boundary}`,
    "Content-Type: text/html; charset=utf-8",
    "Content-Transfer-Encoding: 8bit",
    "",
    html,
    "",
    `--${boundary}--`,
    "",
  ].join("\r\n");
}

async function sendSmtpCommand(socket, command, expectedStatus) {
  if (command) {
    socket.write(`${command}\r\n`);
  }

  let responseText = "";
  while (true) {
    const [chunk] = await once(socket, "data");
    responseText += chunk.toString("utf8");

    const lines = responseText.trimEnd().split(/\r?\n/);
    const lastLine = lines.at(-1) || "";
    if (/^\d{3} /.test(lastLine)) {
      break;
    }
  }

  if (!responseText.startsWith(String(expectedStatus))) {
    throw new Error(`SMTP command failed: ${responseText.trim()}`);
  }

  return responseText;
}

async function sendAppointmentEmail(payload) {
  if (!smtpUser || !smtpPassword) {
    throw new Error("GMAIL_USER and GMAIL_APP_PASSWORD are required to send appointment email.");
  }

  const message = buildMimeMessage({
    from: smtpUser,
    to: appointmentRecipient,
    subject: "New OraCare appointment request",
    text: formatAppointmentEmail(payload),
  });

  const socket = tls.connect({
    host: "smtp.gmail.com",
    port: 465,
    servername: "smtp.gmail.com",
  });

  await once(socket, "secureConnect");

  try {
    await sendSmtpCommand(socket, "", 220);
    await sendSmtpCommand(socket, "EHLO oracare.local", 250);
    await sendSmtpCommand(socket, "AUTH LOGIN", 334);
    await sendSmtpCommand(socket, Buffer.from(smtpUser).toString("base64"), 334);
    await sendSmtpCommand(socket, Buffer.from(smtpPassword).toString("base64"), 235);
    await sendSmtpCommand(socket, `MAIL FROM:<${smtpUser}>`, 250);
    await sendSmtpCommand(socket, `RCPT TO:<${appointmentRecipient}>`, 250);
    await sendSmtpCommand(socket, "DATA", 354);
    await sendSmtpCommand(socket, `${message}\r\n.`, 250);
    await sendSmtpCommand(socket, "QUIT", 221);
  } finally {
    socket.end();
  }
}

async function handleAppointmentRequest(request, response) {
  if (request.method !== "POST") {
    response.writeHead(405, { Allow: "POST" });
    response.end("Method Not Allowed");
    return;
  }

  try {
    const payload = await readJsonBody(request);

    if (clean(payload._honey)) {
      sendJson(response, 200, { ok: true });
      return;
    }

    if (!clean(payload.name) || !clean(payload.phone) || !clean(payload.service)) {
      sendJson(response, 400, { ok: false, message: "Name, phone, and service are required." });
      return;
    }

    await sendAppointmentEmail(payload);
    sendJson(response, 200, { ok: true });
  } catch (error) {
    console.error(error);
    sendJson(response, 500, { ok: false, message: "Appointment request could not be sent." });
  }
}

const server = createServer(async (request, response) => {
  const requestUrl = new URL(request.url || "/", `http://localhost:${port}`);

  if (requestUrl.pathname === "/api/appointment") {
    await handleAppointmentRequest(request, response);
    return;
  }

  const filePath = resolveRequestPath(request.url);

  if (!filePath) {
    response.writeHead(403, { "Content-Type": "text/plain; charset=utf-8" });
    response.end("Forbidden");
    return;
  }

  try {
    const body = await readFile(filePath);
    const type = mimeTypes.get(path.extname(filePath).toLowerCase()) || "application/octet-stream";
    response.writeHead(200, { "Content-Type": type });
    response.end(body);
  } catch {
    response.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
    response.end("Not found");
  }
});

server.listen(port, "0.0.0.0", () => {
  console.log(`Serving ${root} at http://localhost:${port}`);
});
