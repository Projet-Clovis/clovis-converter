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

    TAG_LIST = ('h1', 'h2', 'h3', 'h4', 'p', 'b', 'i', 'br')

    START_TAG = {
        'h1': '<h1 class="title">',
        'h2': '<h2 class="title">',
        'h3': '<h3 class="title">',
        'h4': '<h4 class="title">',

        'p': '<p class="text">',

        'quote': '<div class="quote-container">',
        'quote-content': '<p class="quote-content">',
        'quote-author': '<p class="quote-author">',
        'quote-source': '<p class="quote-source">',
        'quote-date': '<p class="quote-date">',

        'definition-title': '<p class="definition-title">',
        'definition-text': '<p class="text">',

        'b': '<b>',
        'i': '<i>',

        'br': '<br>',
    }

    END_TAG = {
        'h1': '</h1>\n',
        'h2': '</h2>\n',
        'h3': '</h3>\n',
        'h4': '</h4>\n',

        'p': '</p>\n',

        'quote': '</div>\n',
        'quote-content': '</p>\n',
        'quote-author': '</p>\n',
        'quote-source': '</p>',
        'quote-date': '</p>\n',

        'definition-title': '</p>\n',
        'definition-text': '</p>\n',

        'colorful-block': '</div>\n',

        'b': '</b>',
        'i': '</i>',

        'br': '<br>', # just in case of KeyError in wrong input
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


            elif tag == 'span':
                if 'class' in attrs:
                    if 'hl-yellow' in attrs['class']:
                        self.doc += '<span class="hl-yellow">'

                    elif 'f-code' in attrs['class']:
                        self.doc += '<span class="f-code">'

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


        def handle_data(self, data):
            print("Encountered some data  :", repr(data))

            if data.strip() != '':
                self.doc += data



    parser = MyHTMLParser()



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

