import os

from api import WeatherClient
from dotenv import load_dotenv
from storage import DatabaseManager
from ui import WeatherDisplay

load_dotenv()
# env variables
KEY = os.getenv("API_KEY")
URL = os.getenv("URL")

# db init
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
db_url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
client = WeatherClient(KEY, URL)
db_manager = DatabaseManager(db_url)

try:
    city = input("enter a city: ")
    if city == "exit":
        exit
    else:
        report = client.get_current_weather(city)
        WeatherDisplay.display_report(report)
        db_manager.save_report(report)

except Exception as e:
    print(f"we got an error: {e}")
