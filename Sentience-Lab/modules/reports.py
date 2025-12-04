from fpdf import FPDF
from datetime import datetime

class ScientificReporter(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Sentience Lab - Ontology Report', 0, 1, 'C')
        self.ln(5)
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    def generate_pdf(self, input_text, model_name, data_summary):
        self.add_page()
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Date: {datetime.now().strftime("%Y-%m-%d")}', 0, 1)
        self.cell(0, 10, f'Target Model: {model_name}', 0, 1)
        self.ln(5)
        self.multi_cell(0, 10, f'Stimulus: "{input_text}"\n\nConclusion: {data_summary}')
        return self.output(dest='S').encode('latin-1')
