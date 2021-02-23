from .interface import Subject, Observer


class WeatherData(Subject):

    def __init__(self, temperature: float, humidity: float, pressure: float):
        self._observers = set()
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

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

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, arg: float):
        self._pressure = arg

    def add_observers(self, observer: Observer):
        observer.update(self.temperature, self.humidity, self.pressure)
        self._observers.add(observer)

    def delete_observers(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurement(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()
