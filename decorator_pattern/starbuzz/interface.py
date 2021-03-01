from abc import ABC, abstractmethod


class Beverage(ABC):

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


class CondimentDecorator(Beverage):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        self._description = self.__class__.__name__
        self._cost = 0

    @property
    def cost(self):
        return self.beverage.cost + self._cost

    @property
    def description(self):
        return f"{self.beverage.description}, {self._description}"
