from abc import ABCMeta  # , abstractmethod

from .flybehaviors import FlyBehavior, FlyWithWings, FlyNoWay
from .quackbehaviors import QuackBehavior, Quack, Squeak, MuteQuack


class Duck(metaclass=ABCMeta):

    def __init__(self, flybehavior: FlyBehavior, quackbehavior: QuackBehavior):
        self.flybehavior = flybehavior()
        self.quackbehavior = quackbehavior()

    # def __init__(self):
    #     pass

    def perform_fly(self):
        self.flybehavior.fly()

    def set_fly_behavior(self, flybehavior: FlyBehavior):
        self.flybehavior = flybehavior()

    def perform_quack(self):
        self.quackbehavior.quack()

    def set_quack_behavior(self, quackbehavior: QuackBehavior):
        self.quackbehavior = quackbehavior()


class MallarDuck(Duck):
    def __init__(
        self, flybehavior: FlyBehavior = FlyWithWings,
        quackbehavior: QuackBehavior = Quack
    ):
        super().__init__(flybehavior, quackbehavior)


class RobberDuck(Duck):
    def __init__(
        self, flybehavior: FlyBehavior = FlyNoWay,
        quackbehavior: QuackBehavior = MuteQuack
    ):
        super().__init__(flybehavior, quackbehavior)
