from abc import ABCMeta, abstractmethod


class QuackBehavior(metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):

    def quack(self):
        return "quack"


class Squeak(QuackBehavior):
    def quack(self):
        return "squeak"


class MuteQuack(QuackBehavior):
    def quack(self):
        return "<<silence>>"
