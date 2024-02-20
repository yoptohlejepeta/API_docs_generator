from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
import os

def fill_document():
    doc = Document()
    
    with doc.create(Section('A section')):
        doc.append('Some regular text and some ')
        doc.append(italic('italic text.'))
        doc.append(NoEscape(r' \textbf{This is bold.}'))
        doc.append(NoEscape(r' \texttt{This is monospace.}'))
        doc.append(NoEscape(r' \textsc{This is small caps.}'))
        doc.append(NoEscape(r' \textsl{This is slanted.}'))
        doc.append(NoEscape(r' \textit{This is italic.}'))
        doc.append(NoEscape(r' \textsf{This is sans serif.}'))
        doc.append(NoEscape(r' \textnormal{This is normal.}'))
        doc.append(NoEscape(r' \texttt{This is monospace.}'))
        doc.append(NoEscape(r' \textup{This is upright.}'))
        doc.append(NoEscape(r' \textbf{This is bold.}'))
        
        with doc.create(Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')
            doc.append(NoEscape(r' \LaTeX.'))
            doc.append(Command('LaTeX'))
            doc.append(NoEscape(r' \ldots'))
            doc.append(NoEscape(r' \textbackslash'))
            
            with doc.create(Subsection('A subsubsection')):
                doc.append('And some more text.')
                doc.append(NoEscape(r' \ldots'))
                doc.append(NoEscape(r' \textbackslash'))
                doc.append(NoEscape(r' \LaTeX.'))
                doc.append(Command('LaTeX'))
                doc.append(NoEscape(r' \ldots'))
                doc.append(NoEscape(r' \textbackslash'))
                doc.append(NoEscape(r' \LaTeX.'))
                doc.append(Command('LaTeX'))
                doc.append(NoEscape(r' \ldots'))
                doc.append(NoEscape(r' \textbackslash'))
                doc.append(NoEscape(r' \LaTeX.'))
                
    with doc.create(Section('Another section')):
        doc.append('Some text.')
        with doc.create(Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')
            doc.append(NoEscape(r' \LaTeX.'))
            doc.append(Command('LaTeX'))
            doc.append(NoEscape(r' \ldots'))
            doc.append(NoEscape(r' \textbackslash'))
            with doc.create(Subsection('A subsubsection')):
                doc.append('And some more text.')
                doc.append(NoEscape(r' \ldots'))
                doc.append(NoEscape(r' \textbackslash'))
                doc.append(NoEscape(r' \LaTeX.'))
                doc.append(Command('LaTeX'))
                doc.append(NoEscape(r' \ldots'))
                doc.append(NoEscape(r' \textbackslash'))
                doc.append(NoEscape(r' \LaTeX.'))
                doc.append(Command('LaTeX'))
                doc.append(NoEscape(r' \ldots'))
                doc.append(NoEscape(r' \textbackslash'))
                doc.append(NoEscape(r' \LaTeX.'))
    
    os.makedirs('output', exist_ok=True)
    doc.generate_pdf('output/docs', clean_tex=False)
    os.remove('output/docs.tex')
