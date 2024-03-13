from shape import Shape
from calculator_interface import CalculatorInterface


class Circle(Shape):
    def __init__(self, calculator: CalculatorInterface):
        super().__init__(calculator)
        self.radius = float(input(f"Enter radius of {self}: "))
        self.area = self.calculator.area_calculator(self)
        self.perimeter = self.calculator.perimeter_calculator(self)

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter
