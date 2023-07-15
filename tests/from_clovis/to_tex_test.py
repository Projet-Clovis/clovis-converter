from typing import Final

from src.from_clovis.to_tex import clovis_to_tex


def _check_conversion(input_location: str, output_location: str) -> None:
    """Internal function."""
    with open(input_location) as file:
        content: str = file.read()

    with open(output_location) as file:
        expected_output: str = file.read()

    result = clovis_to_tex(content)

    assert result == expected_output


def check_conversion(block_name: str, directory: str = "core") -> None:
    _check_conversion(
        f"tests/assets/study-sheet/block/{directory}/{block_name}.html",
        f"tests/assets/study-sheet/block/{directory}/{block_name}.tex",
    )


FILES_TO_TEST: Final = [
    # Core blocks
    ("h1", "core"),
    ("h2", "core"),
    # ("h3", "core"),
    ("definition", "core"),
    ("colorful-block", "core"),
    # Subject blocks
    ("katex-code", "subject"),
    ("katex-inline-code", "subject"),
]


def test_files() -> None:
    for block, folder in FILES_TO_TEST:
        print(f"{folder}/{block}")
        check_conversion(block, folder)
