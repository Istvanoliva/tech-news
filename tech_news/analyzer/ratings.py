from tech_news.database import get_collection
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
    pass
