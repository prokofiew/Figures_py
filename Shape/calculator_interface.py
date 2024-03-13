from abc import ABC, abstractmethod


class CalculatorInterface(ABC):
    @abstractmethod
    def area_calculator(self, shape):
        pass

    @abstractmethod
    def perimeter_calculator(self, shape):
        pass
