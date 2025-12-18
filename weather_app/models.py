class WeatherReport:
    """
    this class will give us the data we need to send to the ui
    it will return an object
    """

    def __init__(self, temperature, condition, city, is_day):
        self.temperature = temperature
        self.condition = condition
        self.city = city
        self.is_day = is_day

    #  Add a new method called from_api_json(cls, data_dict).

    # This method receives the raw dictionary from the API.

    # It extracts the values (e.g., temp = data_dict['current']['temp_c']).

    # Crucial: It returns cls(temp, ...) (which creates a new instance of itself).
    @classmethod
    def from_api_json(cls, data_dict):
        temperature = data_dict["current"]["temp_c"]
        condtion = data_dict["current"]["condition"]["text"]
        is_day = data_dict["current"]["is_day"] == 1
        city = data_dict["location"]["name"]
        # return the bluePrint of the request
        return cls(temperature, condtion, is_day, city)

    def __str__(self):
        return f"{self.city}: {self.temperature}°C ({self.condition}) {self.is_day}"
