from pylatex import Package, Document, Section, Subsection, Command
from pylatex.utils import bold, italic, NoEscape
from pylatex.basic import NewPage

from html.parser import HTMLParser

document = Document()

study_sheet_name = "Algorithmes d'Optimisation des Graphes"
author = "Licence 3"
date = "2021 - 2022"

document.preamble.append(Command('title', study_sheet_name))
document.preamble.append(Command('author', author))
document.preamble.append(Command('date', date))
document.preamble.append(Command('normalsize'))

document.append(Command('maketitle'))
document.append(Command('tableofcontents'))

document.append(NewPage())

doc = r'''
\documentclass{article}%
\usepackage[T1]{fontenc}%
\usepackage[utf8]{inputenc}%
\usepackage{lmodern}%
\usepackage{textcomp}%
\usepackage{lastpage}%
%
\title{Algorithmes d'Optimisation des Graphes}%
\author{Licence 3}%
\date{2021 {-} 2022}%
\normalsize%
%
\setcounter{tocdepth}{4}
\setcounter{secnumdepth}{4}
%
\begin{document}%
\normalsize%
\maketitle%
\tableofcontents%
\newpage%
'''


class MyHTMLParser(HTMLParser):
    def __init__(self, latex_document):
        super().__init__()
        self.doc = latex_document

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag, attrs)
        attrs = dict(attrs)

        if tag == 'h1':
            self.doc += r"\section{"
        elif tag == 'h2':
            self.doc += r"\subsection{"
        elif tag == 'h3':
            self.doc += r"\subsubsection{"
        elif tag == 'b':
            self.doc += r"\textbf{"
        elif tag == 'i':
            self.doc += r"\textit{"


    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

        if tag == 'h1':
            self.doc += "}\n"
        elif tag == 'h2':
            self.doc += "}\n"
        elif tag == 'h3':
            self.doc += "}\n"
        elif tag == 'b':
            self.doc += "}"
        elif tag == 'i':
            self.doc += "}"
        elif tag == 'p':
            self.doc += r'\\'


    def handle_data(self, data):
        print("Encountered some data  :", data)

        self.doc += data



parser = MyHTMLParser(doc)
"""parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
"""



study_sheet_example = '''<!-- Text -->
<p class="text">Some text.</p>

<!-- Formatted text -->
<p class="text">Some <b>bold</b> text and also <i>italic</i>, even <b><i>both</i></b>.</p>

<!-- Title : h1 -->
<h1 class="title">Some h1 title</h1>

<!-- Title : h2 -->
<h2 class="title">Some h2 title</h2>

<!-- Title : h3 -->
<h3 class="title">Some h3 title</h3>

<!-- Title : h4 -->
<h4 class="title">Some h4 title</h4>

<!-- Colorful block : summary -->
<div class="cb-container summary">
    <div class="colorful-block">
        <div class="cb-title-container">
            <span class="cb-title-icon"></span>
            <span class="cb-title"></span>
        </div>
        <p class="text">Some text, Clovis is the best.</p>
    </div>
</div>'''

parser.feed(study_sheet_example)

