import json
from typing import Any, Dict, List, Optional
import os

print(os.environ.get("PYTHONPATH"))

from src.editorjs.handlers import HANDLER_DICT, handle_unknown


class EditorJSConverter:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.data: Dict[str, Any] = data
        self.html_output: List[str] = []

    def convert(self) -> str:
        for block in self.data.get("blocks", []):
            handler = HANDLER_DICT.get(block['type'], handle_unknown)

            html_block: Optional[str] = handler(block)
            if html_block:
                self.html_output.append(html_block)
        return "\n".join(self.html_output)






# Exemple d'utilisation
if __name__ == "__main__":
    def load_editor_json(file_path: str) -> Dict[str, Any]:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    editor_data: Dict[str, Any] = load_editor_json("src/editorjs/temp.json")
    converter: EditorJSConverter = EditorJSConverter(editor_data)
    html_result: str = converter.convert()

    with open("src/editorjs/output.html", "w", encoding="utf-8") as f:
        f.write(html_result)

    print("✅ Conversion terminée. Fichier 'output.html' généré.")
