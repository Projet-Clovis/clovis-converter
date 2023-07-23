from html.parser import HTMLParser
from src.common import remove_tags as remove_tags, rename_tags as rename_tags
from typing import Final

DEBUG: bool
REMOVE_ENDING_BR_TAGS: Final[tuple[str, ...]]
REMOVE_EMPTY_TAGS: Final[tuple[str, ...]]
COLORFUL_BLOCKS: Final[tuple[str, ...]]

def get_cb_start(cb: str) -> str: ...

CB_START_DICT: Final[dict[str, str]]
CB_END_DICT: Final[dict[str, str]]
TAG_LIST: Final[tuple[str, ...]]
START_TAG: Final[dict[str, str]]
END_TAG: Final[dict[str, str]]
NON_SECABLE_SPACE: Final[tuple[str, ...]]

class MyHTMLParser(HTMLParser):
    doc: str
    def __init__(self) -> None: ...
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None: ...
    def handle_endtag(self, tag: str) -> None: ...
    def handle_data(self, data: str) -> None: ...

def clovis_to_clovis(clovis_input: str) -> str: ...
