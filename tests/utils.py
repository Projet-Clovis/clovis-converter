from typing import Callable, Final, List, Optional

CORE_BLOCKS: Final = ("h1", "h2", "h3", "text", "definition", "colorful-block")
SUBJECT_BLOCKS: Final = ("katex-code", "katex-inline-code")
INLINE_STYLE: Final = ("b", "i", "hl-yellow")

FILES_TO_TEST: Final = (
    *((block, "block/core") for block in CORE_BLOCKS),
    *((block, "block/subject") for block in SUBJECT_BLOCKS),
    *((inline, "inline-style") for inline in INLINE_STYLE),
)


def _check_conversion(
    conversion_function: Callable[[str], str],
    input_location: str,
    output_location: str,
) -> None:
    """Internal function."""
    with open(input_location) as file:
        content: str = file.read()

    with open(output_location) as file:
        expected_output: str = file.read()

    result = conversion_function(content)

    assert result == expected_output


def check_conversion(
    conversion_function: Callable[[str], str],
    input_file: str,
    output_file: str,
) -> None:
    _check_conversion(
        conversion_function,
        f"tests/assets/study-sheet/{input_file}",
        f"tests/assets/study-sheet/{output_file}",
    )


def check_files(
    conversion_function: Callable[[str], str],
    input_name: str,
    output_name: str,
    folder_exclude_list: Optional[List[str]] = None,
) -> None:
    """Helper function to test several files using a conversion function."""
    if folder_exclude_list is None:
        folder_exclude_list = []

    for block, folder in FILES_TO_TEST:
        if folder not in folder_exclude_list:
            print(f"{folder}/{block}")

            input_file = f"{folder}/{block}/{input_name}"
            output_file = f"{folder}/{block}/{output_name}"

            check_conversion(conversion_function, input_file, output_file)


# todo(docs): better docstring
