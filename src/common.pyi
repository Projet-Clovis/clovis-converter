from bs4 import BeautifulSoup


def remove_tags(soup: BeautifulSoup, selector: str) -> None: ...


def rename_tags(
        soup: BeautifulSoup,
        selector: str,
        new_name: str = "article"
) -> None: ...
