from __future__ import annotations

import argparse
import json
from copy import deepcopy
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "clinic-data.json"


clinic_data: dict[str, Any] = {
    "schemaVersion": "1.0.0",
    "clinicId": "template",
    "defaultLocale": "en",
    "availableLocales": [
        {"code": "en", "label": "English"},
    ],
    "locales": {
        "en": {
            "site": {
                "direction": "ltr",
            },
            "seo": {
                "title": "Configurable Healthcare Website Template",
                "description": "A modern clinic website template rendered from Python-generated JSON content.",
                "canonical": "./",
                "image": "./assets/images/hero-care-suite.png",
            },
            "branding": {
                "name": "Your Clinic Name",
                "tagline": "Patient-centered care",
                "logoText": "YC",
                "theme": {
                    "primary": "#1f7a7a",
                    "primaryDark": "#155e63",
                    "secondary": "#3566c4",
                    "accent": "#d98f5f",
                    "ink": "#163139",
                    "muted": "#62757c",
                    "soft": "#eff8f7",
                    "surface": "#ffffff",
                    "surfaceAlt": "#f7fbfb",
                    "border": "#dce9e8",
                },
            },
            "navigation": {
                "homeHref": "#hero",
                "ariaLabel": "Primary navigation",
                "labels": {
                    "openMenu": "Open navigation menu",
                },
                "links": [
                    {"label": "Services", "href": "#services"},
                    {"label": "Doctors", "href": "#doctors"},
                    {"label": "Reviews", "href": "#testimonials"},
                    {"label": "FAQ", "href": "#faq"},
                    {"label": "Contact", "href": "#contact"},
                ],
                "cta": {
                    "label": "Book Appointment",
                    "href": "#appointment",
                },
            },
            "hero": {
                "eyebrow": "Reusable clinic website system",
                "title": "Modern care experiences, powered by your data",
                "summary": "A calm, high-trust template for clinics, doctors, multi-branch practices, and future CMS-backed healthcare websites.",
                "actions": [
                    {"label": "Request Appointment", "href": "#contact"},
                    {"label": "Explore Services", "href": "#services"},
                ],
                "image": {
                    "src": "./assets/images/hero-care-suite.png",
                    "alt": "Bright generic clinic consultation space",
                    "width": 1400,
                    "height": 1000,
                },
                "imageNote": {
                    "title": "Flexible by design",
                    "body": "Swap clinic profiles, branches, services, and colors from JSON without editing layout code.",
                },
                "trustItems": [
                    {
                        "icon": "shield",
                        "value": "Data-driven",
                        "label": "Every visible business detail comes from configuration.",
                    },
                    {
                        "icon": "mapPin",
                        "value": "Branch-ready",
                        "label": "Add locations and contact paths as structured data.",
                    },
                    {
                        "icon": "spark",
                        "value": "CMS-ready",
                        "label": "Prepared for API and multilingual content flows.",
                    },
                ],
            },
            "services": {
                "eyebrow": "Services",
                "title": "Configurable sections for everyday care",
                "summary": "Use this service grid for specialties, treatments, programs, diagnostics, or any reusable offering your clinic needs.",
                "items": [
                    {
                        "icon": "stethoscope",
                        "title": "Primary Care",
                        "description": "General consultations, preventive care, and ongoing health support for routine visits.",
                        "highlights": ["Consultation workflows", "Preventive checkups", "Care plan support"],
                    },
                    {
                        "icon": "calendar",
                        "title": "Scheduled Clinics",
                        "description": "Template-ready blocks for specialty days, follow-up programs, and recurring clinic schedules.",
                        "highlights": ["Flexible time slots", "Multiple providers", "Branch-specific availability"],
                    },
                    {
                        "icon": "shield",
                        "title": "Diagnostics",
                        "description": "Present lab services, screenings, imaging partnerships, or pre-visit preparation clearly.",
                        "highlights": ["Screening lists", "Preparation guidance", "Referral-ready content"],
                    },
                    {
                        "icon": "user",
                        "title": "Specialist Care",
                        "description": "Reusable doctor cards support consultants, visiting specialists, and care team profiles.",
                        "highlights": ["Doctor directories", "Focus areas", "Profile CTAs"],
                    },
                    {
                        "icon": "message",
                        "title": "Patient Support",
                        "description": "Help patients find contact options, appointment channels, branch details, and common answers.",
                        "highlights": ["WhatsApp-ready CTA", "FAQ accordion", "Contact routing"],
                    },
                    {
                        "icon": "spark",
                        "title": "Wellness Programs",
                        "description": "Add packages, long-term care journeys, health checks, or membership-style programs.",
                        "highlights": ["Program cards", "Outcome-focused copy", "Reusable content models"],
                    },
                ],
            },
            "doctors": {
                "eyebrow": "Care team",
                "title": "Doctor profiles built for clinics of any size",
                "summary": "Highlight a lead clinician, then scale into a team directory with consistent, reusable profile cards.",
                "featured": {
                    "kicker": "Featured clinician",
                    "name": "Doctor Name",
                    "role": "Specialty or clinical role",
                    "bio": "Use this space for a concise, trust-building introduction focused on experience, care philosophy, and patient communication style.",
                    "image": {
                        "src": "./assets/images/doctor-placeholder.png",
                        "alt": "Generic clinician portrait placeholder",
                        "width": 900,
                        "height": 1100,
                    },
                    "stats": [
                        {"icon": "calendar", "value": "Flexible hours", "label": "Show provider availability"},
                        {"icon": "shield", "value": "Care focus", "label": "List credentials and specialties"},
                    ],
                    "cta": {
                        "label": "View Appointment Options",
                        "href": "#contact",
                    },
                },
                "items": [
                    {
                        "name": "Clinician Profile",
                        "role": "Care team role",
                        "bio": "Short profile cards can represent full-time doctors, visiting consultants, or allied health providers.",
                        "focusAreas": ["Specialty focus", "Patient group", "Consultation type"],
                    },
                    {
                        "name": "Consultant Profile",
                        "role": "Specialist role",
                        "bio": "Each card uses the same schema, making it simple to connect to a CMS or provider API later.",
                        "focusAreas": ["Branch availability", "Referral support", "Follow-up care"],
                    },
                    {
                        "name": "Provider Profile",
                        "role": "Clinical service role",
                        "bio": "Add or remove profiles from the Python data source without changing the frontend components.",
                        "focusAreas": ["Program support", "Preventive care", "Patient education"],
                    },
                ],
            },
            "testimonials": {
                "eyebrow": "Patient feedback",
                "title": "A calm carousel for trust signals",
                "summary": "Use verified quotes, care journey summaries, or patient experience highlights from your CMS.",
                "labels": {
                    "previous": "Show previous testimonial",
                    "next": "Show next testimonial",
                    "pagination": "Testimonial pagination",
                },
                "items": [
                    {
                        "ratingLabel": "5.0 patient rating",
                        "quote": "The appointment flow was clear, the visit felt organized, and every step was easy to understand.",
                        "name": "Patient A",
                        "context": "Verified visit",
                    },
                    {
                        "ratingLabel": "5.0 patient rating",
                        "quote": "The team explained options with patience and made follow-up instructions simple to keep track of.",
                        "name": "Patient B",
                        "context": "Follow-up care",
                    },
                    {
                        "ratingLabel": "5.0 patient rating",
                        "quote": "Branch information, timings, and contact details were easy to find before booking the visit.",
                        "name": "Patient C",
                        "context": "New appointment",
                    },
                ],
            },
            "faq": {
                "eyebrow": "Questions",
                "title": "FAQ content that can grow with the practice",
                "summary": "Keep answers concise and editable from the same configuration source as the rest of the site.",
                "items": [
                    {
                        "question": "Can this template support more than one clinic?",
                        "answer": "Yes. The Python configuration can define multiple clinic profiles and export the selected profile to the JSON file consumed by the frontend.",
                    },
                    {
                        "question": "Can doctors, services, and branches be changed without editing HTML?",
                        "answer": "Yes. Those sections are rendered from structured arrays in the generated JSON data.",
                    },
                    {
                        "question": "Is the appointment form connected to a backend?",
                        "answer": "The current template handles the interface locally and includes an optional endpoint field for future API integration.",
                    },
                    {
                        "question": "Can this become multilingual later?",
                        "answer": "Yes. The JSON is organized by locale, and the renderer already selects locale content using a query parameter such as ?lang=en.",
                    },
                ],
            },
            "contact": {
                "eyebrow": "Contact",
                "title": "Branch and appointment details from one source",
                "summary": "Display contact paths, locations, hours, and intake fields with a structure ready for API submission.",
                "schema": {
                    "telephone": "+10000000000",
                    "email": "hello@exampleclinic.com",
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": "Add clinic address",
                        "addressLocality": "Add city",
                        "addressRegion": "Add region",
                        "postalCode": "000000",
                        "addressCountry": "Add country",
                    },
                },
                "methods": [
                    {"icon": "phone", "label": "Phone", "value": "+1 (000) 000-0000", "href": "tel:+10000000000"},
                    {"icon": "mail", "label": "Email", "value": "hello@exampleclinic.com", "href": "mailto:hello@exampleclinic.com"},
                    {"icon": "message", "label": "WhatsApp", "value": "Message the front desk", "href": "https://wa.me/10000000000"},
                ],
                "form": {
                    "kicker": "Appointment request",
                    "title": "Send a visit request",
                    "note": "This form is ready to connect to an API endpoint when your backend is available.",
                    "endpoint": "",
                    "submitLabel": "Send Request",
                    "successMessage": "Your request has been captured locally for this demo.",
                    "fields": [
                        {"type": "text", "name": "name", "label": "Full name", "placeholder": "Patient name", "required": True},
                        {"type": "tel", "name": "phone", "label": "Phone number", "placeholder": "+1 000 000 0000", "required": True},
                        {"type": "select", "name": "service", "label": "Service", "required": True, "options": [
                            {"value": "", "label": "Choose a service"},
                            {"value": "primary-care", "label": "Primary Care"},
                            {"value": "specialist-care", "label": "Specialist Care"},
                            {"value": "diagnostics", "label": "Diagnostics"},
                        ]},
                        {"type": "date", "name": "date", "label": "Preferred date", "required": False},
                        {"type": "textarea", "name": "message", "label": "Message", "placeholder": "Share the reason for visit", "required": False},
                    ],
                },
                "branches": [
                    {
                        "name": "Main Branch",
                        "address": "Add primary branch address",
                        "hours": "Mon to Sat, 9:00 AM to 6:00 PM",
                        "phone": "+1 (000) 000-0000",
                        "image": {
                            "src": "./assets/images/branch-suite.png",
                            "alt": "Generic clinic branch interior",
                            "width": 1100,
                            "height": 800,
                        },
                    },
                    {
                        "name": "Second Branch",
                        "address": "Add secondary branch address",
                        "hours": "Mon to Fri, 10:00 AM to 5:00 PM",
                        "phone": "+1 (000) 000-0001",
                        "image": {
                            "src": "./assets/images/branch-suite.png",
                            "alt": "Generic clinic consultation branch",
                            "width": 1100,
                            "height": 800,
                        },
                    },
                    {
                        "name": "Telehealth Desk",
                        "address": "Add virtual care coverage details",
                        "hours": "Configured by care team availability",
                        "phone": "+1 (000) 000-0002",
                        "image": {
                            "src": "./assets/images/telehealth-suite.png",
                            "alt": "Generic telehealth consultation setup",
                            "width": 1100,
                            "height": 800,
                        },
                    },
                ],
            },
            "appointment": {
                "title": "Make the next step simple",
                "summary": "Guide patients from service discovery to contact, booking, or branch selection with clear calls to action.",
                "actions": [
                    {"label": "Request Appointment", "href": "#contact"},
                    {"label": "Call Clinic", "href": "tel:+10000000000"},
                ],
            },
            "floatingContact": {
                "label": "Chat",
                "ariaLabel": "Open WhatsApp contact",
                "href": "https://wa.me/10000000000",
                "icon": "message",
            },
            "footer": {
                "summary": "A reusable frontend template for clinics, multi-doctor practices, and healthcare organizations that manage content through structured data.",
                "columns": [
                    {
                        "title": "Template",
                        "links": [
                            {"label": "Services", "href": "#services"},
                            {"label": "Doctors", "href": "#doctors"},
                            {"label": "Branches", "href": "#contact"},
                        ],
                    },
                    {
                        "title": "Patients",
                        "links": [
                            {"label": "Appointment", "href": "#appointment"},
                            {"label": "FAQ", "href": "#faq"},
                            {"label": "Contact", "href": "#contact"},
                        ],
                    },
                    {
                        "title": "Social",
                        "links": [
                            {"label": "Instagram", "href": "https://example.com"},
                            {"label": "Facebook", "href": "https://example.com"},
                            {"label": "LinkedIn", "href": "https://example.com"},
                        ],
                    },
                ],
                "copyright": "Copyright 2026. Replace with clinic ownership details.",
                "disclaimer": "Content is configurable and should be reviewed by a healthcare professional.",
            },
        },
    },
}


clinic_profiles: dict[str, dict[str, Any]] = {
    "template": clinic_data,
}


def get_clinic_profile(clinic_id: str = "template") -> dict[str, Any]:
    try:
        return deepcopy(clinic_profiles[clinic_id])
    except KeyError as exc:
        available = ", ".join(sorted(clinic_profiles))
        raise SystemExit(f"Unknown clinic '{clinic_id}'. Available profiles: {available}") from exc


def export_json(clinic_id: str = "template", output_path: Path = DEFAULT_OUTPUT) -> Path:
    payload = get_clinic_profile(clinic_id)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Export clinic website configuration to JSON.")
    parser.add_argument("--clinic", default="template", help="Clinic profile id to export.")
    parser.add_argument("--out", default=str(DEFAULT_OUTPUT), help="Output JSON path.")
    args = parser.parse_args()

    output_path = export_json(args.clinic, Path(args.out))
    print(f"Exported {args.clinic} configuration to {output_path}")


if __name__ == "__main__":
    main()
