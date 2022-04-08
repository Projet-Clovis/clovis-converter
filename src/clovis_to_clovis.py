"""
Used to convert old Clovis study sheet to the new format.
And later, may be used to validate study sheet?
"""

from bs4 import BeautifulSoup
from html.parser import HTMLParser

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

            elif 'h1' in attrs['class']:
                self.doc += '<h1 class="title">'
                self.stack.append('h1')

            elif 'h2' in attrs['class']:
                self.doc += '<h2 class="title">'
                self.stack.append('h2')

            elif 'h3' in attrs['class']:
                self.doc += '<h3 class="title">'
                self.stack.append('h3')

            elif 'h4' in attrs['class']:
                self.doc += '<h4 class="title">'
                self.stack.append('h4')

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
            self.doc += '</b>\n'
        elif tag == 'i':
            self.doc += '</i>\n'

        elif tag == 'section':
            self.doc += '</div>\n'


    def handle_data(self, data):
        print("Encountered some data  :", repr(data))

        if data.strip() != '':
            self.doc += data



parser = MyHTMLParser()


study_sheet_example = '''<div class="preview" id="main-content" style="padding-left: 25px;">
 <div class="container toggle-h1" data-hide="h1-1">
  <p class="title" contenteditable="false" data-count="I - " placeholder="Titre">
   Some h1
  </p>
  <div class="toggle-title-container">
  </div>
 </div>
 <div class="container toggle-h2 hide-h1-1" data-hide="h2-1">
  <p class="subtitle" contenteditable="false" data-count="A) " placeholder="Sous-titre">
   Some h2
  </p>
  <div class="toggle-title-container">
  </div>
 </div>
 <div class="container toggle-h3 hide-h1-1 hide-h2-1" data-hide="h3-1">
  <p class="subpart" contenteditable="false" data-count="a) " placeholder="Sous-partie">
   Some h3
  </p>
  <div class="toggle-title-container">
  </div>
 </div>
 <div class="container toggle-h4 hide-h1-1 hide-h2-1 hide-h3-1" data-hide="h4-1">
  <p class="subhead" contenteditable="false" data-count="1) " placeholder="Titre inférieur">
   Some h4
  </p>
  <div class="toggle-title-container">
  </div>
 </div>
 <div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1">
  <p class="text" contenteditable="false" placeholder="Entrez du texte">
   Some text
   <br/>
  </p>
 </div>
 <div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1">
  <p class="text" contenteditable="false" placeholder="Entrez du texte">
   Some
   <span class="hl-yellow">
    highlighted text
   </span>
   , some
   <b>
    bold text
   </b>
   , some
   <i>
    italic text
   </i>
   , some
   <i>
    <b>
     bold and italic
    </b>
   </i>
   , some
   <span class="hl-yellow">
    <b>
     bold and highlighted
    </b>
   </span>
   , some
   <span class="hl-yellow">
    <i>
     <b>
      bold, italic highlighted text
     </b>
    </i>
   </span>
   <i>
    <b>
    </b>
   </i>
   .
   <br/>
  </p>
 </div>
 <div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1">
  <p class="text" contenteditable="false" placeholder="Entrez du texte">
   Some
   <span class="f-code">
    inline code
   </span>
   .
   <br/>
  </p>
 </div>
 <div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1">
  <section class="colorful-block danger">
   <article class="cb-content">
    <p contenteditable="false" placeholder="Avertissement important">
     Some warning
     <br/>
    </p>
   </article>
  </section>
 </div>
 <div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1">
  <section class="colorful-block definition">
   <article class="cb-content">
    <p class="definition-title" contenteditable="false" placeholder="Mot défini">
     Some word
     <br/>
    </p>
    <p contenteditable="false" placeholder="Définition">
     Some definition
     <br/>
    </p>
   </article>
  </section>
 </div>
</div>'''


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
print(parser.doc)

