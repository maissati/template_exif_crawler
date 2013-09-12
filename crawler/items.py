# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

# Add you own field intended to be stored
# For example: manufacturer, lens_model, time, etc
#
class CrawlerItem(Item):
	
	page = Field()
	picture = Field()
	picture_destination = Field()
	exif = Field()

