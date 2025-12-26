import os

import questionary
from dotenv import load_dotenv
from rich.console import Console

# 1. Load Env Vars FIRST
load_dotenv()

# 2. Imports
from tasks.controller import TaskController  # <--- Fixed Name (Singular)
from weather.api import WeatherClient
from weather.controller import WeatherController
from weather.storage import WeatherStorage
from weather.ui import WeatherDisplay

DatabaseManager = WeatherStorage

taskC = TaskController()
console = Console()
weatherC = WeatherController()

while True:
    console.clear()
    # 1. The Menu (Capitalized options)
    choice = questionary.select(
        "What do you want to do?", choices=["Check Weather", "Manage Tasks", "Exit"]
    ).ask()

    # 2. Check for EXACT string matches
    if choice == "Check Weather":
        while True:
            weatherC.run()
    elif choice == "Manage Tasks":
        while True:
            taskC.run()
            input("\nPress Enter to return to menu...")

    elif choice == "Exit":
        print("Bye :)")
        break
