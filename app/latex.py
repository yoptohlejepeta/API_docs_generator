from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
import os

from inputs import Title

def fill_document(title: Title):
    doc = Document()
    
    doc.preamble.append(Command('title', title.title))
    if title.author:
        doc.preamble.append(Command('author', title.author))
    doc.preamble.append(Command('date', title.date))
    doc.append(NoEscape(r'\maketitle'))
    
    with doc.create(Section('A section')):
        doc.append('Some regular text and some ')
        doc.append(italic('italic text.'))
    
        with doc.create(Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')
    
    os.makedirs('output', exist_ok=True)
    doc.generate_pdf('output/docs', clean_tex=False)
    os.remove('output/docs.tex')
