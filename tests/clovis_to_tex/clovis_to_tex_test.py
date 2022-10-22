from src.clovis_to_tex import clovis_to_tex


def check_conversion(input_location: str, output_location: str) -> None:
    with open(input_location) as file:
        content: str = file.read()

    with open(output_location) as file:
        expected_output: str = file.read()

    result = clovis_to_tex(content)

    assert result == expected_output


def h1_test() -> None:
    check_conversion(
        "../assets/study-sheet/block/core/h1.html",
        "../assets/study-sheet/block/core/h1.tex",
    )


def definition_test() -> None:
    check_conversion(
        "../assets/study-sheet/block/core/definition.html",
        "../assets/study-sheet/block/core/definition.tex",
    )


def colorful_block_test() -> None:
    # test for colorful-block danger
    check_conversion(
        "../assets/study-sheet/block/core/colorful-block.html",
        "../assets/study-sheet/block/core/colorful-block.tex",
    )


def katex_code_test() -> None:
    check_conversion(
        "../assets/study-sheet/block/core/katex-code.html",
        "../assets/study-sheet/block/core/katex-code.tex",
    )


def katex_inline_code_test() -> None:
    check_conversion(
        "../assets/study-sheet/block/core/katex-inline-code.html",
        "../assets/study-sheet/block/core/katex-inline-code.tex",
    )
