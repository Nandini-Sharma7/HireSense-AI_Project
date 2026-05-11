from fpdf import FPDF

def generate_pdf(
    speech,
    face,
    emotion,
    nlp,
    resume,
    final,
    suggestions
):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=16)

    pdf.cell(
        200,
        10,
        txt="HireSense AI Interview Report",
        ln=True,
        align='C'
    )

    pdf.ln(10)

    pdf.set_font("Arial", size=12)

    pdf.cell(
        200,
        10,
        txt=f"Speech Confidence: {speech}%",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Facial Confidence: {face}%",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Detected Emotion: {emotion}",
        ln=True
    )
    
    pdf.cell(
        200,
        10,
        txt=f"Answer Relevance: {nlp}%",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Resume Match: {resume}%",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Final Score: {final}/10",
        ln=True
    )

    pdf.ln(10)

    pdf.cell(
        200,
        10,
        txt="AI Suggestions:",
        ln=True
    )

    for item in suggestions:
        pdf.multi_cell(
            0,
            10,
            txt=f"- {item}"
        )

    pdf.output("HireSense_Report.pdf")

    return "HireSense_Report.pdf"