from weather.weatherdata import WeatherData
from weather.display import CurrentConditionDisplay


# if __name__ == "main":
weatherdata = WeatherData(70, 12, 13.3)
currentcondition = CurrentConditionDisplay(weatherdata)
weatherdata.set_measurement(123, 45, 33.2)
# print(currentcondition)
