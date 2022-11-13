"""
Used to convert Clovis study sheet to LaTeX format.
"""
import re
from typing import Final

KATEX_MATHBB = ("N", "Z", "Q", "D", "R", "C")

# commands specific to Katex, not to Latex
KATEX_COMMANDS_TABLE: Final = {**{c: "mathbb{" + c + "}" for c in KATEX_MATHBB}}

SYMBOLS_TABLE: Final = {
    "⩽": "leqslant",
    "⩾": "geqslant",
    "≠": "neq",
    "≈": "approx",
    "⟼": "longmapsto",
    "⇔": "iff",
    "ϕ": "phi",
    "φ": "phi",
    "Φ": "Phi",
    "λ": "lambda",
    "Λ": "Lambda",
    "ω": "omega",
    "Ω": "Omega",
    "π": "pi",
    "ϖ": "pi",
    "Π": "Pi",
    "ℝ": "mathbb{R}",
    "⋅": "cdot",
}


def replace_symbols(text: str, inside_text: bool = False) -> str:
    if inside_text:
        for char in SYMBOLS_TABLE.keys():
            text = text.replace(char, f"$\\{SYMBOLS_TABLE[char]}$ ")
    else:
        for char in SYMBOLS_TABLE.keys():
            text = text.replace(char, f"\\{SYMBOLS_TABLE[char]} ")
    return text


def replace_katex_commands(text: str) -> str:
    """Replaces incompatible Katex commands with Latex ones."""
    for char in KATEX_COMMANDS_TABLE.keys():
        re.sub(f"\\\{char}$", f"\\\{KATEX_COMMANDS_TABLE[char]}", text)  # noqa: W605
        re.sub(f"\\\{char} ", f"\\\{KATEX_COMMANDS_TABLE[char]} ", text)  # noqa: W605

    return text


def escape_text(text: str) -> str:
    text = text.replace("~", r"\textasciitilde")
    text = text.replace("^", r"\textasciicircum")
    text = text.replace("\\", r"\textbackslash")

    for char in ("&", "%", "$", "#", "_", "{", "}"):
        text = text.replace(char, f"\\{char}")

    text = replace_symbols(text, True)
    text = text.replace(" :", " :")

    return text


def process_latex(latex: str) -> str:
    latex = replace_katex_commands(latex)
    latex = replace_symbols(latex)

    return latex


def process_katex_inline_code(latex: str) -> str:
    double_dollar_parts = latex.split("$$")

    for i in range(len(double_dollar_parts)):
        if i % 2 == 1:
            double_dollar_parts[i] = process_latex(double_dollar_parts[i])
        else:
            single_dollar_parts = double_dollar_parts[i].split("$")

            for j in range(len(single_dollar_parts)):
                if j % 2 == 1:
                    single_dollar_parts[j] = process_latex(single_dollar_parts[j])
                else:
                    single_dollar_parts[j] = escape_text(single_dollar_parts[j])

            double_dollar_parts[i] = "$".join(single_dollar_parts)

    return "$$".join(double_dollar_parts)


def clovis_to_tex(clovis_input: str) -> str:
    from bs4 import BeautifulSoup
    from html.parser import HTMLParser
    from common import rename_tags

    # CONSTANTS
    COLORFUL_BLOCKS: Final = (
        "definition",
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

    TAG_LIST = (
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
        "cb-text",
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
    )

    START_TAG: Final = {
        "h1": r"\section{",
        "h2": r"\subsection{",
        "h3": r"\subsubsection{",
        "h4": r"\paragraph{",
        "p": "",
        "quote": r"\clovisQuote{",
        "quote-content": "",
        "quote-author": "",
        "quote-source": "",
        "quote-date": "",
        "cb-text": "",
        "definition-title": r"\clovisDefinition{",
        "definition-text": "",
        "b": r"\textbf{",
        "i": r"\textit{",
        "sup": "$^{",
        "sub": "$_{",
        "hl-yellow": r"\hlYellow{",
        "f-code": r"\inlineCode{",
        "br": r"\\",
        "katex-code": r"\[",
        "katex-inline-code": "",
    }

    END_TAG: Final = {
        "h1": "}",
        "h2": "}",
        "h3": "}",
        "h4": r"}\mbox{}\vspace{8px}\\",
        "p": r"\\" + "",
        "quote": "",
        "quote-content": "}{",
        "quote-author": "}{",
        "quote-source": "}{",
        "quote-date": "}",
        "cb-text": "",
        "definition-title": "}{",
        "definition-text": "}",
        "b": "}",
        "i": "}",
        "sup": "}$",
        "sub": "}$",
        "hl-yellow": "}",
        "f-code": "}",
        "br": "",  # just in case of KeyError in wrong input
        "katex-code": r"\]",
        "katex-inline-code": r"\\",
    }

    class MyHTMLParser(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.doc = ""
            self.inside_tag = {"katex-inline-code": False}

        def handle_starttag(
            self, tag: str, attrs: list[tuple[str, str | None]]
        ) -> None:
            print("Encountered a start tag:", tag, attrs)

            if tag == "katex-inline-code":
                self.inside_tag["katex-inline-code"] = True

            if tag in COLORFUL_BLOCKS and tag != "definition":
                self.doc += r"\clovis" + tag.capitalize() + "{"

            elif tag in TAG_LIST:
                self.doc += START_TAG[tag]

        def handle_endtag(self, tag: str) -> None:
            print("Encountered an end tag :", tag)

            if tag == "katex-inline-code":
                self.inside_tag["katex-inline-code"] = False

            if tag in TAG_LIST:
                self.doc += END_TAG[tag]

            elif tag in COLORFUL_BLOCKS and tag != "definition":
                self.doc += "}"

        def handle_data(self, data: str) -> None:
            print(f"Encountered some data :\n\t{repr(data)}")

            if data.strip() != "" and self.inside_tag["katex-inline-code"]:
                self.doc += process_katex_inline_code(data)

            elif data.strip() != "":
                self.doc += escape_text(data)

    # Pre-processing the study-sheet
    soup = BeautifulSoup(clovis_input, "html.parser")

    # Definition
    rename_tags(soup, ".definition-title", "definition-title")
    rename_tags(soup, ".definition .text", "definition-text")

    # Quote / Excerpts
    rename_tags(soup, ".quote", "quote")
    rename_tags(soup, ".quote-content", "quote-content")
    rename_tags(soup, ".quote-author", "quote-author")
    rename_tags(soup, ".quote-source", "quote-source")
    rename_tags(soup, ".quote-date", "quote-date")

    # Colorful blocks
    rename_tags(soup, ".cb-container .text", "cb-text")

    # Definition
    rename_tags(soup, ".definition-title", "definition-title")
    rename_tags(soup, ".definition .text", "definition-text")

    # Inline styles
    rename_tags(soup, ".hl-yellow", "hl-yellow")
    rename_tags(soup, ".f-code", "f-code")

    # Colorful-blocks
    for tag in COLORFUL_BLOCKS:
        rename_tags(soup, f".{tag}", f"{tag}")

    # Katex
    rename_tags(soup, ".katex-code", "katex-code")
    rename_tags(soup, ".katex-inline-code", "katex-inline-code")

    # Special characters
    soup_text = str(soup)

    # Parser
    parser: MyHTMLParser = MyHTMLParser()
    parser.feed(soup_text)

    return parser.doc
