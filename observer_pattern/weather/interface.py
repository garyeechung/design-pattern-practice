from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass


class DisplayElement(ABC):

    @abstractmethod
    def display(self):
        pass


class Subject(ABC):

    @abstractmethod
    def add_observer(self, observer: Observer):
        pass

    @abstractmethod
    def delete_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass
