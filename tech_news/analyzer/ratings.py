from tech_news.database import get_collection, find_news
from tech_news.analyzer.helpers import categorize_list


# Requisito 10
def top_5_news():
    news_list = get_collection()

    result = (
        news_list.find({})
        .sort([("comments_count", -1), ("title", 1)])
        .limit(5)
    )

    return categorize_list(result)


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
