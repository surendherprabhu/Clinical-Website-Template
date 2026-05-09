import { initAnimations } from "./animations.js";
import {
  initAppointmentForms,
  initCarousel,
  initFaq,
  initFloatingContact,
  initNavbar,
  initSmoothScroll,
} from "./components/interactions.js";
import { fetchClinicData, renderSite, resolveClinicContent } from "./renderer.js";

const DATA_URL = "./data/clinic-data.json";

async function boot() {
  try {
    const data = await fetchClinicData(DATA_URL);
    const state = resolveClinicContent(data);

    renderSite(state);
    initSmoothScroll();
    initNavbar();
    initFaq();
    initCarousel();
    initAppointmentForms();
    initFloatingContact();
    initAnimations();

    document.body.classList.add("is-ready");
  } catch (error) {
    renderDataError(error);
    console.error(error);
  }
}

function renderDataError(error) {
  document.body.innerHTML = `
    <main class="data-error">
      <h1>Configuration could not be loaded</h1>
      <p>${error.message}</p>
      <p>Serve the project over HTTP and confirm that data/clinic-data.json exists.</p>
    </main>
  `;
}

document.addEventListener("DOMContentLoaded", boot);
