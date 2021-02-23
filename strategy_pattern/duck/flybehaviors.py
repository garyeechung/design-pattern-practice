from abc import ABCMeta, abstractmethod


class FlyBehavior(metaclass=ABCMeta):

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):

    def fly(self):
        return "I fly with wings"


class FlyNoWay(FlyBehavior):

    def fly(self):
        return "I cannot fly"


class FlyWithRocket(FlyBehavior):

    def fly(self):
        return "I fly with a rocket"
