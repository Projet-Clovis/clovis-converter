from typing import Final, Callable

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


def check_files(check_conversion_function: Callable[[str, str], None]) -> None:
    """Helper function to test several files using a conversion function."""
    for block, folder in FILES_TO_TEST:
        print(f"{folder}/{block}")
        check_conversion_function(block, folder)
