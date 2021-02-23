from .interface import Observer, DisplayElement
from .weatherdata import WeatherData


class CurrentConditionDisplay(Observer, DisplayElement):

    def __init__(self, weatherdata: WeatherData):
        self._temperature = None
        self._humidity = None
        self._weatherdata = weatherdata
        self._weatherdata.add_observers(self)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, arg: float):
        self._temperature = arg

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, arg: float):
        self._humidity = arg

    def update(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(
            f"Current condition: "
            f"{self.temperature} F degrees; "
            f"{self.humidity} humidity"
        )
