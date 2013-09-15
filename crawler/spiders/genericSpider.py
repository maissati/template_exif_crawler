from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from crawler.items import CrawlerItem
from scrapy import signals
from scrapy import log

from scrapy.xlib.pydispatch import dispatcher
import requests
import utils.exif as Exif
import StringIO
import pprint
import utils.plugins as Plugins

class genericSpider(CrawlSpider):
    name = 'genericSpider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/site']

    rules = (
        Rule(SgmlLinkExtractor(
            #allow = ()
            #deny = ('\?tag=', '/tag/','/tags/', '/feed/', '/category/', '#comment', 'replytocom')
            ),
            callback='parse_item',
            follow=True),
        )

    def __init__(self, *a, **kw):
        super(genericSpider, self).__init__(*a, **kw)
        dispatcher.connect(self.post_process, signals.spider_closed)


    def post_process(self, spider):
        log.msg('Starting post_process function...', level=log.INFO)

    def CALLBACK_processImage(self, url, item):

        img = Plugins.pluginImageDownloader(url)
        stream = StringIO.StringIO(img)
        data = Exif.process_file(stream)

        if not data:
            log.msg('No EXIF data for %s' % url, level=log.DEBUG)
            item['exif'] = False
        else:
            log.msg('EXIF data for %s' % url, level=log.DEBUG)
            item['exif'] = True
        return item

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        items = []

        # extract urls from the src attribute of img tags
        # Example: <img src="http://url"> will extract http://url
        images = hxs.select('//img')
        for image in images:
            item = CrawlerItem()
            item['page'] = response.url
            item['picture'] = image.select('@src').extract()[0]
            item = self.CALLBACK_processImage(item['picture'], item)
            items.append(item)

        urls = hxs.select('//a')
        for url in urls:
            if url.select('img'):
                item = CrawlerItem()
                item['page'] = response.url
                item['picture'] = url.select('img/@src').extract()[0]
                item['picture_destination'] = url.select('@href').extract()[0]
                item = self.CALLBACK_processImage(item['picture_destination'], item)
                items.append(item)

        if len(items):
            log.msg('%s images were found.' % len(items), level=log.DEBUG)
        return items

