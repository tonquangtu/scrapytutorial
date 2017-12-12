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
        print("tu ton")
        script_xpath = "/html/body/script/text()"
        recommended_symbol = '"recommendedSymbols":'
        script_list = response.xpath(script_xpath).extract()
        matched_script = next((script_text for script_text in script_list if recommended_symbol in script_text), None)

        if matched_script is None:
            return

        extracted_content = matched_script.split(recommended_symbol)[1].split('"options"')[0].split('[')[1].split(']')[0]
        extracted_content = '[' + extracted_content + ']'
        extracted_content_json = json.loads(extracted_content)
        tickers = [item['symbol'] for item in extracted_content_json]
        yield {"tickers": tickers}
        #
        # # print(content)
        # #
        # with open("matched.txt", 'w+') as f:
        #     f.write(matched_script)
