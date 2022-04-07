from html.parser import HTMLParser

study_sheet_name = "Algorithmes d'Optimisation des Graphes"
author = "Licence 3"
date = "2021 - 2022"

doc = r'''
\documentclass{article}%
\usepackage[T1]{fontenc}%
\usepackage[utf8]{inputenc}%
\usepackage{lmodern}%
\usepackage{textcomp}%
\usepackage{lastpage}%
%
\usepackage{fontawesome5}
%
\usepackage{xcolor}
\usepackage[framemethod=tikz]{mdframed}
\usepackage{tikzpagenodes}
\usetikzlibrary{calc}
%

% -------------------- Couleurs --------------------
\definecolor{definition}{HTML}{2f80ed}
\definecolor{definition-bg}{HTML}{e0ecfd}

\definecolor{danger-color}{HTML}{e6505f}
\definecolor{danger-bg-color}{HTML}{fce5e7}



% -------------------- Macros --------------------
\mdfdefinestyle{definition-style}{%
  innertopmargin=10px,
  innerbottommargin=10px,
  linecolor=definition,
  backgroundcolor=definition-bg,
  roundcorner=4px
}
\newmdenv[style=definition-style]{definition}

\newcommand\clovisDefinition[2]{
    \begin{definition}
    { \scriptsize \textcolor{definition}{\faIcon{graduation-cap} \textbf{DEFINITION}}}
    \vspace{3px}
    \\ \underline{\textbf{#1}}
    \vspace{2.5px}
    \\ #2
    \end{definition}
}


% -------------------- Study Sheet --------------------
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
        elif tag == 'h4':
            self.doc += r"\paragraph{"

        elif tag == 'p' and 'definition-title' in attrs['class']:
            self.doc += ''

        elif tag == 'b':
            self.doc += r"\textbf{"
        elif tag == 'i':
            self.doc += r"\textit{"

        elif tag == 'section' and 'colorful-block' in attrs['class']:
            colorful_block_class = attrs['class'].split()[-1]
            colorful_block_class = colorful_block_class.capitalize()

                self.doc += "\\" + colorful_block_class + "{"


    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

        if tag == 'h1':
            self.doc += "}\n\n"
        elif tag == 'h2':
            self.doc += "}\n\n"
        elif tag == 'h3':
            self.doc += "}\n\n"
        elif tag == 'h4':
            self.doc += "}\n\n"
        elif tag == 'b':
            self.doc += "}"
        elif tag == 'i':
            self.doc += "}"
        elif tag == 'p':
            self.doc += r'\\' + "\n\n"


    def handle_data(self, data):
        print("Encountered some data  :", repr(data))

        if data.strip() != '':
            self.doc += data



parser = MyHTMLParser(doc)


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
parser.doc += r"\end{document}" + "\n"

