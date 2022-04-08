"""
Used to convert old Clovis study sheet to the new format.
And later, may be used to validate study sheet?
"""

from bs4 import BeautifulSoup
from html.parser import HTMLParser

REMOVE_ENDING_BR_TAGS = ('h1', 'h2', 'h3', 'h4', 'p')
REMOVE_EMPTY_TAGS = ('b', 'i')
TAGS_LIST = ('h1', 'h2', 'h3', 'h4', 'p', 'b', 'i')
COLORFUL_BLOCKS = ('definition', 'excerpt', 'quote', 'example', 'byheart',
                'danger', 'summary', 'reminder', 'advice', 'remark')
CLASS_LIST = ()


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.doc = ''
        self.stack = []

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

        # p with class
        elif tag == 'p' and 'class' in attrs:
            if 'definition-title' in attrs['class']:
                self.doc += '<p class="definition-title">'
                self.stack.append('p')

            elif attrs['class'] == 'title':
                self.doc += '<h1 class="title">'
                self.stack.append('h1')

            elif 'subtitle' in attrs['class']:
                self.doc += '<h2 class="title">'
                self.stack.append('h2')

            elif 'subpart' in attrs['class']:
                self.doc += '<h3 class="title">'
                self.stack.append('h3')

            elif 'subhead' in attrs['class']:
                self.doc += '<h4 class="title">'
                self.stack.append('h4')

            elif 'text' in attrs['class']:
                self.doc += '<p class="text">'
                self.stack.append('p')

            else:
                self.stack.append('p')

        elif tag == 'p':
            self.doc += '<p class="text">'
            self.stack.append('p')

        elif tag == 'b':
            self.doc += '<b>'
        elif tag == 'i':
            self.doc += '<i>'

        elif tag == 'br':
            self.doc += '<br>'

        elif tag == 'section' and 'colorful-block' in attrs['class']:
            colorful_block_class = attrs['class'].split()[-1]
            self.doc += f'''<div class="cb-container {colorful_block_class}">
    <div class="cb-title-container">
        <span class="cb-title-icon"></span>
        <span class="cb-title"></span>
    </div>
'''


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
            matching_tag = self.stack.pop()
            self.doc += f'</{matching_tag}>\n'

        elif tag == 'b':
            self.doc += '</b>'
        elif tag == 'i':
            self.doc += '</i>'

        elif tag == 'section':
            self.doc += '</div>\n'


    def handle_data(self, data):
        print("Encountered some data  :", repr(data))

        if data.strip() != '':
            self.doc += data



parser = MyHTMLParser()


study_sheet_example = '''<div id="main-content" class="preview" style="padding-left: 25px;">


            <div class="container toggle-h1" data-hide="h1-1"><p placeholder="Titre" class="title" data-count="I - " contenteditable="false">Some h1</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container toggle-h2 hide-h1-1" data-hide="h2-1" style=""><p placeholder="Sous-titre" class="subtitle" data-count="A) " contenteditable="false">Some h2</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container toggle-h3 hide-h1-1 hide-h2-1" data-hide="h3-1" style=""><p placeholder="Sous-partie" class="subpart" data-count="a) " contenteditable="false">Some h3</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container toggle-h4 hide-h1-1 hide-h2-1 hide-h3-1" data-hide="h4-1" style=""><p placeholder="Titre inférieur" class="subhead" data-count="1) " contenteditable="false">Some h4</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><p placeholder="Entrez du texte" class="text" contenteditable="false">Some text<br></p></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><p placeholder="Entrez du texte" class="text" contenteditable="false">Some <span class="hl-yellow">highlighted text</span>, some <b>bold text</b>, some <i>italic text</i>, some <i><b>bold and italic</b></i>, some <span class="hl-yellow"><b>bold and highlighted</b></span>, some <span class="hl-yellow"><i><b>bold, italic highlighted text</b></i></span><i><b></b></i>.<br></p></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><p placeholder="Entrez du texte" class="text" contenteditable="false">Some <span class="f-code">inline code</span>.<br></p></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><section class="colorful-block danger"><section class="cb-content"><article class="mini-title mt-danger">Attention</article><p placeholder="Avertissement important" contenteditable="false">Some warning<br></p></section></section></div>        <div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><section class="colorful-block definition"><section class="cb-content"><article class="mini-title mt-definition">Définition</article><p placeholder="Mot défini" class="definition-title" contenteditable="false">Some word<br></p><p placeholder="Définition" contenteditable="false">Some definition<br></p></section></section></div>                </div>'''


## Functions
def remove_tags(soup, tags_class):
    tags = soup.find_all(class_=tags_class)

    for t in tags:
        t.decompose() # remove


def rename_tags(soup, tags_class, new_name='article'):
    tags = soup.find_all(class_=tags_class)

    for t in tags:
        t.name = new_name


## Main
soup = BeautifulSoup(study_sheet_example, 'html.parser')

remove_tags(soup, 'mini-title')
remove_tags(soup, 'block-edit-button-container')
remove_tags(soup, 'material-icons')

rename_tags(soup, 'cb-content')

parser.feed(str(soup))
parser.doc += '\n'

for tag in REMOVE_ENDING_BR_TAGS:
    parser.doc = parser.doc.replace(f'<br></{tag}>', f'</{tag}>')

# remove empty span, b, i, ...
for i in range(5): # 5 times so it can replace nested empty tags
    for tag in REMOVE_EMPTY_TAGS:
        parser.doc = parser.doc.replace(f'<{tag}></{tag}>', '')

print(parser.doc)

