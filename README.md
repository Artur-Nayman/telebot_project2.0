# Telebot Project 2.0

## Description
Telebot Project 2.0 is a Telegram bot that retrieves Xbox Game Pass subscription prices from the Eneba website, stores this data in a MySQL database, and allows users to query game information via Telegram.

## Features
- Fetches real-time Xbox Game Pass subscription prices from Eneba.
- Stores data in a MySQL database.
- Displays price information via Telegram bot.
- Filters results based on price.
- Interactive menu with links to CV, GitHub, and LinkedIn.

## Technologies
- Python
- Telegram API (telebot)
- MySQL (mysql-connector-python)
- Web Scraping (requests, BeautifulSoup4)

## Installation & Setup

### 1. Clone the repository
```sh
git clone https://github.com/Artur-Nayman/telebot_project2.0.git
cd telebot_project2.0
```

### 2. Install dependencies
```sh
pip install -r requirements.txt
```

### 3. Database Setup
Create a database `artur_bot` and a table `xbox` with the following structure:
```sql
CREATE TABLE xbox (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Price FLOAT NOT NULL
);
```

### 4. Run the bot
Update the MySQL credentials in `main.py` and start the bot:
```sh
python main.py
```

## Project Structure
```
telebot_project2.0/
├── bot/
│   ├── telegram_bot.py
├── db/
│   ├── database_manager.py
├── scraper/
│   ├── xbox_scraper.py
├── main.py
├── requirements.txt
├── README.md
```

## Author
[Artur Nayman](https://github.com/Artur-Nayman)

