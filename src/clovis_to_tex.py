"""
Used to convert Clovis study sheet to LaTeX format.
"""

def clovis_to_tex(clovis_input):
    from bs4 import BeautifulSoup
    from html.parser import HTMLParser
    from common import remove_tags, rename_tags

    ## CONSTANTS
    COLORFUL_BLOCKS = ('definition', 'excerpt', 'quote', 'example', 'byheart',
                    'danger', 'summary', 'reminder', 'advice', 'remark')

    TAB = 4 * " "

    TAG_LIST = (
        'h1',
        'h2',
        'h3',
        'h4',

        'p',

        'quote',
        'quote-content',
        'quote-author',
        'quote-source',
        'quote-date',

        'definition-title',
        'definition-text',

        'b',
        'i',

        'hl-yellow',
        'f-code',

        'br',
    )

    START_TAG = {
        'h1': r'\section{',
        'h2': r'\subsection{',
        'h3': r'\subsubsection{',
        'h4': r'\paragraph{',

        'p': '',

        'quote': '',
        'quote-content': '',
        'quote-author': '',
        'quote-source': '',
        'quote-date': '',

        'definition-title': r'\clovisDefinition{',
        'definition-text': '',

        'b': r'\textbf{',
        'i': r'\textit{',

        'hl-yellow': r'\hlYellow{',
        'f-code': r'\inlineCode{',

        'br': r'\\',
    }

    END_TAG = {
        'h1': '}\n\n',
        'h2': '}\n\n',
        'h3': '}\n\n',
        'h4': '\\\\}\n\n',

        'p': '',

        'quote': '',
        'quote-content': '',
        'quote-author': '',
        'quote-source': '',
        'quote-date': '',

        'definition-title': '}{\n' + TAB,
        'definition-text': '\n}\n\n',

        'b': '}',
        'i': '}',

        'hl-yellow': '}',
        'f-code': '}',

        'br': r'\\', # just in case of KeyError in wrong input
    }


    study_sheet_name = "Study Sheet Name"
    author = "Study Sheet Author"
    date = r"\today"


    class MyHTMLParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.doc = ''


        def handle_starttag(self, tag, attrs):
            print("Encountered a start tag:", tag, attrs)
            attrs = dict(attrs)

            if tag in TAG_LIST:
                self.doc += START_TAG[tag]

            elif tag in COLORFUL_BLOCKS and tag != "definition":
                self.doc += r"\clovis" + tag.capitalize() + "{"


        def handle_endtag(self, tag):
            print("Encountered an end tag :", tag)

            if tag in TAG_LIST:
                self.doc += END_TAG[tag]

            elif tag == 'p':
                self.doc += r'\\' + "\n\n"

            elif tag in COLORFUL_BLOCKS: #todo: faire "if tag in COLORFUL-BLOCK
                self.doc += "}\n\n"


        def handle_data(self, data):
            print("Encountered some data  :", repr(data))

            if data.strip() != '':
                self.doc += data


    with open('../tests/assets/study-sheet/study-sheet-example.md') as file:
        study_sheet_example = file.readlines()

    # remove first and last line
    study_sheet_example.pop(0)
    study_sheet_example.pop()
    study_sheet_example = ''.join(study_sheet_example)

    ## Main
    soup = BeautifulSoup(clovis_input, 'html.parser')

    # Definition
    remove_tags(soup, '.cb-title-container')

    rename_tags(soup, '.definition-title', 'definition-title')
    rename_tags(soup, '.definition .text', 'definition-text')

    # Colorful-blocks
    for tag in COLORFUL_BLOCKS:
        rename_tags(soup, f'.{tag} .text', f'{tag}')

    parser = MyHTMLParser()

    parser.feed(str(soup))
    #parser.doc += r"\end{document}" + "\n"

    return parser.doc
