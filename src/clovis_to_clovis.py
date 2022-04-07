"""
Used to convert old Clovis study sheet to the new format.
And later, may be used to validate study sheet?
"""

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


study_sheet_example = '''<div class="block toggle-h1" data-hide="h1-1">
                    <h1 class="title">Prologue : The Birth of a Sales System</h1>
                <div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div>
                <div class="block hide-h1-1" style="">
                    <p class="text">For example, do they think you’re a likable, trustworthy person, who is not only an expert in your field but also prides yourself on putting your customer’s needs first and making sure that if any problems arise you’ll be right there on the spot to resolve them?</p>
                </div>
                <div class="block hide-h1-1" style="">
                    <p class="text">Some text.</p>
                </div>
                <div class="block toggle-h1" data-hide="h1-2">
                    <h1 class="title">Cracking the code for sales and influence</h1>
                <div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div>
                <div class="block toggle-h1" data-hide="h1-3">
                    <h2 class="title">The Three Tens</h2>
                <div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div>
                <div class="block toggle-h1" data-hide="h1-4">
                    <h3 class="title">The product, idea, or concept</h3>
                <div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div>
                <div class="block toggle-h1" data-hide="h1-5">
                    <h4 class="title">The four elements of the not so straight line system</h4>
                <div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div>
                <div class="block hide-h1-5">
                    <p class="text">Complexity kills. It sucks the life out of developers, it makes products difficult to plan, build and test, it introduces security challenges, and it causes end-user and administrator frustration. (Ray Ozzie) In C++ it’s harder to shoot yourself in the foot, but when you do, you blow off your whole leg. (Bjarne Stroustrup) If debugging is the process of removing software bugs, then programming must be the process of putting them in. (Edsger Dijkstra) Measuring programming progress by lines of code is like measuring aircraft building progress by weight. (Bill Gates)
                    </p>
                </div>'''

parser.feed(study_sheet_example)
parser.doc += '\n'

