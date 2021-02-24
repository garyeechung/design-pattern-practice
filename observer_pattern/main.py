from weather.weatherdata import WeatherData
from weather.display import CurrentConditionDisplay


weatherdata = WeatherData(70, 12, 13.3)
currentcondition = CurrentConditionDisplay(weatherdata)
weatherdata.set_measurement(123, 45, 33.2)
weatherdata.set_measurement(168, 42, 42.1)
