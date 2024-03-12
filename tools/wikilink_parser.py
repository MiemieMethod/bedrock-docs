def wiki_url_builder(label="", base=r"/", end=r"/"):
    split_label = label.split(r"|")
    page_name = split_label[0]
    if len(split_label) > 1:
        label = split_label[1] if split_label[1] != "" else page_name
    else:
        label = page_name

    url = base + page_name + end

    return url
