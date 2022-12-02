from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_list = find_news()

    top_5_news = sorted(
        news_list, key=lambda news: (-news["comments_count"], news["title"]))

    return [(news["title"], news["url"]) for news in top_5_news[:5]]


# Requisito 11
def top_5_categories():
    news_list = find_news()
    categories_list = [news["category"] for news in news_list]
    categories = dict()

    for category in categories_list:
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    sorted_categories = sorted(
        categories,
        key=lambda category: (-categories.get(category), category),
    )

    return sorted_categories[:5]
