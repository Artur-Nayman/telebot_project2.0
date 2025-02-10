# bot/telegram_bot.py
import telebot
from telebot import types

# Define the TelegramBot class to handle bot operations
class TelegramBot:
    def __init__(self, token, db_manager, scraper):
        # Initialize the Telegram bot with the provided token
        self.bot = telebot.TeleBot(token)
        # Initialize the Telegram bot with the provided token
        self.db_manager = db_manager
        self.scraper = scraper
        self.filter_price = 0 # Set a default minimum price filter
        self.setup_handlers() # Message handlers

    def setup_handlers(self):
        # Define a handler for the /start command
        @self.bot.message_handler(commands=["start"])
        def start(message):
            # Create keyboard with buttons for Project, CV, GitHub, and LinkedIn in Telegram chat interface
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            project = types.KeyboardButton("Project")
            cv = types.KeyboardButton("CV")
            hub = types.KeyboardButton("GitHub")
            linked = types.KeyboardButton("LinkedIn")
            markup.add(project, cv, hub, linked)
            # Send a welcome message with user name
            self.bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}!", reply_markup=markup)

        # Define a handler for all other messages
        @self.bot.message_handler(func=lambda message: True)
        def handle_message(message):
            try:
                self.filter_price = float(message.text)   # If the message is a number, apply price filtering
                self.update_prices()  # Update the prices in the database based on the filter
                games = self.db_manager.get_games() # Retrieve games from the database

                if not games:
                    # Send a message if no games are found with set price
                    self.bot.reply_to(message, "No games found with the specified price range.")
                    return

                for title, price in games:
                    # Send the game titles and prices to the user
                    self.bot.reply_to(message, f'Title: {title} \nPrice: {price}$')

            except ValueError:
                # Handle text messages separately
                self.handle_text_message(message)

    def update_prices(self):
        # Clear the existing games in db
        self.db_manager.clear_xbox_table()
        games = self.scraper.get_prices() # Get the latest game prices from the scraper
        for title, price in games: # Insert each game into the database if it meets the price filter criteria
            if price <= self.filter_price:
                self.db_manager.insert_game(title, price)

    def handle_text_message(self, message): # Lists of greetings and thanks messages
        greetings = ["Hello", "Hi", "hello", "hi", "Good morning", "good morning", "Good afternoon", "Good evening"]
        tynks = ["ty", "Thank you", "Thanks", "Ty", "thank you", "thanks", "thx", "Thx", "THX", "Thy", "thy"]
        # Responds to messages
        if message.text in greetings:
            self.bot.send_message(message.chat.id, "How can I help you?")
        elif message.text in tynks:
            self.bot.send_message(message.chat.id, "Always at your service.")
        elif message.text == "Project": #Project button
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton("Second Project", url="https://artur-nayman.github.io/Asiakasty-2022v2/"))
            self.bot.send_message(message.chat.id, "Here are my projects:", reply_markup=markup)
        elif message.text == "CV": #CV button
            chat_id = message.chat.id
            document_path = 'CV.pdf'
            with open(document_path, 'rb') as document:
                self.bot.send_document(chat_id, document)
        elif message.text == "GitHub": #GitHub button
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("GitHub", url="https://github.com/Artur-Nayman"))
            self.bot.send_message(message.chat.id, "Here is my GitHub page:", reply_markup=markup)
        elif message.text == "LinkedIn": #LinkedIn button
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton("LinkedIn", url="https://www.linkedin.com/in/artur-nayman-98ba12200/"))
            self.bot.send_message(message.chat.id, "Here is my LinkedIn profile:", reply_markup=markup)

    def run(self):# Start polling for new messages
        self.bot.polling(none_stop=True)
