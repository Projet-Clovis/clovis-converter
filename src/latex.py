from pylatex import Document, Section, Subsection, Command
from pylatex.utils import bold, italic, NoEscape
from pylatex.basic import NewPage

import os

doc = Document()


study_sheet_name = "Algorithmes d'Optimisation des Graphes"
author = "Licence 3"
date = "2021 - 2022"

header = f"""\\title{{{study_sheet_name}}}
\\author{{{author}}}
\\date{{{date}}}
\\begin{{document}}
\\normalsize
\\maketitle
"""

doc.append(NoEscape(r'\tableofcontents'))
doc.append(NewPage())

with doc.create(Section('Le sujet')):
    pass

with doc.create(Subsection('Problématiques')):
    doc.append('Existe-t-il réellement un "moi-même", cette identité que je revendique ?')
    doc.append('\n\nSi elle existe, cette identité est-elle immuable ?')
    doc.append('\n\nEt est-elle nichée en moi ou n\'est-elle qu\'une apparence extérieure ?')
    doc.append('\n\nDéfinitions à connaître : éducation, alter ego, schizophrénie.')

with doc.create(Subsection('Le sujet selon Descartes')):
    doc.append('Descartes donne un définition universelle du sujet, valable pour tous les humains. Le seul élément indiscutable auquel il parvient est qu\'il est sûr de penser. Une autre certitude émerge : s\'il pense, c\'est qu\'il existe. Donc si la pensée existe, l\'entité qui l\'exprime existe aussi. Même si elle s\'illusionne sur ce qui fait le réel. Pour Descartes, le sujet est donc à l\'origine des pensées. ce sujet derrière la pensée est appelé sujet pensant ou être pensant. La métaphysique de Descartes repose sur le cogito ergo sum, c\'est-à-dire, "Je pense donc je suis".')

doc.generate_tex()
