## Functions
def remove_tags(soup, selector):
    tags = soup.select(selector)

    for t in tags:
        t.decompose() # remove


def rename_tags(soup, selector, new_name='article'):
    tags = soup.select(selector)

    for t in tags:
        t.name = new_name
