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

## Appointment Email

The appointment form posts to `/api/appointment`. The included Node server sends those requests through Gmail SMTP to `surendherprabhu@gmail.com`.

Create a Gmail App Password for the sending Gmail account, then run the server with:

```bash
GMAIL_USER="surendherprabhu@gmail.com" \
GMAIL_APP_PASSWORD="your-gmail-app-password" \
APPOINTMENT_TO_EMAIL="surendherprabhu@gmail.com" \
node tools/static-server.mjs 8000
```

The Gmail password must stay on the server as an environment variable. Do not put it in `python/config.py`, `data/clinic-data.json`, or frontend JavaScript.

## Scaling Notes

- Add clinics by registering additional entries in `clinic_profiles`.
- Add languages by adding locale keys under `locales` and opening the site with `?lang=<code>`.
- Connect the appointment form by setting `contact.form.endpoint` in the exported data.
- Replace image paths, colors, navigation, services, doctors, branches, testimonials, FAQ, and footer content from configuration only.
