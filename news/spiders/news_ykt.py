import re

import scrapy


class NewsYktSpider(scrapy.Spider):
    name = 'news_ykt'
    allowed_domains = ['news.ykt.ru']
    start_urls = ['http://news.ykt.ru/']

    def parse(self, response):
        links_to_follow = set()
        news_link = re.compile('/article/\d+')
        for link in response.css('a'):
            href = link.attrib['href']
            if news_link.match(href):
                pos = href.find('?')
                if pos > 0:
                    href = href[:pos]
                links_to_follow.add(href)

        for link in links_to_follow:
            yield response.follow(link, callback=self.parse_news)

    def parse_news(self, response):
        # print(vars(response.css('h1.n-post_title::text').get()))
        yield {
            'title': response.css('h1.n-post_title::text').get(),
        }
