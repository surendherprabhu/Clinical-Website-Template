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
                "tagline": "Beautiful smiles through expert care.",
                "logo": {
                    "src": "./assets/images/logo.jpeg",
                    "alt": "OraCare Dental Clinic logo",
                    "width": 64,
                    "height": 64,
                },
                "theme": {
                    "primary": "#1676c4",
                    "primaryDark": "#135a7a",
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
                "actions": [
                    {
                        "label": "Aligner Camp",
                        "href": "https://forms.gle/REPLACE_WITH_ALIGNER_CAMP_FORM_LINK",
                        "variant": "secondary",
                    },
                    {
                        "label": "Book Appointment",
                        "href": "#appointment",
                        "variant": "primary",
                    },
                ],
            },
            "hero": {
                "eyebrow": "The place where lively smiles are made.",
                "title": "Oral Health is Over-All Health.",
                "summary": "Personalized dental care for your confident smile, delivered with clinical mastery and transparency.",
                "actions": [
                    {"label": "Request Appointment", "href": "#appointment"},
                    {"label": "Explore Services", "href": "#services"},
                ],
                "image": {
                    "src": "./assets/images/logo.jpeg",
                    "alt": "Modern dental care environment at OraCare Dental Clinic.",
                    "width": 1400,
                    "height": 1000,
                },
                "imageNote": {
                    "title": "Care meets craft.",
                    "body": "A Dentist is a Doctor, an Artist, and an Enginneer, all at the same time and at the same place.",
                },
                "trustItems": [],
            },
            "services": {
                "eyebrow": "Services",
                "title": "Complete dental care for confident smiles",
                "summary": "Here at OraCare Dental Clinic, we focus on precise and personalized treatment for any and all dental needs.",
                "items": [
                    {
                        "icon": "stethoscope",
                        "title": "Diagnosis",
                        "image": {
                            "src": "./assets/images/services/diagnosis.jpg",
                            "alt": "Diagnosis",
                            "width": 800,
                            "height": 520,
                        },
                    },
                    {
                        "icon": "calendar",
                        "title": "X-Ray",
                        "image": {
                            "src": "./assets/images/services/xray.jpg",
                            "alt": "X-Ray",
                            "width": 800,
                            "height": 520,
                        },
                    },
                    {
                        "icon": "shield",
                        "title": "Preventive Dentistry",
                        "image": {
                            "src": "./assets/images/services/preventive dentistry.jpg",
                            "alt": "Preventive Dentistry",
                            "width": 800,
                            "height": 520,
                        },
                    },
                    {
                        "icon": "user",
                        "title": "Prosthodontics and Implantology",
                        "image": {
                            "src": "./assets/images/services/Implant.jpg",
                            "alt": "Prosthodontics and Implantology",
                            "width": 800,
                            "height": 520,
                        },
                    },
                    {
                        "icon": "message",
                        "title": "Orthodontics and Aligner Therapy",
                        "image": {
                            "src": "./assets/images/services/Aligners.jpg",
                            "alt": "Orthodontics and Aligner Therapy",
                            "width": 800,
                            "height": 520,
                        },
                    },
                    {
                        "icon": "spark",
                        "title": "Restorative Dentistry",
                        "image": {
                            "src": "./assets/images/services/restrorative dentistry.jpg",
                            "alt": "Restorative Dentistry",
                            "width": 800,
                            "height": 520,
                        },
                    },
                ],
            },
            "about": {
                "eyebrow": "About OraCare",
                "title": "Where every smile tells you a story.",
                "summary": """Founded in the year 2018, In the city of Ranipet, OraCare Dental Clinic offers complete dental care for any and all dental needs.
We follow a multi-disciplinary practice in which Specialists in various fields provide you with the Best possible Dental Treatment. With Experienced hands and a wide range of treatments offered, we are committed to providing the best dental care experience for our patients, with a focus on personalized treatment and a compassionate approach.""",
                "vision": {
                    "title": "Vision",
                    "body": "Our vision is to prioritize every patient, raise awareness about Oral Health and its impact on the overall health of an individual and to provide ethical Medical and Dental practice.",
                },
                "mission": {
                    "title": "Mission",
                    "body": "Our mission is to provide Oral Health Care services with good standards to every individual in the community.",
                },
            },
            "doctors": {
                "eyebrow": "Care team",
                "title": "Meet the OraCare clinical team",
                "summary": "Our clinicians bring together dental expertise, thoughtful communication, and a comfort-focused approach to oral health.",
                "featuredDoctors": [
                    {
                        "kicker": "Lead clinician",
                        "name": "Dr.Gayathri.R",
                        "role": "MBBS, MDS, FMCN - Oral Medicine and Radiology",
                        "bio": "Born and brought up in Ranipet, Dr.Gayathri.R did her Bachelor of Dental Surgery (BDS) in Saveetha Dental College, Chennai in the year 2007. She completed her Master of Dental Surgery (MDS) in Oral Medicine and Radiology in the year 2011. She has been into the academic field for more than 7 years and has published in both national and international Dental jouranals and Publications. She has since then started her practice in both Ranipet and Chengalpattu and has further completed The Functional Medicine course in the year 2025s. With over 15 years of experience in the field of dentistry, Dr.Gayathri.R has a deep understanding of oral health and in Functional Medicine. Dr.Gayathri.R is passionate about helping her patients achieve optimal oral health and a confident smile.",
                        "image": {
                            "src": "./assets/images/DR.Gayathri.jpeg",
                            "alt": "Generic lead clinician portrait placeholder",
                            "width": 900,
                            "height": 1100,
                        },
                        "cta": {
                            "label": "View Appointment Options",
                            "href": "#contact",
                        },
                    },
                    {
                        "kicker": "Lead clinician",
                        "name": "Dr.K.Prabhu",
                        "role": "MBBS, MDS - Prosthodontics and Implantology",
                        "bio": "Born and Brought up in Chengalpattu, Dr.Prabhu.K did his bachelor of Dental Surgery (BDS) in Rajah Muthiah Dental College, Chidambaram and followed on his Master of Dental Surgery (MDS) in Saveetha Dental College, Chennai in the year 2010. He has also Completed his training in Computer Guided Implant Dentistry in Belgium in the year 2010. He has since been in the academic field for more than 15 years and has also published in numerous National and International Dental Journals and Publications. He has also been practicing in both Ranipet and Chengalpattu. He has a deep understanding of Prosthodontics and Implantology and is passionate about helping his patients achieve optimal oral health and a confident smile.",
                        "image": {
                            "src": "./assets/images/Prabhu.jpeg",
                            "alt": "Generic second lead clinician portrait placeholder",
                            "width": 900,
                            "height": 1100,
                        },
                        "cta": {
                            "label": "View Appointment Options",
                            "href": "#contact",
                        },
                    },
                ],
            },
            "testimonials": {
                "eyebrow": "Patient feedback",
                "title": "Read what patients say on Google",
                "summary": "Visit OraCare's Google Reviews profile for current patient feedback.",
                "googleReviews": {
                    "label": "View Google Reviews",
                    "href": "https://share.google/fwXxFECKLiYlZywYF",
                },
                "items": [],
            },
            "faq": {
                "eyebrow": "Questions",
                "title": "Helpful answers before your dental visit",
                "summary": "Find quick guidance on appointments, comfort, treatment planning, and OraCare's patient-first approach.",
                "items": [
                    {
                        "question": "When should my child have their first dental visit?",
                        "answer": "It is recommended that a child’s first dental visit be scheduled by their first birthday or within six months of the first tooth erupting. Early visits help ensure proper oral development and prevent future dental issues.",
                    },
                    {
                        "question": "What toothpaste should I use, and when should I start using it?",
                        "answer": "There is no objective best toothpaste for everyone. The right toothpaste depends on your individual oral health needs and preferences. For children under 3 years old, use a smear of fluoride toothpaste. For children 3-6 years old, use a pea-sized amount. Adults should choose a fluoride toothpaste that meets their specific needs, such as sensitivity or whitening.",
                    },
                    {
                        "question": "Is Dental flossing really necessary?",
                        "answer": "Yes. Flossing is an important part of oral hygiene as it helps remove plaque and food particles from between the teeth and under the gumline, areas that a toothbrush cannot reach. Regular flossing can help prevent cavities, gum disease, and bad breath.",
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
                    "title": "Book through our Google Form",
                    "note": "Appointments are collected through Google Forms and saved automatically to Google Sheets.",
                    "externalUrl": "https://forms.gle/REPLACE_WITH_YOUR_GOOGLE_FORM_LINK",
                    "submitLabel": "Open Appointment Form",
                },
                "branches": [
                    {
                        "name": "OraCare Dental Clinic, Ranipet",
                        "address": "No:161/282, Thandalam Road, Vallalar Nagar, Ranipet.",
                        "hours": "9:30 AM to 1:00 PM and 4.30 PM to 9.00 PM",
                        "phone": "+91 99405 92307",
                        "image": {
                            "src": "./assets/images/rpt.jpeg",
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
                            "src": "./assets/images/cpt.jpg",
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
                "summary": "Request an appointment through the OraCare Google Form.",
                "actions": [
                    {"label": "Open Appointment Form", "href": "https://docs.google.com/forms/d/e/1FAIpQLSfU0oo9fUOq7GHQhD0d8pGZ1q8xKdhshD3AQbSRVbUls680tA/viewform?usp=publish-editor"},
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
