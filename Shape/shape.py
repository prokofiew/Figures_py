from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, calculator):
        self.calculator = calculator

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}"
