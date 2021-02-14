from .flybehaviors import FlyBehavior, FlyWithWings, FlyNoWay
from .quackbehaviors import QuackBehavior, Quack, Squeak, MuteQuack


class Duck():

    def __init__(self, flybehavior: FlyBehavior, quackbehavior: QuackBehavior):
        self.flybehavior = flybehavior()
        self.quackbehavior = quackbehavior()

    def __repr__(self):
        return f"I am a {self.__class__.__name__}"

    def perform_fly(self):
        return self.flybehavior.fly()

    def set_fly_behavior(self, flybehavior: FlyBehavior):
        self.flybehavior = flybehavior()

    def perform_quack(self):
        return self.quackbehavior.quack()

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
        quackbehavior: QuackBehavior = Squeak
    ):
        super().__init__(flybehavior, quackbehavior)


class ModelDuck(Duck):
    def __init__(
        self, flybehavior: FlyBehavior = FlyNoWay,
        quackbehavior: QuackBehavior = MuteQuack
    ):
        super().__init__(flybehavior, quackbehavior)
