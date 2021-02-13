from abc import ABCMeta, abstractmethod


class QuackBehavior(metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):

    def quack(self):
        print("quack quack")


class Squeak(QuackBehavior):
    def quack(self):
        print("squeak squeak")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< silence >>")
