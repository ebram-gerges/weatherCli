import os
import time

import questionary
from dotenv import load_dotenv
from rich.console import Console
from weather.api import WeatherClient
from weather.storage import WeatherStorage
from weather.ui import WeatherDisplay

load_dotenv()
console = Console()
KEY = os.getenv("API_KEY")
URL = os.getenv("URL")

# Initialize Managers
weather_api = WeatherClient(KEY, URL)
weather_db = WeatherStorage()


class WeatherController:
    @staticmethod
    def run():
        # Clear screen isn't strictly necessary here if main.py handles it,
        # but it keeps the sub-menu clean.
        console.clear()

        weatherChoice = questionary.select(
            "Which service do you need?",
            choices=["Check Weather", "Search History", "Back"],
        ).ask()

        if weatherChoice == "Check Weather":
            city = questionary.text("Enter city name:").ask()

            if city:
                try:
                    with console.status(
                        "[bold green]Fetching weather report..."
                    ) as status:
                        report = weather_api.get_current_weather(city)
                        time.sleep(1)  # Just to show off the animation
                    # Use the new Panel display
                    WeatherDisplay.display_report(report)
                    weather_db.save_report(report)
                except Exception as e:
                    console.print(f"[bold red]Error: {e}[/]")

            input("\nPress Enter to return...")

        elif weatherChoice == "Search History":
            console.print("Fetching search history...")
            try:
                history = weather_db.get_history()
                # Use the new Table display logic
                WeatherDisplay.display_history(history)
            except Exception as e:
                console.print(f"[bold red]Error: {e}[/]")

            input("\nPress Enter to return...")

        elif weatherChoice == "Back":
            return  # Returns to the main menu loop
