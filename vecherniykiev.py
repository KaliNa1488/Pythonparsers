import requests
from bs4 import BeautifulSoup

def parse():
	URL = 'https://vechirniy.kyiv.ua/news/today'
	HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	items = soup.findAll(class_ = 'col-xs-12 col-sm-6 col-md-3')
	news = []

	for item in items:
		news.append({
			'title':  item.find('a', class_ = 'topic-name').text
				})

	for newse in news:
		print(newse['title'])

parse()