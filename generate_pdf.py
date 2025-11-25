from fpdf import FPDF

def create_pdf(result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="FakeFind Review Report", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Grade: {result['grade']}", ln=True)
    pdf.cell(200, 10, txt=f"Fake Reviews: {result['fake_percentage']}%", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Reviews:", ln=True)

    for r in result["reviews"]:
        pdf.ln(8)
        status = "Fake" if r["fake"] else "Genuine"
        pdf.multi_cell(0, 8, f"[{status}] {r['text']}")

    pdf.output("report.pdf")
