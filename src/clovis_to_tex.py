from html.parser import HTMLParser

study_sheet_name = "Study Sheet Name"
author = "Study Sheet Author"
date = r"\today"


doc = r'''
\documentclass{article}%
\usepackage[T1]{fontenc}%
\usepackage[utf8]{inputenc}%
\usepackage{lmodern}%
\usepackage{textcomp}%
\usepackage{lastpage}%
%
\usepackage{soul} % highlighting
\usepackage{inconsolata} % monospace font
\usepackage{fontawesome5}
%
\usepackage{xcolor}
\usepackage[framemethod=tikz]{mdframed}
\usepackage{tikzpagenodes}
\usetikzlibrary{calc}
%

% -------------------- Colors --------------------
\definecolor{definition}{HTML}{2f80ed}
\definecolor{definition-bg}{HTML}{e0ecfd}

\definecolor{danger-color}{HTML}{e6505f}
\definecolor{danger-bg-color}{HTML}{fce5e7}

\definecolor{code-bg-color}{HTML}{fcfcfc} % todo: temp color
\definecolor{code-border-color}{HTML}{dadce0} % todo: temp color

\definecolor{code-border-color}{HTML}{dadce0} % todo: temp color
FEF3C7


% -------------------- Macros --------------------
% highlight function
\newcommand{\highlight}[2]{%
    \begingroup
    \sethlcolor{#1}%
    \hl{#2}%
    \endgroup
}


% inlineCode (without border)
\newcommand{\inlineCodeWithoutBorder}[1]{%
    {\small\tt \highlight{code-bg-color}{#1}}%
}


% inlineCode (with border)
\usepackage[most]{tcolorbox}
\tcbset{
    on line,
    boxsep=2px,
    left=0pt,
    right=0pt,
    top=0pt,
    bottom=0pt,
    boxrule=0.5px,
    colframe=code-border-color,
    colback=code-bg-color,
    highlight math style={enhanced},
    breakable
}

\newcommand{\inlineCode}[1]{%
    \tcbox{{\small\tt #1}}%
}


% colorful-blocks
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
\title{Study Sheet Name}%
\author{Study Sheet Author}%
\date{\today}%
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
    def __init__(self):
        super().__init__()
        self.doc = ''


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
            #TODO
            self.doc += "\\" + colorful_block_class + "{"

        elif tag == 'span' and 'colorful-block' in attrs['class']:
            self.doc += r"\textit{"


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



parser = MyHTMLParser()


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

