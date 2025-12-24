import requests
from weather.models import WeatherReport


class WeatherClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def get_current_weather(self, city):
        url = f"{self.base_url}/current.json?key={self.api_key}&q={city}"

        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"api Error: {response.status_code}")

        data = response.json()

        return WeatherReport.from_api_json(data)
