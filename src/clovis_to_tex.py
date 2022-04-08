from bs4 import BeautifulSoup
from html.parser import HTMLParser
from common import remove_tags, rename_tags

## CONSTANTS
COLORFUL_BLOCKS = ('definition', 'excerpt', 'quote', 'example', 'byheart',
                'danger', 'summary', 'reminder', 'advice', 'remark')

TAB = 4 * " "



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

\definecolor{hl-yellow-color}{HTML}{fef3c7}



% -------------------- Macros --------------------
% highlight function
\newcommand{\highlight}[2]{%
    \begingroup
    \sethlcolor{#1}%
    \hl{#2}%
    \endgroup
}

\newcommand{\hlYellow}[1]{%
    \highlight{hl-yellow-color}{#1}%
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

        self.definition_active = False


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

        elif tag == 'definition-title':
            self.doc += r"\clovisDefinition{"

        elif tag in COLORFUL_BLOCKS and tag != "definition":
            self.doc += r"\clovis" + tag.capitalize() + "{"

        elif tag == 'b':
            self.doc += r"\textbf{"
        elif tag == 'i':
            self.doc += r"\textit{"

        elif tag == 'span' and 'class' in attrs:
            if 'hl-yellow' in attrs['class']:
                self.doc += r"\hlYellow{"
            if 'f-code' in attrs['class']:
                self.doc += r"\inlineCode{"


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

        elif tag == 'definition-title':
            self.doc += "}{\n" + TAB
        elif tag == 'definition':
            self.doc += "\n}\n\n"

        elif tag in COLORFUL_BLOCKS: #todo: faire "if tag in COLORFUL-BLOCK
            self.doc += "}\n\n"

        elif tag == 'span':
            self.doc += "}"


    def handle_data(self, data):
        print("Encountered some data  :", repr(data))

        if data.strip() != '':
            self.doc += data



study_sheet_example = '''<!-- Title : h1 -->
<h1 class="title">Some h1 title</h1>

<!-- Title : h2 -->
<h2 class="title">Some h2 title</h2>

<!-- Title : h3 -->
<h3 class="title">Some h3 title</h3>

<!-- Title : h4 -->
<h4 class="title">Some h4 title</h4>

<!-- Text -->
<p class="text">Some text.</p>

<!-- Formatted text -->
<p class="text">Some <b>bold</b> text and also <i>italic</i>, even <b><i>both</i></b>.</p>

<!-- Formatted text : even more -->
<p class="text">Some <span class="hl-yellow">highlighted text</span>, some <b>bold text</b>, some <i>italic text</i>, some <i><b>bold and italic</b></i>, some <span class="hl-yellow"><b>bold and highlighted</b></span>, some <span class="hl-yellow"><i><b>bold, italic highlighted text</b></i></span>.</p>

<!-- Inline code -->
<p class="text">Some <span class="f-code">inline code</span>.</p>

<!-- Colorful block : danger -->
<div class="cb-container danger">
    <div class="cb-title-container">
        <span class="cb-title-icon"></span>
        <span class="cb-title"></span>
    </div>
    <p class="text">Some warning</p>
</div>

<!-- Colorful block : definition -->
<div class="cb-container definition">
    <div class="cb-title-container">
        <span class="cb-title-icon"></span>
        <span class="cb-title"></span>
    </div>
    <p class="definition-title">Some word</p>
    <p class="text">Some definition</p>
</div>
'''

## Main
soup = BeautifulSoup(study_sheet_example, 'html.parser')

# Definition
remove_tags(soup, '.cb-title-container')

rename_tags(soup, '.definition-title', 'definition-title')
rename_tags(soup, '.definition .text', 'definition-text')

# Colorful-blocks
for tag in COLORFUL_BLOCKS:
    rename_tags(soup, f'.{tag} .text', f'{tag}')

parser = MyHTMLParser()

parser.feed(str(soup))
parser.doc += r"\end{document}" + "\n"

print(parser.doc)
