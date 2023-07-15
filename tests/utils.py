from typing import Final, Callable, List

FILES_TO_TEST: Final = (
    # Core blocks
    ("h1", "core"),
    ("h2", "core"),
    # ("h3", "core"),
    ("definition", "core"),
    ("colorful-block", "core"),
    # Subject blocks
    ("katex-code", "subject"),
    ("katex-inline-code", "subject"),
)

FILENAME = (
    "clovis.html",
    "clovis-old.html",
    "tex.tex",
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
        f"tests/assets/study-sheet/block/{input_file}",
        f"tests/assets/study-sheet/block/{output_file}",
    )


def check_files(
    conversion_function: Callable[[str], str],
    input_name: str,
    output_name: str,
    folder_exclude_list: List[str],
) -> None:
    """Helper function to test several files using a conversion function."""
    for block, folder in FILES_TO_TEST:
        print(f"{folder}/{block}")

        if folder not in folder_exclude_list:
            input_file = f"{folder}/{block}/{input_name}"
            output_file = f"{folder}/{block}/{output_name}"

            check_conversion(conversion_function, input_file, output_file)


# todo(docs): better docstring
