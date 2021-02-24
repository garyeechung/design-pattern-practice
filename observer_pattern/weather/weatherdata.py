from .interface import Subject, Observer


class WeatherData(Subject):

    def __init__(self, temperature: float, humidity: float, pressure: float):
        self._observers = set()
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self._changed = False

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

    @property
    def changed(self):
        return self._changed

    @changed.setter
    def changed(self, arg):
        self._changed = arg

    def add_observers(self, observer: Observer):
        observer.update()
        self._observers.add(observer)

    def delete_observers(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        if self.changed:
            for observer in self._observers:
                observer.update()
        self.changed = False

    def set_measurement(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.changed = True
        self.notify_observers()
