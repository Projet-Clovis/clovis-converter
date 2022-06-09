from bs4 import BeautifulSoup, ResultSet  # type: ignore


def remove_tags(soup: BeautifulSoup, selector: str) -> None:
    tags = soup.select(selector)

    for t in tags:
        t.decompose()  # remove


def rename_tags(soup: BeautifulSoup, selector: str, new_name: str = "article") -> None:
    tags: ResultSet = soup.select(selector)

    for t in tags:
        t.name = new_name
