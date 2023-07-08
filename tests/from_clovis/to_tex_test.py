from src.from_clovis.to_tex import clovis_to_tex


def _check_conversion(input_location: str, output_location: str) -> None:
    """Internal function."""
    with open(input_location) as file:
        content: str = file.read()

    with open(output_location) as file:
        expected_output: str = file.read()

    result = clovis_to_tex(content)

    assert result == expected_output


def check_conversion(block_name: str, directory: str="core") -> None:
    _check_conversion(
        f"tests/assets/study-sheet/block/{directory}/{block_name}.html",
        f"tests/assets/study-sheet/block/{directory}/{block_name}.tex",
    )


def test_h1() -> None:
    check_conversion("h1")


def test_definition() -> None:
    check_conversion("definition")


def test_colorful_block() -> None:
    # test for colorful-block danger
    check_conversion("colorful-block")


def test_katex_code() -> None:
    check_conversion("katex-code", "subject")


def test_katex_inline_code() -> None:
    check_conversion("katex-inline-code", "subject")
