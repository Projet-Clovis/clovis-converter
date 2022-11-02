import mistune

md_example = '''
Some text.

Some **bold** text and also *italic*, even _**both**_.

# Some h1 title

## Some h2 title

### Some h3 title

#### Some h4 title

Some text, Clovis is the best.
'''


class MyRenderer(mistune.HTMLRenderer):
    def heading(self, text, level):
        return f'<h{level} class="title">{text}</h{level}>\n'

    def paragraph(self, text):
        return f'<p class="text">{text}</p>\n'

    def linebreak(self):
        return '<br>'

    def strong(self, text):
        return f'<b>{text}</b>'

    def emphasis(self, text):
        return f'<i>{text}</i>'


# use customized renderer
markdown = mistune.create_markdown(renderer=MyRenderer())
print(markdown(md_example))
