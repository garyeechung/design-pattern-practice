from .interface import Beverage, CondimentDecorator


class Mocha(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self._cost = 0.2


class Whip(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self._cost = 0.1


class Soy(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self._cost = 0.15
