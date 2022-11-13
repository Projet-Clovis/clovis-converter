from bs4 import BeautifulSoup, ResultSet, Tag


def remove_tags(soup: BeautifulSoup, selector: str) -> None:
    tags = soup.select(selector)

    for t in tags:
        t.decompose()  # remove


def rename_tags(soup: BeautifulSoup, selector: str, new_name: str = "article") -> None:
    tags: ResultSet[Tag] = soup.select(selector)

    for t in tags:
        t.name = new_name
