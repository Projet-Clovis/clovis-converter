from html.parser import HTMLParser


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


    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

        if tag == 'h1':
            self.doc += '</h1>'
        elif tag == 'h2':
            self.doc += '</h2>'
        elif tag == 'h3':
            self.doc += '</h3>'
        elif tag == 'h4':
            self.doc += '</h4>'
        elif tag == 'p':
            self.doc += '</p>'
        elif tag == 'b':
            self.doc += '</b>'
        elif tag == 'i':
            self.doc += '</i>'


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
parser.doc += '\n'

