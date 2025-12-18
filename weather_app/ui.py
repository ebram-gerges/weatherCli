class WeatherDisplay:
    """
    Handles how the weather is presented to the user.
    """

    # We use a dictionary to map "Text" to "Emoji"
    # This is a scalable way to handle icons
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
        # Quick fix for "Clear" vs "Sunny" based on API quirks
        if condition == "Clear" and is_day:
            return "☀️"
        return WeatherDisplay.ICONS.get(
            condition, "🌈"
        )  # Default to rainbow if unknown

    @staticmethod
    def display_report(report):
        """
        Takes a WeatherReport object and prints a pretty box.
        """
        emoji = WeatherDisplay.get_emoji(report.condition, report.is_day)

        # ASCII Box Design
        print("\n" + "=" * 30)
        print(f"  {report.city.upper()}")
        print("-" * 30)
        print(f"  {emoji}  {report.condition}")
        print(f"  🌡️   {report.temperature}°C")
        print("=" * 30 + "\n")
