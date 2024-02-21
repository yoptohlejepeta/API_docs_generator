from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import getSampleStyleSheet
import os

from inputs import Title


def fill_document(make_title: Title):
    doc = SimpleDocTemplate("output/docs.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    styleN = styles["Normal"]
    styleH = styles["Heading1"]
    styleT = styles["Title"]

    title = Paragraph(make_title.title, styleT)
    if make_title.author is None:
        make_title.author = "DocGen"
    author = Paragraph(make_title.author, styleN)
    date = Paragraph(make_title.date, styleN)

    os.makedirs(os.path.dirname("output/docs.pdf"), exist_ok=True)

    doc.build([title, author, date])
