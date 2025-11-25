from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import random
import io
import logging

# Try to import reportlab, but if not installed use fallback to text-only PDF with reportlab error message
try:
    from reportlab.pdfgen import canvas
    REPORTLAB_OK = True
except Exception:
    REPORTLAB_OK = False

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)


def fake_model_predict(review):
    """Dummy predictor for demo: returns 1 for fake, 0 for real randomly."""
    return random.choice([0, 1])


def scrape_reviews(url):
    """Demo scraper: replace with real scraping / API later."""
    return [
        "Great product, works perfectly!",
        "Worst product ever, waste of money.",
        "Amazing quality, highly recommend.",
        "Totally fake product, don't buy!"
    ]


def clean(text):
    return text.lower().strip()


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON received"}), 400

    url = data.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    app.logger.info(f"Analyze request for URL: {url}")

    reviews = scrape_reviews(url)
    cleaned = [clean(r) for r in reviews]
    preds = [fake_model_predict(r) for r in cleaned]

    fake_percent = int((sum(preds) / max(len(preds), 1)) * 100)
    trust_score = 100 - fake_percent
    grade = "A" if trust_score >= 80 else "B" if trust_score >= 60 else "C"
    verdict = "Mostly Genuine" if trust_score >= 80 else "Mixed Reviews" if trust_score >= 60 else "Mostly Fake"

    insights = [
        f"{fake_percent}% reviews detected as fake",
        f"Trust Score: {trust_score}%",
        f"Grade: {grade}"
    ]

    result = {
        "trust_score": trust_score,
        "grade": grade,
        "verdict": verdict,
        "insights": insights,
        "reviews": [{"text": r, "fake": bool(p)} for r, p in zip(reviews, preds)]
    }

    return jsonify(result)


@app.route("/download-pdf", methods=["POST"])
def download_pdf():
    data = request.get_json()
    if not data or "result" not in data:
        return jsonify({"error": "No result data received"}), 400

    result = data["result"]

    buffer = io.BytesIO()

    if REPORTLAB_OK:
        pdf = canvas.Canvas(buffer)
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(50, 800, "FakeFind Review Report")
        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, 770, f"Trust Score: {result.get('trust_score', 'N/A')}%")
        pdf.drawString(50, 750, f"Grade: {result.get('grade', 'N/A')}")
        pdf.drawString(50, 730, f"Verdict: {result.get('verdict', 'N/A')}")
        y = 700
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(50, y, "Reviews:")
        y -= 24
        pdf.setFont("Helvetica", 12)
        for r in result.get("reviews", []):
            text = f"{'Fake' if r.get('fake') else 'Real'} - {r.get('text','')}"
            pdf.drawString(50, y, text[:90])   # clip long lines
            y -= 18
            if y < 60:
                pdf.showPage()
                y = 800
        pdf.save()
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name="FakeFind_Report.pdf", mimetype="application/pdf")
    else:
        # Simple fallback: return small plain PDF-like text file and an error message
        content = io.BytesIO()
        content.write(b"Reportlab not installed on server. Install with: pip install reportlab\n\n")
        content.write(f"Trust Score: {result.get('trust_score','N/A')}\n".encode())
        content.write(f"Grade: {result.get('grade','N/A')}\n".encode())
        content.write(f"Verdict: {result.get('verdict','N/A')}\n\n".encode())
        content.write("Reviews:\n".encode())
        for r in result.get("reviews", []):
            content.write((f"{'Fake' if r.get('fake') else 'Real'} - {r.get('text','')}\n").encode())
        content.seek(0)
        return send_file(content, as_attachment=True, download_name="FakeFind_Report.txt", mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
