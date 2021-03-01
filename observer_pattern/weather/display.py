from .interface import Observer, DisplayElement
from .weatherdata import WeatherData


class CurrentConditionDisplay(Observer, DisplayElement):

    def __init__(self, weatherdata: WeatherData):
        self._temperature = None
        self._humidity = None
        self.weatherdata = weatherdata
        self.weatherdata.add_observers(self)

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

    def update(self):
        self.temperature = self.weatherdata.temperature
        self.humidity = self.weatherdata.humidity
        self.display()

    def display(self):
        print(
            f"Current condition: "
            f"{self.temperature} F degrees; "
            f"{self.humidity} humidity"
        )


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weatherdata: WeatherData):
        self._min_temperature = None
        self._max_temperature = None
        self._avg_temperature = None
        self._num_of_measurement = 0
        self.weatherdata = weatherdata
        self.weatherdata.add_observers(self)

    @property
    def temperature(self):
        return self._temperature

    def update(self):
        temp = self.weatherdata.temperature
        if self._num_of_measurement == 0:
            self._min_temperature = temp
            self._max_temperature = temp
            self._avg_temperature = temp
        else:
            self._min_temperature = min(self._min_temperature, temp)
            self._max_temperature = max(self._max_temperature, temp)
            self._avg_temperature = (
                (self._avg_temperature * self._num_of_measurement + temp) /
                (self._num_of_measurement + 1)
            )
        self._num_of_measurement += 1
        self.display()

    def display(self):
        print(
            "Min/Max/Avg: "
            f"{self._min_temperature: .2f}/"
            f"{self._max_temperature: .2f}/"
            f"{self._avg_temperature: .2f}"
        )
