# bot/telegram_bot.py
import telebot
from telebot import types

class TelegramBot:
    def __init__(self, token, db_manager, scraper):
        self.bot = telebot.TeleBot(token)
        self.db_manager = db_manager
        self.scraper = scraper
        self.filter_price = 0  # Minimum price filter
        self.setup_handlers()

    def setup_handlers(self):
        @self.bot.message_handler(commands=["start"])
        def start(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            project = types.KeyboardButton("Project")
            cv = types.KeyboardButton("CV")
            hub = types.KeyboardButton("GitHub")
            linked = types.KeyboardButton("LinkedIn")
            markup.add(project, cv, hub, linked)
            self.bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}!", reply_markup=markup)

        @self.bot.message_handler(func=lambda message: True)
        def handle_message(message):
            try:
                self.filter_price = float(message.text)   # If the message is a number, apply price filtering
                self.update_prices()
                games = self.db_manager.get_games()

                if not games:
                    self.bot.reply_to(message, "No games found with the specified price range.")
                    return

                for title, price in games:
                    self.bot.reply_to(message, f'Title: {title} \nPrice: {price}$')

            except ValueError:
                self.handle_text_message(message)

    def update_prices(self):
        self.db_manager.clear_xbox_table()
        games = self.scraper.get_prices()
        for title, price in games:
            if price <= self.filter_price:
                self.db_manager.insert_game(title, price)

    def handle_text_message(self, message):
        greetings = ["Hello", "Hi", "hello", "hi", "Good morning", "good morning", "Good afternoon", "Good evening"]
        tynks = ["ty", "Thank you", "Thanks", "Ty", "thank you", "thanks", "thx", "Thx", "THX", "Thy", "thy"]

        if message.text in greetings:
            self.bot.send_message(message.chat.id, "How can I help you?")
        elif message.text in tynks:
            self.bot.send_message(message.chat.id, "Always at your service.")
        elif message.text == "Project":
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton("Second Project", url="https://artur-nayman.github.io/Asiakasty-2022v2/"))
            self.bot.send_message(message.chat.id, "Here are my projects:", reply_markup=markup)
        elif message.text == "CV":
            chat_id = message.chat.id
            document_path = 'CV.pdf'
            with open(document_path, 'rb') as document:
                self.bot.send_document(chat_id, document)
        elif message.text == "GitHub":
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("GitHub", url="https://github.com/Artur-Nayman"))
            self.bot.send_message(message.chat.id, "Here is my GitHub page:", reply_markup=markup)
        elif message.text == "LinkedIn":
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton("LinkedIn", url="https://www.linkedin.com/in/artur-nayman-98ba12200/"))
            self.bot.send_message(message.chat.id, "Here is my LinkedIn profile:", reply_markup=markup)

    def run(self):
        self.bot.polling(none_stop=True)
