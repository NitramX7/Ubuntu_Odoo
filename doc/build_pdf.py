import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PDF = os.path.join(BASE_DIR, "Entrega_Equipos.pdf")
SRC_MD = os.path.join(BASE_DIR, "Entrega_Equipos.md")
CAPTURAS_DIR = os.path.join(BASE_DIR, "capturas")


def parse_md_to_flowables(md_path):
    styles = getSampleStyleSheet()
    normal = styles["BodyText"]
    normal.alignment = TA_LEFT
    title = styles["Title"]
    h2 = styles["Heading2"]
    bullets = []
    flow = []

    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    def flush_bullets():
        nonlocal bullets
        for b in bullets:
            flow.append(Paragraph(f"• {b}", normal))
            flow.append(Spacer(1, 0.2 * cm))
        bullets = []

    for line in lines:
        if line.startswith("# "):
            flush_bullets()
            flow.append(Paragraph(line[2:].strip(), title))
            flow.append(Spacer(1, 0.5 * cm))
        elif line.startswith("## "):
            flush_bullets()
            flow.append(Spacer(1, 0.2 * cm))
            flow.append(Paragraph(line[3:].strip(), h2))
            flow.append(Spacer(1, 0.2 * cm))
        elif line.startswith("- "):
            bullets.append(line[2:].strip())
        elif line.strip() == "":
            flush_bullets()
            flow.append(Spacer(1, 0.2 * cm))
        else:
            flush_bullets()
            flow.append(Paragraph(line, normal))
            flow.append(Spacer(1, 0.2 * cm))

    flush_bullets()
    return flow


def add_capturas(flow):
    if not os.path.isdir(CAPTURAS_DIR):
        return
    files = sorted(
        [f for f in os.listdir(CAPTURAS_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    )
    if not files:
        return
    styles = getSampleStyleSheet()
    h2 = styles["Heading2"]
    normal = styles["BodyText"]
    flow.append(PageBreak())
    flow.append(Paragraph("Capturas de pantalla", h2))
    flow.append(Spacer(1, 0.4 * cm))
    max_width = 16 * cm
    for fname in files:
        path = os.path.join(CAPTURAS_DIR, fname)
        try:
            img = Image(path)
            # scale respecting aspect ratio
            w, h = img.drawWidth, img.drawHeight
            if w > max_width:
                scale = max_width / w
                img.drawWidth = w * scale
                img.drawHeight = h * scale
            flow.append(img)
            flow.append(Paragraph(fname, normal))
            flow.append(Spacer(1, 0.5 * cm))
        except Exception as e:
            flow.append(Paragraph(f"No se pudo insertar {fname}: {e}", normal))
            flow.append(Spacer(1, 0.2 * cm))


def build_pdf():
    doc = SimpleDocTemplate(
        OUT_PDF,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="Entrega Equipos",
        author="martinModulo",
    )
    flow = parse_md_to_flowables(SRC_MD)
    add_capturas(flow)
    doc.build(flow)
    print(f"PDF generado: {OUT_PDF}")


if __name__ == "__main__":
    os.makedirs(CAPTURAS_DIR, exist_ok=True)
    build_pdf()
