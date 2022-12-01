def categorize_list(list):
    return [(news["title"], news["url"]) for news in list]
