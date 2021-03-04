from .interface import Beverage


class DarkRoast(Beverage):
    def __init__(self):
        self._cost = 0.99
        self._description = self.__class__.__name__

    @property
    def cost(self):
        return self._cost

    @property
    def description(self):
        return self._description


class Espresso(Beverage):
    def __init__(self):
        self._cost = 1.99
        self._description = self.__class__.__name__

    @property
    def cost(self):
        return self._cost

    @property
    def description(self):
        return self._description


class HomeBlend(Beverage):
    def __init__(self):
        self._cost = 0.89
        self._description = self.__class__.__name__

    @property
    def cost(self):
        return self._cost

    @property
    def description(self):
        return self._description
