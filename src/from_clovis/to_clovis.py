"""
Used to convert old Clovis study sheet to the new format.
And later, may be used to validate study sheet?
"""
from typing import Final, Pattern

REMOVE_ENDING_BR_TAGS: Final = ("h1", "h2", "h3", "h4", "p", "article")
REMOVE_EMPTY_TAGS: Final = ("b", "i")
COLORFUL_BLOCKS = (
    "excerpt",
    "quote",
    "example",
    "byheart",
    "danger",
    "summary",
    "reminder",
    "advice",
    "remark",
)


def get_cb_start(cb: str) -> str:
    return f'<div class="cb-container {cb}">'


CB_START_DICT: Final = {cb: get_cb_start(cb) for cb in COLORFUL_BLOCKS}
CB_END_DICT: Final = {cb: "</div>" for cb in COLORFUL_BLOCKS}

TAG_LIST: Final = (
    "h1",
    "h2",
    "h3",
    "h4",
    "p",
    "quote",
    "quote-content",
    "quote-author",
    "quote-source",
    "quote-date",
    "definition-title",
    "definition-text",
    "b",
    "i",
    "sup",
    "sub",
    "hl-yellow",
    "f-code",
    "br",
    "katex-code",
    "katex-inline-code",
    *COLORFUL_BLOCKS,
)

START_TAG: Final = {
    "h1": '<h1 class="title">',
    "h2": '<h2 class="title">',
    "h3": '<h3 class="title">',
    "h4": '<h4 class="title">',
    "p": '<p class="text">',
    "quote": '<div class="quote-container">',
    "quote-content": '<p class="quote-content">',
    "quote-author": '<p class="quote-author">',
    "quote-source": '<p class="quote-source">',
    "quote-date": '<p class="quote-date">',
    "definition-title": '<div class="cb-container definition">'
                        '<p class="definition-title">',
    "definition-text": '<p class="text">',
    "b": "<b>",
    "i": "<i>",
    "sup": "<sup>",
    "sub": "<sub>",
    "hl-yellow": '<span class="hl-yellow">',
    "f-code": '<span class="f-code">',
    "br": "<br>",
    "katex-code": '<div class="katex-container"><p class="katex-code">',
    "katex-inline-code": '<div class="katex-container"><p '
                         'class="katex-inline-code">',
    **CB_START_DICT,
}

END_TAG: Final = {
    "h1": "</h1>",
    "h2": "</h2>",
    "h3": "</h3>",
    "h4": "</h4>",
    "p": "</p>",
    "quote": "</div>",
    "quote-content": "</p>",
    "quote-author": "</p>",
    "quote-source": "</p>",
    "quote-date": "</p>",
    "definition-title": "</p>",
    "definition-text": "</p></div>",
    "colorful-block": "</div>",
    "b": "</b>",
    "i": "</i>",
    "sup": "</sup>",
    "sub": "</sub>",
    "hl-yellow": "</span>",
    "f-code": "</span>",
    "br": "",  # just in case of KeyError in wrong input
    "katex-code": "</p></div>",
    "katex-inline-code": "</p></div>",
    **CB_END_DICT,
}

NON_SECABLE_SPACE = ("&amp;nbsp;", " ")


def clovis_to_clovis(clovis_input: str) -> str:
    from bs4 import BeautifulSoup
    from html.parser import HTMLParser
    from src.common import remove_tags, rename_tags
    import re

    class MyHTMLParser(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.doc = ""

        def handle_starttag(
                self, tag: str, attrs: list[tuple[str, str | None]]
        ) -> None:
            print("Encountered a start tag:", tag, attrs)

            if tag in TAG_LIST:
                self.doc += START_TAG[tag]
            elif tag == "colorful-block":
                self.doc += "</div>"

        def handle_endtag(self, tag: str) -> None:
            print("Encountered an end tag :", tag)

            if tag in TAG_LIST:
                self.doc += END_TAG[tag]
            elif tag == "colorful-block":
                self.doc += "</div>"

        def handle_data(self, data: str) -> None:
            print("Encountered some data  :", repr(data))

            if data.strip() != "":
                self.doc += data

    # Pre-processing the study-sheet
    soup = BeautifulSoup(clovis_input, "html.parser")

    remove_tags(soup, ".mini-title")
    remove_tags(soup, ".block-edit-button-container")
    remove_tags(soup, ".material-icons")

    rename_tags(soup, ".cb-content")

    # Headings
    rename_tags(soup, "p.title", "h1")
    rename_tags(soup, "p.subtitle", "h2")
    rename_tags(soup, "p.subpart", "h3")
    rename_tags(soup, "p.subhead", "h4")

    # Quote / Excerpts
    rename_tags(soup, ".quote", "quote")
    rename_tags(soup, ".quote-content", "quote-content")
    rename_tags(soup, ".ob-quote [placeholder='Auteur']", "quote-author")
    rename_tags(soup, ".ob-quote [placeholder='Source']", "quote-source")
    rename_tags(soup, ".ob-quote [placeholder='Date']", "quote-date")

    # Definition
    rename_tags(soup, ".definition-title", "definition-title")
    rename_tags(soup, ".definition p", "definition-text")

    # Colorful blocks
    for c in COLORFUL_BLOCKS:
        rename_tags(soup, f".{c}", c)

    # Inline styles
    rename_tags(soup, ".hl-yellow", "hl-yellow")
    rename_tags(soup, ".f-code", "f-code")

    # Nested inline styles
    # "ignore tag" does not exist and will therefore be ignored
    rename_tags(soup, "hl-yellow hl-yellow", "ignore")

    # Code
    remove_tags(soup, ".code-render")

    # Katex
    remove_tags(soup, ".katex-render")
    remove_tags(soup, ".katex-inline-render")

    rename_tags(soup, ".katex-code", "katex-code")
    rename_tags(soup, ".katex-inline-code", "katex-inline-code")

    # Special characters
    soup_text: str = str(soup)

    for space in NON_SECABLE_SPACE:
        soup_text = soup_text.replace(space, " ")

    # Parser
    parser: MyHTMLParser = MyHTMLParser()
    parser.feed(soup_text)

    for tag in REMOVE_ENDING_BR_TAGS:
        br_regex: str = f"(?P<variable>(<br>)*)</{tag}>"
        pattern: Pattern[str] = re.compile(br_regex)
        parser.doc = re.sub(pattern, f"</{tag}>", parser.doc)

    # remove empty span, b, i, ...
    # todo: another way of removing (smarter): checking if "text" content is empty
    # todo: like you would do in jQuery?
    for i in range(5):  # 5 times so it can replace nested empty tags
        for tag in REMOVE_EMPTY_TAGS:
            parser.doc = parser.doc.replace(f"<{tag}></{tag}>", "")

    return parser.doc
