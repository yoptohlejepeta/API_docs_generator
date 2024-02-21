from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import getSampleStyleSheet

from inputs import Title

def fill_document(make_title: Title):
    doc = SimpleDocTemplate("output/docs.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']
    styleT = styles['Title']

    title = Paragraph(make_title.title, styleT)
    author = Paragraph(make_title.author, styleN)
    date = Paragraph(make_title.date, styleN)

    doc.build([title, author, date])
