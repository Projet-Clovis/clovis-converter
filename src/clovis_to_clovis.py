"""
Used to convert old Clovis study sheet to the new format.
And later, may be used to validate study sheet?
"""

from html.parser import HTMLParser

TAGS_LIST = ('h1', 'h2', 'h3', 'h4', 'p', 'b', 'i')
CLASS_LIST = ()


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.doc = ''

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag, attrs)
        attrs = dict(attrs)

        if tag == 'h1':
            self.doc += '<h1 class="title">'
        elif tag == 'h2':
            self.doc += '<h2 class="title">'
        elif tag == 'h3':
            self.doc += '<h3 class="title">'
        elif tag == 'h4':
            self.doc += '<h4 class="title">'
        elif tag == 'p':
            self.doc += '<p class="text">'
        elif tag == 'b':
            self.doc += '<b>'
        elif tag == 'i':
            self.doc += '<i>'
        elif tag == 'br':
            self.doc += '<br>'


    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

        if tag == 'h1':
            self.doc += '</h1>\n'
        elif tag == 'h2':
            self.doc += '</h2>\n'
        elif tag == 'h3':
            self.doc += '</h3>\n'
        elif tag == 'h4':
            self.doc += '</h4>\n'
        elif tag == 'p':
            self.doc += '</p>\n'
        elif tag == 'b':
            self.doc += '</b>\n'
        elif tag == 'i':
            self.doc += '</i>\n'


    def handle_data(self, data):
        print("Encountered some data  :", repr(data))

        if data.strip() != '':
            self.doc += data



parser = MyHTMLParser()


study_sheet_example = '''
                    <div class="container"><div class="block-edit-button-container"></div><p placeholder="Titre" class="title" data-count="I - " contenteditable="false">Some h1</p></div><div class="container"><div class="block-edit-button-container"></div><p placeholder="Sous-titre" class="subtitle" data-count="A) " contenteditable="false">Some h2</p></div><div class="container"><div class="block-edit-button-container"></div><p placeholder="Sous-partie" class="subpart" data-count="a) " contenteditable="false">Some h3</p></div><div class="container"><div class="block-edit-button-container"></div><p placeholder="Titre inférieur" class="subhead" data-count="1) " contenteditable="false">Some h4</p></div><div class="container"><div class="block-edit-button-container"></div><p placeholder="Entrez du texte" class="text" contenteditable="false">Some text<br></p></div><div class="container"><div class="block-edit-button-container"></div><section class="colorful-block danger"><section class="cb-content"><article class="mini-title mt-danger">Attention</article><p placeholder="Avertissement important" contenteditable="false">Some warning<br></p></section></section></div>'''

parser.feed(study_sheet_example)
parser.doc += '\n'

