from shape import Shape
from calculator_interface import CalculatorInterface


class Triangle(Shape):
    def __init__(self, calculator: CalculatorInterface):
        super().__init__(calculator)
        self.base = float(input(f"Enter base dimension of {self}: "))
        self.height = float(input(f"Enter height of {self}: "))
        self.area = self.calculator.area_calculator(self)
        self.perimeter = self.calculator.perimeter_calculator(self)

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter
