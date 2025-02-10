class BaseScraper:
    def __init__(self, url):
        self.url = url

    def get_prices(self):
        raise NotImplementedError("This method should be overridden in subclasses")
