from abc import ABCMeta, abstractmethod


class FlyBehavior(metaclass=ABCMeta):

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I am flying with wings!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I cannot fly!")
