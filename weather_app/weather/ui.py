from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


class WeatherDisplay:
    """
    Handles how the weather is presented to the user.
    """

    ICONS = {
        "Sunny": "☀️",
        "Clear": "🌙",
        "Partly cloudy": "⛅",
        "Cloudy": "☁️",
        "Overcast": "☁️",
        "Mist": "🌫️",
        "Rain": "🌧️",
        "Snow": "❄️",
    }

    @staticmethod
    def get_emoji(condition, is_day):
        if condition == "Clear" and is_day:
            return "☀️"
        return WeatherDisplay.ICONS.get(condition, "🌈")

    @staticmethod
    def display_report(report):
        """
        Takes a WeatherReport object and prints a styled Rich Panel.
        """
        emoji = WeatherDisplay.get_emoji(report.condition, report.is_day)

        # Get current time for the card
        now = datetime.now().strftime("%H:%M")

        # 1. Build the content string
        # Added a footer with the time in warm ORANGE
        content = f"\n[size=20]{emoji}[/size]   [bold white]{report.condition}[/]\n\n"
        content += f"🌡️   [bold cyan]{report.temperature}°C[/]\n"
        content += f"[italic orange3]       at {now}[/]"  # <--- NEW WARM TIME

        # 2. Create the Panel
        weather_panel = Panel(
            content,
            title=f"[bold yellow]{report.city.upper()}[/]",
            subtitle="[dim]Current Weather[/]",
            expand=False,
            border_style="cyan",
            padding=(1, 4),
        )

        console.print(weather_panel)

    @staticmethod
    def display_history(history_list):
        """
        Prints the search history as a nice table.
        """
        if not history_list:
            console.print("[yellow]No search history found.[/]")
            return

        table = Table(title="Search History", border_style="magenta")

        table.add_column("City", style="bold yellow")
        table.add_column("Temperature", style="cyan")

        # CHANGED: 'dim white' -> 'orange3' (Warm Color)
        table.add_column("Time", style="orange3")

        for item in history_list:
            pretty_date = item.searched_at.strftime("%Y-%m-%d %H:%M")

            table.add_row(item.city, f"{item.temperature}°C", pretty_date)

        console.print(table)
