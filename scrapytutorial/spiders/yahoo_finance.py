# -*- coding: utf-8 -*-
import scrapy
import json

class YahooFinance(scrapy.Spider):
    name = "yahoo_finance"
    start_urls = ["https://finance.yahoo.com/quote/AAPL/",
                  "https://finance.yahoo.com/quote/GOOG/",
                  "https://finance.yahoo.com/quote/AMZN/",
                  "https://finance.yahoo.com/quote/TSLA/",
                  "https://finance.yahoo.com/quote/FB/",
                  "https://finance.yahoo.com/quote/NFLX/",
                  "https://finance.yahoo.com/quote/BABA",
                  "https://finance.yahoo.com/quote/TWTR",
                  "https://finance.yahoo.com/quote/TWTR",
                  "https://finance.yahoo.com/quote/BIDU"]

    def parse(self, response):
        # all_link = response.xpath("//a").extract()

        # for link in all_link:
        #     yield {"link": link}
        # print(type(response.body))
        # filename = "yahoo.txt"

        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # yield response.body
        print("tu ton")
        js = response.xpath("/html/body/script[1]/text()").extract_first()
        script_file = "js.txt"
        list = js.split('"recommendedSymbols":')
        content = list[1].split('"options"')[0].split('[')[1].split(']')[0]
        content = '[' + content + ']'
        content = json.loads(content)

        content = [item['symbol'] for item in content]
        yield {"content": content}
        # print(content)
        #
        # with open(script_file, 'w+') as f:
        #     f.write(' '.join(content))
