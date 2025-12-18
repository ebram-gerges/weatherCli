import os

from dotenv import load_dotenv

from api import WeatherClient

load_dotenv()

KEY = os.getenv("API_KEY")
URL = os.getenv("URL")

client = WeatherClient(KEY, URL)


try:
    city = input("enter a city: ")
    report = client.get_current_weather(city)
    print(report)
except Exception as e:
    print(f"we got an error: {e}")
