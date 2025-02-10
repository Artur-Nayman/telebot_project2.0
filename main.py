# Import necessary classes from their respective modules
from bot.telegram_bot import TelegramBot
from db.database_manager import DatabaseManager
from scraper.xbox_scraper import XboxScraper

if __name__ == "__main__":
    # URL to scrape Xbox Game Pass subscription prices
    URL = "https://www.eneba.com/store/xbox-game-pass?drms[]=xbox&page=1&regions[]=emea&regions[]=europe&regions[]=finland&regions[]=global&text=game%20pass%20subscription&types[]=subscription"
    # Telegram bot token
    TOKEN = "6258928093:AAERQF1wZjvEaDTBeTlVQPGAQFC_lk1KADw"

    # Initialize the DatabaseManager with MySQL credentials
    db_manager = DatabaseManager("localhost", "3306", "root", "root", "artur_bot")
    scraper = XboxScraper(URL) # Initialize the XboxScraper with the URL to scrape
    bot = TelegramBot(TOKEN, db_manager, scraper) # Initialize the TelegramBot with the token, database manager, and scraper

    bot.run() # Run the bot