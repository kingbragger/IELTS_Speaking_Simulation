from fpdf import FPDF

def generate_pdf(feedback, file_name="feedback_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="IELTS Speaking Test Feedback", ln=True, align='C')
    pdf.multi_cell(0, 10, feedback)
    pdf.output(file_name)
    return file_name