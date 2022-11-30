import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError, requests.Timeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("a.cs-overlay-link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("a.next.page-numbers::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author a.url.fn.n::text").get(),
        "comments_count": len(selector.css("ol.comment-list li").getall()),
        "summary": "".join(
            selector.css("div.entry-content > p:nth-of-type(1) *::text")
            .getall()).strip(),
        "tags": selector.css("a[rel=tag]::text").getall(),
        "category": selector.css("span.label::text").get()
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
