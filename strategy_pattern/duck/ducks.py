from .flybehaviors import FlyBehavior, FlyWithWings, FlyNoWay
from .quackbehaviors import QuackBehavior, Quack, Squeak, MuteQuack


class Duck():

    def __init__(self, flybehavior: FlyBehavior, quackbehavior: QuackBehavior):
        self._flybehavior = flybehavior
        self._quackbehavior = quackbehavior

    def __repr__(self):
        return f"I am a {self.__class__.__name__}"

    def perform_fly(self):
        return self._flybehavior.fly()

    @property
    def flybehavior(self):
        return self._flybehavior

    @flybehavior.setter
    def flybehavior(self, new_flybehavior: FlyBehavior):
        if isinstance(new_flybehavior, FlyBehavior):
            self._flybehavior = new_flybehavior
        else:
            raise TypeError("FlyBehavior is required while setting.")

    def perform_quack(self):
        return self._quackbehavior.quack()

    @property
    def quackbehavior(self):
        return self._quackbehavior

    @quackbehavior.setter
    def quackbehavior(self, new_quackbehavior: QuackBehavior):
        if isinstance(new_quackbehavior, QuackBehavior):
            self._quackbehavior = new_quackbehavior
        else:
            raise TypeError("QuackBehavior is required while setting.")


class MallarDuck(Duck):
    def __init__(
        self, flybehavior: FlyBehavior = FlyWithWings(),
        quackbehavior: QuackBehavior = Quack()
    ):
        super().__init__(flybehavior, quackbehavior)


class RobberDuck(Duck):
    def __init__(
        self, flybehavior: FlyBehavior = FlyNoWay(),
        quackbehavior: QuackBehavior = Squeak()
    ):
        super().__init__(flybehavior, quackbehavior)


class ModelDuck(Duck):
    def __init__(
        self, flybehavior: FlyBehavior = FlyNoWay(),
        quackbehavior: QuackBehavior = MuteQuack()
    ):
        super().__init__(flybehavior, quackbehavior)
