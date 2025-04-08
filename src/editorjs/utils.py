import html


def sanitize(text: str) -> str:
    return html.escape(text)
