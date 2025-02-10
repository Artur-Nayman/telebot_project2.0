class BaseScraper:
    def __init__(self, url):
        self.url = url # Initialize the scraper with a URL

    def get_prices(self):
        # This method should be overridden in subclasses to implement specific scraping logic
        raise NotImplementedError("This method should be overridden in subclasses")
