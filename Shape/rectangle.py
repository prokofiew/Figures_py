from shape import Shape
from calculator_interface import CalculatorInterface


class Rectangle(Shape):
    def __init__(self, calculator: CalculatorInterface):
        super().__init__(calculator)
        self.side_a = float(input(f"Enter dimension of side_A of the {self}: "))
        self.side_b = float(input(f"Enter dimension of side_B of the {self}: "))
        self.area = self.calculator.area_calculator(self)
        self.perimeter = self.calculator.perimeter_calculator(self)

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter