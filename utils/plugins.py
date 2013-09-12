import requests

def pluginImageDownloader(url):
	return requests.get(url).content

