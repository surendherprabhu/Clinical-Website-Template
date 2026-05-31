# Clinical Website Template

A production-ready healthcare website template built with HTML, CSS, vanilla JavaScript, and a Python-generated JSON data source.

## Architecture

```text
project/
├── index.html
├── assets/
│   └── images/
├── styles/
│   ├── globals.css
│   ├── components.css
│   └── responsive.css
├── js/
│   ├── app.js
│   ├── renderer.js
│   ├── animations.js
│   ├── utils/
│   │   └── dom.js
│   └── components/
├── data/
│   └── clinic-data.json
└── python/
    └── config.py
```

## Data Flow

1. Edit `python/config.py`.
2. Export the active clinic profile:

```powershell
py python/config.py --clinic template --out data/clinic-data.json
```

3. Serve the project over HTTP so the browser can fetch JSON:

```powershell
py -m http.server 8000
```

Or use the included dependency-free Node preview helper:

```powershell
node tools/static-server.mjs 8000
```

4. Open `http://localhost:8000`.

## Appointment Form

The appointment buttons link to a Google Form. Google Forms can save responses directly into Google Sheets, so the website stays static-hosting friendly.

Setup:

1. Create a Google Form with the appointment fields.
2. In Google Forms, open `Responses` and link it to a Google Sheet.
3. Copy the Google Form share URL.
4. Replace `https://forms.gle/REPLACE_WITH_YOUR_GOOGLE_FORM_LINK` in `python/config.py`.
5. Replace `https://forms.gle/REPLACE_WITH_ALIGNER_CAMP_FORM_LINK` if you are using the aligner camp top-bar button.
6. Export the config again to update `data/clinic-data.json`.

## Scaling Notes

- Add clinics by registering additional entries in `clinic_profiles`.
- Add languages by adding locale keys under `locales` and opening the site with `?lang=<code>`.
- Connect appointments by replacing the Google Form URL in `contact.form.externalUrl`.
- Replace image paths, colors, navigation, services, doctors, branches, testimonials, FAQ, and footer content from configuration only.
