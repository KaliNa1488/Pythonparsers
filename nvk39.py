import requests
from bs4 import BeautifulSoup

def parse():
	i = 1
	URL = 'http://nvk39.kiev.ua/'
	HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	items = soup.findAll(class_ = 'archive-post-wrap')
	news = []

	for item in items:
		news.append({
			'title':  item.find('a').text
				})

	for newse in news:
		print(i, newse['title'])
		i=i+1


parse()