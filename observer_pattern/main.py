from weather.weatherdata import WeatherData
from weather.display import CurrentConditionDisplay, StatisticsDisplay


weatherdata = WeatherData(70, 12, 13.3)
statisticsdisplay = StatisticsDisplay(weatherdata)
weatherdata.set_measurement(24, 45, 33.2)

currentcondition = CurrentConditionDisplay(weatherdata)
weatherdata.set_measurement(76, 42, 42.1)

weatherdata.delete_observer(statisticsdisplay)
weatherdata.set_measurement(0, 3, 0)
weatherdata.set_measurement(5, 8, 3.4)

weatherdata.add_observer(statisticsdisplay)
weatherdata.set_measurement(13, 8, 23.4)
