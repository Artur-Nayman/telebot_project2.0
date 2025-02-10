from scraper.base_scraper import BaseScraper
import requests
from bs4 import BeautifulSoup as BS

class XboxScraper(BaseScraper):
    def get_prices(self):
        r = requests.get(self.url)
        site = BS(r.text, 'html.parser')

        games = [c.text for c in site.find_all('span', class_="YLosEL")]
        prices = [float(c.text[1:]) for c in site.find_all('span', class_="L5ErLT")]

        return list(zip(games, prices))
