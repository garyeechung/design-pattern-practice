from abc import ABC, abstractclassmethod


class Observer(ABC):

    @abstractclassmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass


class DisplayElement(ABC):

    @abstractclassmethod
    def display(self):
        pass


class Subject(ABC):

    @abstractclassmethod
    def add_observer(self, observer: Observer):
        pass

    @abstractclassmethod
    def delete_observer(self, observer: Observer):
        pass

    @abstractclassmethod
    def notify_observers(self):
        pass
