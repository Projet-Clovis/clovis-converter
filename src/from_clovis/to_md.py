from html.parser import HTMLParser
from typing import Final


class MyHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.doc: str = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "h1":
            self.doc += "# "
        elif tag == "h2":
            self.doc += "## "
        elif tag == "h3":
            self.doc += "### "
        elif tag == "h4":
            self.doc += "#### "
        elif tag == "b":
            self.doc += "**"
        elif tag == "i":
            self.doc += "*"

    def handle_endtag(self, tag: str) -> None:
        print("Encountered an end tag :", tag)

        if tag == "h1":
            self.doc += "\n\n"
        elif tag == "h2":
            self.doc += "\n\n"
        elif tag == "h3":
            self.doc += "\n\n"
        elif tag == "h4":
            self.doc += "\n\n"
        elif tag == "b":
            self.doc += "**"
        elif tag == "i":
            self.doc += "*"
        elif tag == "p":
            self.doc += "  \n\n"

    def handle_data(self, data: str) -> None:
        print("Encountered some data  :", repr(data))

        if data.strip() != "":
            self.doc += data


parser = MyHTMLParser()

study_sheet_example: Final[str] = """<!-- Text -->
<p class="text">Some text.</p>

<!-- Formatted text --> <p class="text">Some <b>bold</b> text and also <i>italic</i>,
 even <b><i>both</i></b>.</p>

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
</div>"""

parser.feed(study_sheet_example)
parser.doc += "\n"
