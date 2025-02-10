from scraper.base_scraper import BaseScraper
import requests
from bs4 import BeautifulSoup as BS

# Define the XboxScraper class that inherits from BaseScraper
class XboxScraper(BaseScraper):
    def get_prices(self):
        r = requests.get(self.url) # Send a GET request to the URL
        site = BS(r.text, 'html.parser') # Parse the HTML content of the page

        games = [c.text for c in site.find_all('span', class_="YLosEL")] # Extract game titles from the parsed HTML
        prices = [float(c.text[1:]) for c in site.find_all('span', class_="L5ErLT")] # Extract prices from the parsed HTML and convert them to float

        return list(zip(games, prices)) # Return a list of tuples containing game titles and their prices
