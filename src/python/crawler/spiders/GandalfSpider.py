import logging

import scrapy
import json
import os
import re


class GandalfSpider(scrapy.Spider):
    name = "gandalf-spider"

    def start_requests(self):
        urls = [
            'https://jeancsil.github.io/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        title = response.css('title::text').get()
        body = response.css('::text').getall()
        links = response.css('a::attr(href)').getall()

        url_folder = re.sub('[^0-9a-zA-Z]+', '_', response.url).strip("_")

        self.log("Changing {} into {}".format(response.url, url_folder), logging.DEBUG)

        crawled_data_dir = 'data/' + url_folder

        if not os.path.exists(crawled_data_dir):
            self.log(f'Creating dir {crawled_data_dir}')
            os.makedirs(crawled_data_dir)
        else:
            self.log(f'Dir {crawled_data_dir} already exists')

        page = response.url.split("/")[-2]
        filename = f'{crawled_data_dir}/{page}.json'
        data_in_json = {'title': title, 'body': body, 'links': links}

        self.log(data_in_json)
        with open(filename, 'w') as f:
            json.dump(data_in_json, f)
            #f.write(json.dumps(data_in_json))

        self.log(f'Saved file {filename}')

        yield from response.follow_all(links, callback=self.parse)
        # for link in all_links:
        #     next_page = response.urljoin(link)
        #     # yield scrapy.Request(next_page, callback=self.parse)
        #     yield response.follow(next_page, callback=self.parse)
