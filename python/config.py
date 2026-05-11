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
                "title": "OraCare Dental Clinic | Advanced Dentistry, Gentle Touch",
                "description": "OraCare Dental Clinic blends advanced dental technology with patient-first care for healthy, confident, radiant smiles.",
                "canonical": "./",
                "image": "./assets/images/logo.jpeg",
            },
            "branding": {
                "name": "OraCare Dental Clinic",
                "tagline": "Advanced Dentistry, Gentle Touch.",
                "logoText": "",
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
                    {"label": "About", "href": "#about"},
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
                "eyebrow": "Artistic smiles, precise care.",
                "title": "OraCare: Your Smile, Our Science.",
                "summary": "Next-gen care for a timeless smile, delivered with clinical mastery, transparency, and a gentle patient-first approach.",
                "actions": [
                    {"label": "Request Appointment", "href": "#contact"},
                    {"label": "Explore Services", "href": "#services"},
                ],
                "image": {
                    "src": "./assets/images/hero-care-suite.png",
                    "alt": "Modern dental care environment at OraCare Dental Clinic.",
                    "width": 1400,
                    "height": 1000,
                },
                "imageNote": {
                    "title": "Care meets craft.",
                    "body": "Beautiful smiles through expert care.",
                },
                "trustItems": [
                    {
                        "icon": "shield",
                        "value": "Patient-First",
                        "label": "Every treatment plan is shaped around comfort, goals, and long-term well-being.",
                    },
                    {
                        "icon": "message",
                        "value": "Compassion in Action",
                        "label": "A judgment-free dental experience where patients feel heard, relaxed, and understood.",
                    },
                    {
                        "icon": "spark",
                        "value": "Unwavering Integrity",
                        "label": "Honest advice, clear communication, and ethical care for every smile.",
                    },
                ],
            },
            "services": {
                "eyebrow": "Services",
                "title": "Complete dental care for confident smiles",
                "summary": "From preventive dentistry to cosmetic smile design, OraCare focuses on precise, personalized treatment in a calm clinical setting.",
                "items": [
                    {
                        "icon": "stethoscope",
                        "title": "Preventive Dentistry",
                        "description": "Routine dental exams, cleanings, and oral health guidance designed to protect smiles before problems grow.",
                        "highlights": ["Dental checkups", "Professional cleaning", "Oral hygiene guidance"],
                    },
                    {
                        "icon": "calendar",
                        "title": "Cosmetic Smile Design",
                        "description": "Aesthetic dentistry options focused on natural-looking, radiant results that match each patient's goals.",
                        "highlights": ["Smile planning", "Whitening guidance", "Aesthetic restorations"],
                    },
                    {
                        "icon": "shield",
                        "title": "Restorative Dentistry",
                        "description": "Precision-driven care for damaged, decayed, or missing teeth with a focus on function and appearance.",
                        "highlights": ["Tooth-colored restorations", "Crown planning", "Bite-focused care"],
                    },
                    {
                        "icon": "user",
                        "title": "Expert Consultations",
                        "description": "Personalized dental assessments with clear explanations, practical options, and transparent recommendations.",
                        "highlights": ["Personalized treatment plans", "Second-opinion support", "Clear care discussions"],
                    },
                    {
                        "icon": "message",
                        "title": "Gentle Patient Care",
                        "description": "A comfort-first approach for patients who want dental visits to feel calm, respectful, and reassuring.",
                        "highlights": ["Judgment-free visits", "Anxiety-aware care", "Step-by-step guidance"],
                    },
                    {
                        "icon": "spark",
                        "title": "Lifelong Oral Health",
                        "description": "Ongoing care plans that support oral health, confidence, and radiant smiles at every stage of life.",
                        "highlights": ["Maintenance plans", "Follow-up support", "Long-term smile health"],
                    },
                ],
            },
            "about": {
                "eyebrow": "About OraCare",
                "title": "Where every smile tells a story.",
                "summary": "OraCare Dental Clinic combines advanced technology, clinical mastery, and a patient-first philosophy to make modern dentistry feel precise, transparent, and personal.",
                "vision": {
                    "title": "Vision",
                    "body": "To redefine the standard of modern dentistry through innovative care and clinical mastery, ensuring OraCare is the first name in lifelong oral health and radiant smiles.",
                },
                "mission": {
                    "title": "Mission",
                    "body": "At OraCare, our mission is to redefine the dental experience through a fusion of advanced technology and a patient-first philosophy. Our dedicated team delivers precision-driven, personalized care to ensure every patient leaves with a healthy, confident, and radiant smile.",
                },
                "valuesTitle": "The OraCare Core Values",
                "valuesSummary": "A healthy smile is built on more than clinical skill. It is built on trust, innovation, and genuine connection.",
                "values": [
                    {
                        "icon": "shield",
                        "title": "Patient-First",
                        "body": "We do not just treat teeth; we care for people. Every treatment plan is a collaboration designed around comfort, goals, and lifestyle.",
                    },
                    {
                        "icon": "message",
                        "title": "Compassion in Action",
                        "body": "Dental visits can be daunting, so we lead with empathy and create a judgment-free space where kindness is the default.",
                    },
                    {
                        "icon": "check",
                        "title": "Unwavering Integrity",
                        "body": "Trust is our most valuable instrument. We practice honest advice, clear pricing, and ethical care that puts health first.",
                    },
                ],
            },
            "doctors": {
                "eyebrow": "Care team",
                "title": "Meet the OraCare clinical team",
                "summary": "Our clinicians bring together dental expertise, thoughtful communication, and a comfort-focused approach to oral health.",
                "featuredDoctors": [
                    {
                        "kicker": "Lead clinician",
                        "name": "Dr.Gayathri.R",
                        "role": "Oral Medicine and Radiology",
                        "bio": "MBBS, MDS, FMCN",
                        "image": {
                            "src": "./assets/images/DR.Gayathri.jpeg",
                            "alt": "Generic lead clinician portrait placeholder",
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
                    {
                        "kicker": "Lead clinician",
                        "name": "Dr.K.Prabhu",
                        "role": "prosthodontist",
                        "bio": "MBBS, MDS",
                        "image": {
                            "src": "./assets/images/old photo .png",
                            "alt": "Generic second lead clinician portrait placeholder",
                            "width": 900,
                            "height": 1100,
                        },
                        "stats": [
                            {"icon": "stethoscope", "value": "Specialty focus", "label": "Show lead clinician expertise"},
                            {"icon": "mapPin", "value": "Branch coverage", "label": "Connect availability to locations"},
                        ],
                        "cta": {
                            "label": "View Appointment Options",
                            "href": "#contact",
                        },
                    },
                ],
                "items": [
                    {
                        "name": "",
                        "role": "Clinical dentistry support",
                        "bio": "Focused on careful assessment, patient education, and coordinated support throughout the dental visit.",
                        "focusAreas": ["Preventive guidance", "Treatment preparation", "Follow-up support"],
                    },
                    {
                        "name": "",
                        "role": "Aesthetic care support",
                        "bio": "Supports cosmetic planning and patient communication for natural-looking, confidence-building smile outcomes.",
                        "focusAreas": ["Smile goals", "Aesthetic planning", "Result-focused care"],
                    },
                    {
                        "name": "",
                        "role": "Comfort and coordination",
                        "bio": "Helps patients feel informed, prepared, and supported before, during, and after their appointment.",
                        "focusAreas": ["Appointment guidance", "Comfort support", "Care coordination"],
                    },
                ],
            },
            "testimonials": {
                "eyebrow": "Patient feedback",
                "title": "Patients choose care they can feel",
                "summary": "OraCare is built around clear communication, gentle treatment, and confidence at every step.",
                "labels": {
                    "previous": "Show previous testimonial",
                    "next": "Show next testimonial",
                    "pagination": "Testimonial pagination",
                },
                "items": [
                    {
                        "ratingLabel": "5.0 patient rating",
                        "quote": "The visit felt calm and organized, and every step of the treatment plan was explained clearly.",
                        "name": "Patient A",
                        "context": "Verified visit",
                    },
                    {
                        "ratingLabel": "5.0 patient rating",
                        "quote": "The team listened patiently, answered questions, and made the experience feel genuinely comfortable.",
                        "name": "Patient B",
                        "context": "Follow-up care",
                    },
                    {
                        "ratingLabel": "5.0 patient rating",
                        "quote": "The care felt precise and personal, with honest guidance about what my smile actually needed.",
                        "name": "Patient C",
                        "context": "Smile care",
                    },
                ],
            },
            "faq": {
                "eyebrow": "Questions",
                "title": "Helpful answers before your dental visit",
                "summary": "Find quick guidance on appointments, comfort, treatment planning, and OraCare's patient-first approach.",
                "items": [
                    {
                        "question": "What makes OraCare's approach different?",
                        "answer": "OraCare combines advanced dentistry with a gentle, patient-first philosophy so treatment feels clear, comfortable, and personalized.",
                    },
                    {
                        "question": "Can I discuss my smile goals before treatment?",
                        "answer": "Yes. Every plan starts with a conversation about your comfort, goals, lifestyle, and long-term oral health.",
                    },
                    {
                        "question": "I feel nervous about dental visits. Can OraCare help?",
                        "answer": "Yes. Compassion in action is one of OraCare's core values, and the clinic is designed to be judgment-free, calm, and reassuring.",
                    },
                    {
                        "question": "Will treatment options and pricing be explained clearly?",
                        "answer": "Yes. OraCare values transparent advice, clear communication, and ethical care that puts your health first.",
                    },
                ],
            },
            "contact": {
                "eyebrow": "Contact",
                "title": "Book a visit with OraCare",
                "summary": "Share your preferred visit details and the OraCare team will help guide the next step.",
                "schema": {
                    "telephone": "+919940592307",
                    "email": "oracare7@gmail.com",
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": "No:161/282 , Thandalam Road",
                        "addressLocality": "Vallalar Nagar , Ranipet",
                        "addressRegion": "TamilNadu",
                        "postalCode": "632401",
                        "addressCountry": "India",
                    },
                },
                "methods": [
                    {"icon": "phone", "label": "Phone", "value": "+91 99405 92307", "href": "tel:+919940592307"},
                    {"icon": "mail", "label": "Email", "value": "oracare7@gmail.com", "href": "mailto:oracare7@gmail.com"},
                    {"icon": "message", "label": "WhatsApp", "value": "Book an Appointment", "href": "https://wa.me/+919940592307"},
                ],
                "form": {
                    "kicker": "Appointment request",
                    "title": "Start your smile care request",
                    "note": "Tell us what you would like help with, and the team will confirm the next steps.",
                    "endpoint": "",
                    "submitLabel": "Send Request",
                    "successMessage": "Your request has been received. The OraCare team will follow up soon.",
                    "fields": [
                        {"type": "text", "name": "name", "label": "Full name", "placeholder": "Patient name", "required": True},
                        {"type": "tel", "name": "phone", "label": "Phone number", "placeholder": "+1 000 000 0000", "required": True},
                        {"type": "select", "name": "service", "label": "Service", "required": True, "options": [
                            {"value": "", "label": "Choose a service"},
                            {"value": "preventive-dentistry", "label": "Preventive Dentistry"},
                            {"value": "cosmetic-smile-design", "label": "Cosmetic Smile Design"},
                            {"value": "restorative-dentistry", "label": "Restorative Dentistry"},
                        ]},
                        {"type": "date", "name": "date", "label": "Preferred date", "required": False},
                        {"type": "textarea", "name": "message", "label": "Message", "placeholder": "Share the reason for visit", "required": False},
                    ],
                },
                "branches": [
                    {
                        "name": "OraCare Dental Clinic, Ranipet",
                        "address": "No:161/282, Thandalam Road, Vallalar Nagar, Ranipet.",
                        "hours": "9:30 AM to 1:00 PM and 4.30 PM to 9.00 PM",
                        "phone": "+91 99405 92307",
                        "image": {
                            "src": "./assets/images/branch-suite.png",
                            "alt": "OraCare dental clinic interior placeholder",
                            "width": 1100,
                            "height": 800,
                        },
                    },
                    {
                        "name": "OraCare Dental Clinic, Chengalpattu.",
                        "address": "No:256B, Main Road, Sai Lskshmi Nagar, Nenmeli, Chengalpattu ",
                        "hours": "9.00 AM to 9.00 PM",
                        "phone": "+91 9994179155 / +91 9940592307",
                        "image": {
                            "src": "./assets/images/branch-suite.png",
                            "alt": "OraCare second dental clinic, Chengalpattu",
                            "width": 1100,
                            "height": 800,
                        },
                    },
                    {
                        "name": "OraCare TeleConsultation",
                        "address": "Consult our Doctors via TeleConsultation",
                        "hours": "7.00 AM to 9.00 PM",
                        "phone": "+91 9940592307",
                        "image": {
                            "src": "./assets/images/telehealth-suite.png",
                            "alt": "OraCare virtual consultation",
                            "width": 1100,
                            "height": 800,
                        },
                    },
                ],
            },
            "appointment": {
                "title": "Ready for a healthier, brighter smile?",
                "summary": "Request an appointment and take the next step toward advanced dentistry with a gentle touch.",
                "actions": [
                    {"label": "Request Appointment", "href": "#contact"},
                    {"label": "Call Clinic", "href": "tel:+919940592307"},
                ],
            },
            "floatingContact": {
                "label": "Chat",
                "ariaLabel": "Open WhatsApp contact",
                "href": "https://wa.me/+919940592307",
                "icon": "message",
            },
            "footer": {
                "summary": "OraCare Dental Clinic blends advanced technology, clinical mastery, and compassionate care for lifelong oral health and radiant smiles.",
                "columns": [
                    {
                        "title": "OraCare",
                        "links": [
                            {"label": "About", "href": "#about"},
                            {"label": "Services", "href": "#services"},
                            {"label": "Doctors", "href": "#doctors"},
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
                            {"label": "Instagram", "href": "https://www.instagram.com/oracare_ranipet?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="},
                            {"label": "", "href": "https://example.com"},
                            {"label": "", "href": "https://example.com"},
                        ],
                    },
                ],
                "copyright": "Copyright 2026 OraCare Dental Clinic. All rights reserved.",
                "disclaimer": "Dental information is for general guidance and does not replace a clinical consultation.",
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
