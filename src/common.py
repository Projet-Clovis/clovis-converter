from bs4 import BeautifulSoup, ResultSet, Tag


def remove_tags(soup: BeautifulSoup, selector: str) -> None:
    tags = soup.select(selector)

    for t in tags:
        t.decompose()  # remove


def rename_tags(soup: BeautifulSoup, selector: str, new_name: str = "article") -> None:
    """Rename the tag selected in selector.

    Example:
        If we have the tag `<p class="test">ok</p>`
        Running `rename_tags(soup, ".test", "new_p")`
        will turn the tag to `<new_p class="test">ok</new_p>`
    """
    tags: ResultSet[Tag] = soup.select(selector)

    for t in tags:
        t.name = new_name
