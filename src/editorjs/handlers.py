import html
from typing import Any, Dict, List, Optional, Callable

from src.editorjs.utils import sanitize


def handle_paragraph(block: Dict[str, Any]) -> str:
    text = sanitize(block["data"].get("text", ""))
    return f"<p>{text}</p>"

def handle_header(block: Dict[str, Any]) -> str:
    level: int = block["data"].get("level", 1)
    text: str = sanitize(block["data"].get("text", ""))
    if level in (1, 2, 3):  # Ajoute 3 ici si besoin
        return f"<h{level}>{text}</h{level}>"
    return f"<p>{text}</p>"

def handle_list(block: Dict[str, Any]) -> str:
    tag: str = "ul" if block["data"].get("type") == "unordered" else "ol"
    items: List[str] = block["data"].get("items", [])
    list_items: str = "".join(f"<li>{sanitize(item)}</li>" for item in items)
    return f"<{tag}>{list_items}</{tag}>"

def handle_image(block: Dict[str, Any]) -> str:
    data: Dict[str, Any] = block.get("data", {})
    url: Optional[str] = data.get("file", {}).get("url")
    caption: str = html.escape(data.get("caption", ""))
    if url:
        return f'<figure><img src="{html.escape(url)}" alt="{caption}"/><figcaption>{caption}</figcaption></figure>'
    return ""

def handle_unknown(block: Dict[str, Any]) -> str:
    return f"<!-- Block type '{block['type']}' not supported -->"


HANDLER_DICT = {
    "paragraph": handle_paragraph,
    "header": handle_header,
    "list": handle_list,
    "image": handle_image,
    "unknown": handle_unknown,
}
