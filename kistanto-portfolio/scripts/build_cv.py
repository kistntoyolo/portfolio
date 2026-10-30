"""Membuat assets/cv/Kistanto_CV.pdf dari data yang sudah dikonfirmasi.

Jalankan: python3 scripts/build_cv.py   (butuh: pip install reportlab)
Edit data pada konstanta di bawah, lalu jalankan ulang untuk memperbarui CV.
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv" / "Kistanto_CV.pdf"

ACCENT = colors.HexColor("#1a73f0")
DARK = colors.HexColor("#0a0f24")
GREY = colors.HexColor("#4b5563")

NAME = "KISTANTO"
TAGLINE = "Informatics Graduate | Python Developer | Computer Vision Enthusiast"
CONTACT = (
    "Brebes, Jawa Tengah, Indonesia &nbsp;|&nbsp; WhatsApp: 085227341724 &nbsp;|&nbsp; Email: kistnto@gmail.com &nbsp;|&nbsp; "
    '<link href="https://github.com/kistntoyolo" color="#1a73f0">github.com/kistntoyolo</link>'
)
SUMMARY = (
    "Lulusan S1 Teknik Informatika Universitas Muhadi Setiabudi (2026) dengan ketertarikan pada "
    "pengembangan perangkat lunak berbasis Artificial Intelligence dan Computer Vision. "
    "Berpengalaman membangun sistem deteksi objek berbasis YOLO yang diintegrasikan ke aplikasi Streamlit "
    "melalui proyek tugas akhir. Mencari kesempatan sebagai Software Developer, Python Developer, "
    "AI / Machine Learning Engineer, atau Computer Vision Engineer."
)
EDUCATION = [
    ("Universitas Muhadi Setiabudi", "2022 – 2026"),
    ("Sarjana Teknik Informatika", "IPK 3,43 / 4,00 · 145 SKS · Predikat Sangat Memuaskan"),
]
PROJECT_TITLE = "SoleGuard – Shoe Defect Detection System"
PROJECT_META = "Final Year Project · Studi kasus: PT. Tah Sung Hung · Python, YOLOv26n, Streamlit"
PROJECT_DESC = (
    "Sistem deteksi cacat produk sepatu menggunakan Object Detection berbasis YOLOv26n yang diintegrasikan "
    "ke aplikasi Streamlit untuk membantu pemeriksaan produk melalui input video."
)
PROJECT_POINTS = [
    "Upload video MP4, AVI, dan MOV",
    "Object Detection dengan YOLOv26n, Confidence Threshold, dan IoU Threshold",
    "Filter kelas defect, statistik deteksi, dan riwayat deteksi",
    "Real-time detection",
]
SKILLS = [
    ("Programming", "Python"),
    ("Artificial Intelligence", "YOLOv26n, Object Detection, Deep Learning"),
    ("Computer Vision", "Image Detection, Computer Vision"),
    ("Framework", "Streamlit"),
    ("Tools", "GitHub"),
]
COURSES = (
    "Deep Learning, Data Mining, Analisis Big Data, Pemrograman Website, Pemrograman Client-Server, "
    "Sistem Basis Data, Struktur Data, Algoritma Pemrograman, Network Security"
)


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)

    h_name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=26, leading=30, textColor=DARK)
    h_tag = ParagraphStyle("tag", fontName="Helvetica", fontSize=10.5, leading=14, textColor=ACCENT)
    h_contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=9, leading=13, textColor=GREY)
    h_sec = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=ACCENT, spaceBefore=12, spaceAfter=3)
    body = ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, leading=14, textColor=DARK)
    bold = ParagraphStyle("bold", parent=body, fontName="Helvetica-Bold")
    meta = ParagraphStyle("meta", parent=body, textColor=GREY, fontSize=9)

    def rule():
        return HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#d1d5db"), spaceAfter=5)

    doc = SimpleDocTemplate(
        str(OUT), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=14 * mm,
        title="CV Kistanto", author="Kistanto",
    )

    s = [Paragraph(NAME, h_name), Paragraph(TAGLINE, h_tag), Spacer(1, 3), Paragraph(CONTACT, h_contact)]

    s += [Paragraph("PROFIL", h_sec), rule(), Paragraph(SUMMARY, body)]

    s += [Paragraph("PENDIDIKAN", h_sec), rule()]
    s += [Paragraph(f"<b>{EDUCATION[0][0]}</b> &nbsp;·&nbsp; {EDUCATION[0][1]}", body)]
    s += [Paragraph(EDUCATION[1][0], body), Paragraph(EDUCATION[1][1], meta)]

    s += [Paragraph("PROYEK", h_sec), rule(), Paragraph(PROJECT_TITLE, bold), Paragraph(PROJECT_META, meta), Spacer(1, 2)]
    s += [Paragraph(PROJECT_DESC, body), Spacer(1, 2)]
    s += [ListFlowable([ListItem(Paragraph(p, body), leftIndent=12) for p in PROJECT_POINTS], bulletType="bullet", start="•", leftIndent=12)]
    s += [Paragraph('<link href="https://github.com/kistntoyolo/SoleGuard-YOLOv26n" color="#1a73f0">github.com/kistntoyolo/SoleGuard-YOLOv26n</link>', meta)]

    s += [Paragraph("KEMAMPUAN TEKNIS", h_sec), rule()]
    for k, v in SKILLS:
        s.append(Paragraph(f"<b>{k}:</b> {v}", body))

    s += [Paragraph("MATA KULIAH RELEVAN", h_sec), rule(), Paragraph(COURSES, body)]

    doc.build(s)
    print(f"CV dibuat: {OUT}")


if __name__ == "__main__":
    main()
