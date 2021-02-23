from abc import ABCMeta, abstractclassmethod


class Observer(metaclass=ABCMeta):

    @abstractclassmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass


class Subject(metaclass=ABCMeta):

    @abstractclassmethod
    def add_observers(self, observer: Observer):
        pass

    @abstractclassmethod
    def delete_observers(self, observer: Observer):
        pass

    @abstractclassmethod
    def notify_observers(self):
        pass


class DisplayElement(metaclass=ABCMeta):

    @abstractclassmethod
    def display(self):
        pass
