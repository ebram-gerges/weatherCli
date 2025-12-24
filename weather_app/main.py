import os
import time

import questionary
from dotenv import load_dotenv

load_dotenv()
from database import init_db
from tasks.storage import TasksStorage
from weather.api import WeatherClient
from weather.storage import WeatherStorage
from weather.ui import WeatherDisplay

DatabaseManager = WeatherStorage

init_db()
# env variables
KEY = os.getenv("API_KEY")
URL = os.getenv("URL")

# db init
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
db_url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
weather_api = WeatherClient(KEY, URL)
task_db = TasksStorage()
weather_db = WeatherStorage()


# ... setup code ...

while True:
    # 1. The Menu (Capitalized options)
    choice = questionary.select(
        "What do you want to do?", choices=["Check Weather", "Manage Tasks", "Exit"]
    ).ask()

    # 2. Check for EXACT string matches
    if choice == "Check Weather":
        weatherChoice = questionary.select(
            "which serves u need", choices=["Check Weather", "Search History", "Back"]
        ).ask()

        if weatherChoice == "Check Weather":
            city = questionary.text("enter city name: ").ask()

            if city:
                print(f"fetching weather for {city}")

                try:
                    report = weather_api.get_current_weather(city)
                    WeatherDisplay.display_report(report)
                    weather_db.save_report(report)
                except Exception as e:
                    print(f"error {e}")

        elif weatherChoice == "Search History":
            print("getting search history....")
            try:
                history = weather_db.get_history()
                print("\n----History----")
                for item in history:
                    pDate = item.searched_at.strftime("%y-%m-%d %H:%M")
                    print(f"• {item.city}: {item.temperature}\n {pDate}")
            except Exception as e:
                print(f"error {e}")

        elif weatherChoice == "exit":
            break
        # Add your weather logic here later
        input("\nPress Enter to return to menu...")

    elif choice == "Manage Tasks":
        print("Managing tasks...")
        # Add your task logic here later
        input("\nPress Enter to return to menu...")

    elif choice == "Exit":
        print("Bye :)")
        break

    else:
        # This shouldn't happen with questionary, but just in case
        print(f"Unknown command: {choice}")
        input("\nPress Enter to continue...")
