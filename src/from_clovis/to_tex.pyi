from html.parser import HTMLParser
from typing import Final

from src.common import rename_tags as rename_tags

DEBUG: bool
COLORFUL_BLOCKS: Final[tuple[str, ...]]
TAG_LIST: Final[tuple[str, ...]]
START_TAG: Final[dict[str, str]]
END_TAG: Final[dict[str, str]]
KATEX_MATHBB: Final[tuple[str, ...]]
KATEX_COMMANDS_TABLE: Final[dict[str, str]]
SYMBOLS_TABLE: Final[dict[str, str]]

def replace_symbols(text: str, inside_text: bool = ...) -> str: ...
def replace_katex_commands(text: str) -> str: ...
def escape_text(text: str) -> str: ...
def process_latex(latex: str) -> str: ...
def process_katex_inline_code(latex: str) -> str: ...

class MyHTMLParser(HTMLParser):
    doc: str
    inside_tag: dict[str, bool]
    def __init__(self) -> None: ...
    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None: ...
    def handle_endtag(self, tag: str) -> None: ...
    def handle_data(self, data: str) -> None: ...

def clovis_to_tex(clovis_input: str) -> str: ...
