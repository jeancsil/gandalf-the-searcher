# Research phase

## What is the difference between a web crawler and a web scrapper

[Web Crawler](https://en.wikipedia.org/wiki/Web_crawler)  
[Web Scraper definition](https://en.wikipedia.org/wiki/Web_scraping)  
  
*source*: [Wikipedia](https://en.wikipedia.org/)

## Starting ideas

These ideas are in very early stages. There is not lots of knowledge of the area of web-scrapping or crawling, only the desire to build such a system and use my knowledge to make
the information searchable.

- The system must be distributed. For me, there is no point in building a software that runs on a single machine and can't scale up based on the need of speed or down based
on the need of cost saving.
- The languages to be used will depend heavily on what is the best for each part of the application.
- The modules, applications and/or microservices has to be dockerized.
This makes testing and deployment easier with k8s for production or multiple docker containers while developing to mimic distributed system in different servers.

## Terminology

In the industry, this is a solved problem. There are big companies such as [Google](https://google.com), [Bing](https://bing.com), [Duck Duck Go](https://duckduckgo.com) and
others that have built their own solutions to make their spiders and search engines.
Therefore, I'm going to create a list of terms and their definitions along the way so that I'm not inventing new names to existing things.

|Term |Definition  | Other info |
| --- | --- | --- |
|Web Crawler|One component of the scraper. It crawls the internet of a set of pages and marks/stores it for later data extraction (scrapping).||
|Web Scraper|Extracts the data of a given website.||
|URL Frontier|The component that stores URL's to be downloaded.|Link to more information about the URL Frontier|

## Possible components

`URL Frontier`: Give the links to the crawler. Has to take into consideration the politeness, URL prioritization, freshness and possibly more.  
`DNS Resolver (Cache)`: Caching the DNS resolution is useful because this process is going to happen over and over again.
`URL Filter`: To exclude certain mime-types that are not interesting to the whole process, such as JPG, AVI, etc...  
`Duplicate Finder`: Needs to find duplicate content with 2 or more different URL's. There is lots of ways to achieve that, one that seems promissing and doesn't take the full
document in consideration (small parts can change but it is still considered a duplicate) is: [SimHash](https://en.wikipedia.org/wiki/SimHash)

## References

### Building a scalable web-crawler with selenium

[Building a scalable web crawler with Selenium and Python](https://towardsdatascience.com/build-a-scalable-web-crawler-with-selenium-and-pyhton-9c0c23e3ebe5)  

As this project starts, I think the idea of using Selenium to render the webpages is very promising.  

The fact that many pages today are single page applications that only load their content as the user browsers the website or dynamically using Javascript makes the indexing
process error prone.  

Of course, to start with, it may be not a bad idea just to crawl and scrape the data I can get with `HTTP GET` request, but ranking will be better if considered the usability,
time to load completely and more.  

### System Design Interview

[Distributed web crawler to crawl Billions of web pages](https://www.youtube.com/watch?v=BKZxZwUgL3Y)  

[System Design Web Crawler](https://siddarthkanted.wordpress.com/2020/08/16/system-design-web-crawler/)
