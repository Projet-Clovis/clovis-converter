from src.from_clovis.to_clovis import clovis_to_clovis


def _check_conversion(input_location: str, output_location: str) -> None:
    """Internal function."""
    with open(input_location) as file:
        content: str = file.read()

    with open(output_location) as file:
        expected_output: str = file.read()

    result = clovis_to_clovis(content)

    assert result == expected_output


def check_conversion(block_name: str) -> None:
    _check_conversion(
        f"tests/assets/study-sheet/block/core/{block_name}-old.html",
        f"tests/assets/study-sheet/block/core/{block_name}.html",
    )


def test_h1() -> None:
    check_conversion("h1")


def test_definition() -> None:
    check_conversion("definition")


def test_colorful_block() -> None:
    # test for colorful-block danger
    check_conversion("colorful-block")
