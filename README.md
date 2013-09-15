Scrapy EXIF Crawler
=========

Scrapy EXIF Crawler is a python template which uses [The Scrapy Framework](http://scrapy.org) to automatically crawl all pages from a given URL and extract EXIF information from any scraped picture. 

The EXIF parser used in this project is a slightly modified version of [Gene Cash and Ianaré Sévi](https://github.com/ianare/exif-py) project.


The project in general is part of the thesis of my diploma Msc. Computer Science (Univeristy of Kent) :
> Crawling the Internet for EXIF data and contextual mismatches.

Requirements
-----------

To be able to run the project, you will need:

* [Python v 2.6-2.7.5] - version 2.7.5 is recommended (scrapy is not compatible python 3 !)
* [Scrapy v 1.6.5] - The project has been tested only with this version. It might be compatible with newer versions


Installation
--------------

No installation, just extract the folder where you want =)


For the developers
-----------

This is just a template. All it does is extract all exif information from all web pages.
The crawling operation is based on the ```allowed_domains``` and ```starts_urls``` in the file "crawler/spiders/genericSpider.py"

*Note: check [Scrapy Documentation](http://doc.scrapy.org/en/0.16/) for all settings and customization.*

Use
----------

Edit the file "crawler/spiders/genericSpider.py" and change the value of the variables:

```python
    allowed_domains = ['www.domain.net']
    start_urls = ['http://www.domain.net/site']
```

You can also edit the file crawler/settings.py for scrapy settings.

When you are ready, just run one of the following command:
```sh
  scrapy crawl genericSpider
  scrapy crawl genericSpider -o dump/full.json -t json #this will output the results
```

License
-
MIT

*Mohamed Amine AISSATI - https://github.com/maissati*
