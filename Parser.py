import requests
from bs4 import BeautifulSoup as bs


class Parser_holidays:
	def __init__(self) -> None:
		self.URL = 'https://kakoysegodnyaprazdnik.ru'
		self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.686 YaBrowser/23.9.5.686 Yowser/2.5 Safari/537.36"}
		self.encoding = 'utf-8'

	def get_response(self):
		response = requests.get(self.URL, headers=self.headers)
		response.encoding = self.encoding

		return response

	def get_holidays(self) -> list[str]:
		html = bs(self.get_response().text, 'html.parser')

		data = html.find('div', 'listing_wr').find_all('span', {'itemprop':'text'})
		list_holidays = [i.text for i in data]

		return list_holidays
