from src.from_clovis.to_tex import clovis_to_tex
from ..utils import check_files


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


def test_files():
    check_files(check_conversion)

