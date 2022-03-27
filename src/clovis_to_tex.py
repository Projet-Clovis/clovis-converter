from pylatex import Package, Document, Section, Subsection, Command
from pylatex.utils import bold, italic, NoEscape
from pylatex.basic import NewPage

from html.parser import HTMLParser

document = Document()

study_sheet_name = "Algorithmes d'Optimisation des Graphes"
author = "Licence 3"
date = "2021 - 2022"

document.preamble.append(Command('title', study_sheet_name))
document.preamble.append(Command('author', author))
document.preamble.append(Command('date', date))
document.preamble.append(Command('normalsize'))

document.append(Command('maketitle'))
document.append(Command('tableofcontents'))

document.append(NewPage())

doc = ''


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag, attrs)
        attrs = dict(attrs)

        if tag == 'h1':
            doc += r"\section{"
        elif tag == 'h2':
            doc += r"\subsection{"
        elif tag == 'h3':
            doc += r"\subsubsection{"
        elif tag == 'i':
            htmlStyle['italic'] = 1
        elif tag == 'u':
            htmlStyle['underline'] = 1
        elif tag == 'sup':
            htmlStyle['sup'] = 1
        elif tag == 'sub':
            htmlStyle['sub'] = 1
        elif tag == 'span':
            if attrs['class'] == 'f-code':
                htmlStyle['f-code'] = 1
            elif attrs['class'] == 'hl-yellow':
                htmlStyle['hl-yellow'] = 1


    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

        if tag == 'b':
            htmlStyle['bold'] = 0
        elif tag == 'i':
            htmlStyle['italic'] = 0
        elif tag == 'u':
            htmlStyle['underline'] = 0
        elif tag == 'sup':
            htmlStyle['sup'] = 0
        elif tag == 'sub':
            htmlStyle['sub'] = 0
        elif tag == 'span':
            htmlStyle['f-code'] = 0
            htmlStyle['hl-yellow'] = 0
            #todo : mettre une pile pour savoir la classe correspondante ?

            
    def handle_data(self, data):
        print("Encountered some data  :", data)

        run = p.add_run(data)

        if htmlStyle['bold']:
            run.bold = True

        if htmlStyle['italic']:
            run.italic = True

        if htmlStyle['underline']:
            run.underline = True

        if htmlStyle['sup']:
            run.font.superscript = True

        if htmlStyle['sub']:
            run.font.subscript = True

        if htmlStyle['hl-yellow']:
            run.font.highlight_color = WD_COLOR_INDEX.YELLOW

        if htmlStyle['f-code']:
            run.font.name = 'Courier New'
            run.font.highlight_color = WD_COLOR_INDEX.GRAY_25



parser = MyHTMLParser()
"""parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
"""



a = 'On ne peut pas faire une liste d\'<span class="f-code">int</span> car les listes acceptent uniquement les <b>Objets </b>et pas les <b>types primitifs</b>.<br>'
a = 'On ne peut pas faire une liste d\'<span class="f-code">int</span> car les listes acceptent uniquement les <b>Objets </b>et pas les <b>types primitifs</b>.<br><br>Marco je ne rigole pas avec la fonction e<sup>x</sup> surtout avec x<sub>0</sub> = <u>lmao</u>.<br>J\'espère que <i><b>fusionner </b></i>les <span class="f-code"><i><u><b>st<sup>y</sup>l<sub>e</sub>s</b></u></i></span> fera pas tout bug.<br>'

if a[-4:] == '<br>': # if the 4 last characters is a <br>, remove it
    a = a[:-4] # without the 4 last characters

b = a.split('<br>')

for i in range(len(b)-1): #
    parser.feed(b[i])
    p.add_run('\n')
parser.feed(b[-1]) # the last element (to not add a '\n' at the end)

#parser.feed(a)

import os
os.chdir('') #todo
document.generate_tex()
