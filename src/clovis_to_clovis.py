"""
Used to convert old Clovis study sheet to the new format.
And later, may be used to validate study sheet?
"""

def clovis_to_clovis(clovis_input):
    from bs4 import BeautifulSoup
    from html.parser import HTMLParser
    from common import remove_tags, rename_tags

    REMOVE_ENDING_BR_TAGS = ('h1', 'h2', 'h3', 'h4', 'p', 'article')
    REMOVE_EMPTY_TAGS = ('b', 'i')
    TAGS_LIST = ('h1', 'h2', 'h3', 'h4', 'p', 'b', 'i')
    COLORFUL_BLOCKS = ('definition', 'excerpt', 'quote', 'example', 'byheart',
                    'danger', 'summary', 'reminder', 'advice', 'remark')
    CLASS_LIST = ()

    TAG_LIST = ('h1', 'h2', 'h3', 'h4',)

    START_TAG = {
        'h1': '<h1 class="title">',
        'h2': '<h2 class="title">',
        'h3': '<h3 class="title">',
        'h4': '<h4 class="title">',
    }

    END_TAG = {
        'h1': '</h1>\n',
        'h2': '</h2>\n',
        'h3': '</h3>\n',
        'h4': '</h4>\n',
    }


    class MyHTMLParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.doc = ''

        def handle_starttag(self, tag, attrs):
            print("Encountered a start tag:", tag, attrs)
            attrs = dict(attrs)

            if tag in TAG_LIST:
                self.doc += START_TAG[tag]


            elif tag == 'p':
                self.doc += '<p class="text">'


            elif tag == 'span':
                if 'class' in attrs:
                    if 'hl-yellow' in attrs['class']:
                        self.doc += '<span class="hl-yellow">'

                    elif 'f-code' in attrs['class']:
                        self.doc += '<span class="f-code">'

            elif tag == 'b':
                self.doc += '<b>'
            elif tag == 'i':
                self.doc += '<i>'


            elif tag == 'br':
                self.doc += '<br>'


            elif tag == 'quote':
                self.doc += '<div class="quote-container">'

            elif tag == 'quote-content':
                self.doc += '<p class="quote-content">'

            elif tag == 'quote-author':
                self.doc += '<p class="quote-author">'

            elif tag == 'quote-source':
                self.doc += '<p class="quote-source">'

            elif tag == 'quote-date':
                self.doc += '<p class="quote-date">'


            elif tag == 'definition-title':
                self.doc += '<p class="definition-title">'
            elif tag == 'definition-text':
                self.doc += '<p class="text">'


            elif tag == 'colorful-block':
                colorful_block_class = attrs['class'].split()[-1]
                self.doc += f'''<div class="cb-container {colorful_block_class}">
        <div class="cb-title-container">
            <span class="cb-title-icon"></span>
            <span class="cb-title"></span>
        </div>
    '''


        def handle_endtag(self, tag):
            print("Encountered an end tag :", tag)

            if tag in TAG_LIST:
                self.doc += END_TAG[tag]


            elif tag == 'p':
                self.doc += '</p>\n'


            elif tag == 'span':
                self.doc += '</span>'

            elif tag == 'b':
                self.doc += '</b>'
            elif tag == 'i':
                self.doc += '</i>'


            elif tag == 'quote':
                self.doc += '</div>\n'

            elif tag == 'quote-content':
                self.doc += '</p>\n'

            elif tag == 'quote-author':
                self.doc += '</p>\n'

            elif tag == 'quote-source':
                self.doc += '</p>'

            elif tag == 'quote-date':
                self.doc += '</p>\n'


            elif tag == 'definition-title':
                self.doc += '</p>\n'

            elif tag == 'definition-text':
                self.doc += '</p>\n'


            elif tag == 'colorful-block':
                self.doc += '</div>\n'


        def handle_data(self, data):
            print("Encountered some data  :", repr(data))

            if data.strip() != '':
                self.doc += data



    parser = MyHTMLParser()


    study_sheet_example = '''<div id="main-content" class="preview" style="padding-left: 25px;">


                <div class="container toggle-h1" data-hide="h1-1"><p placeholder="Titre" class="title" data-count="I - " contenteditable="false">Some h1</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container toggle-h2 hide-h1-1" data-hide="h2-1" style=""><p placeholder="Sous-titre" class="subtitle" data-count="A) " contenteditable="false">Some h2</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container toggle-h3 hide-h1-1 hide-h2-1" data-hide="h3-1" style=""><p placeholder="Sous-partie" class="subpart" data-count="a) " contenteditable="false">Some h3</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container toggle-h4 hide-h1-1 hide-h2-1 hide-h3-1" data-hide="h4-1" style=""><p placeholder="Titre inférieur" class="subhead" data-count="1) " contenteditable="false">Some h4</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><p placeholder="Entrez du texte" class="text" contenteditable="false">Some text<br></p></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><p placeholder="Entrez du texte" class="text" contenteditable="false">Some <span class="hl-yellow">highlighted text</span>, some <b>bold text</b>, some <i>italic text</i>, some <i><b>bold and italic</b></i>, some <span class="hl-yellow"><b>bold and highlighted</b></span>, some <span class="hl-yellow"><i><b>bold, italic highlighted text</b></i></span><i><b></b></i>.<br></p></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><p placeholder="Entrez du texte" class="text" contenteditable="false">Some <span class="f-code">inline code</span>.<br></p></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><section class="colorful-block danger"><section class="cb-content"><article class="mini-title mt-danger">Attention</article><p placeholder="Avertissement important" contenteditable="false">Some warning<br></p></section></section></div>        <div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><section class="colorful-block definition"><section class="cb-content"><article class="mini-title mt-definition">Définition</article><p placeholder="Mot défini" class="definition-title" contenteditable="false">Some word<br></p><p placeholder="Définition" contenteditable="false">Some definition<br></p></section></section></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1"><div class="block-edit-button-container"></div><div class="block-edit-button-container"></div><div class="block-edit-button-container"></div><div class="block-edit-button-container"></div><div class="block-edit-button-container"></div><section class="colorful-block quote"><section class="cb-content"><section class="quote-container"><article class="quote-content" placeholder="Citation" contenteditable="false">This is a short citation<br></article></section><section class="optional-button-container ob-quote"><section class="optional-button ob-selected ob-selected-preview"><i class="material-icons optional-icon" style="display: none;">clear</i><article class="optional-text" placeholder="Auteur" contenteditable="false">John Doe<br></article></section><section class="optional-button ob-selected ob-selected-preview"><i class="material-icons optional-icon" style="display: none;">clear</i><article class="optional-text" placeholder="Source" contenteditable="false">The Book Written by Him<br></article></section><section class="optional-button ob-selected ob-selected-preview"><i class="material-icons optional-icon" style="display: none;">clear</i><article class="optional-text" placeholder="Date" contenteditable="false">1857</article></section></section></section></section></div>                </div>'''


    ## Pre-processing the study-sheet
    soup = BeautifulSoup(clovis_input, 'html.parser')

    remove_tags(soup, '.mini-title')
    remove_tags(soup, '.block-edit-button-container')
    remove_tags(soup, '.material-icons')

    rename_tags(soup, '.cb-content')

    # Headings
    rename_tags(soup, 'p.title', 'h1')
    rename_tags(soup, 'p.subtitle', 'h2')
    rename_tags(soup, 'p.subpart', 'h3')
    rename_tags(soup, 'p.subhead', 'h4')

    # Quote / Excerpts
    rename_tags(soup, '.quote', 'quote')
    rename_tags(soup, '.quote-content', 'quote-content')
    rename_tags(soup, '.ob-quote .ob-selected-preview:nth-child(1)', 'quote-author')
    rename_tags(soup, '.ob-quote .ob-selected-preview:nth-child(2)', 'quote-source')
    rename_tags(soup, '.ob-quote .ob-selected-preview:nth-child(3)', 'quote-date')

    # Definition
    rename_tags(soup, '.definition-title', 'definition-title')
    rename_tags(soup, '.definition p', 'definition-text')

    # Colorful blocks
    rename_tags(soup, '.colorful-block:not(.quote)', 'colorful-block')


    ## Parser
    parser.feed(str(soup))
    parser.doc += '\n'

    for tag in REMOVE_ENDING_BR_TAGS:
        parser.doc = parser.doc.replace(f'<br></{tag}>', f'</{tag}>')

    # remove empty span, b, i, ...
    for i in range(5): # 5 times so it can replace nested empty tags
        for tag in REMOVE_EMPTY_TAGS:
            parser.doc = parser.doc.replace(f'<{tag}></{tag}>', '')

    return parser.doc

