# from abc import ABCMeta, abstractmethod

from .flybehaviors import FlyBehavior, FlyWithWings


class Duck():

    def __init__(self, flybehavior: FlyBehavior):
        self.flybehavior = flybehavior()

    def perform_fly(self):
        self.flybehavior.fly()

    def set_fly_behavior(self, flybehavior: FlyBehavior):
        self.flybehavior = flybehavior()


class MallarDuck(Duck):
    def __init__(self, flybehavior: FlyBehavior = FlyWithWings):
        self.flybehavior = flybehavior()
