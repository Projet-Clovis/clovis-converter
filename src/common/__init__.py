## Functions
def remove_tags(soup, tags_class):
    tags = soup.find_all(class_=tags_class)

    for t in tags:
        t.decompose() # remove


def rename_tags(soup, tags_class, new_name='article'):
    tags = soup.find_all(class_=tags_class)

    for t in tags:
        t.name = new_name
