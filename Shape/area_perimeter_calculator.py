from calculator_interface import CalculatorInterface
from .square import Square
from .rectangle import Rectangle
from .triangle import Triangle
from .circle import Circle
import math


class AreaPerimeterCalculator(CalculatorInterface):

    @staticmethod
    def area_calculator(shape):
        if isinstance(shape, Square):
            return AreaPerimeterCalculator.calculate_square_area(shape)
        elif isinstance(shape, Rectangle):
            return AreaPerimeterCalculator.calculate_rectangle_area(shape)
        elif isinstance(shape, Triangle):
            return AreaPerimeterCalculator.calculate_triangle_area(shape)
        elif isinstance(shape, Circle):
            return AreaPerimeterCalculator.calculate_circle_area(shape)
        else:
            raise ValueError(f'Wrong shape: {shape}')

    @staticmethod
    def perimeter_calculator(shape):
        if isinstance(shape, Square):
            return AreaPerimeterCalculator.calculate_square_perimeter(shape)
        elif isinstance(shape, Rectangle):
            return AreaPerimeterCalculator.calculate_rectangle_perimeter(shape)
        elif isinstance(shape, Triangle):
            return AreaPerimeterCalculator.calculate_triangle_perimeter(shape)
        elif isinstance(shape, Circle):
            return AreaPerimeterCalculator.calculate_circle_perimeter(shape)
        else:
            raise ValueError(f'Wrong shape: {shape}')

    @staticmethod
    def calculate_square_area(square_shape):
        return square_shape.side_a ** 2

    @staticmethod
    def calculate_square_perimeter(square_shape):
        return square_shape.side_a * 4

    @staticmethod
    def calculate_rectangle_area(rectangle_shape):
        return rectangle_shape.side_a * rectangle_shape.side_b

    @staticmethod
    def calculate_rectangle_perimeter(rectangle_shape):
        return rectangle_shape.side_a * 2 + rectangle_shape.side_b * 2

    @staticmethod
    def calculate_circle_area(circle_shape):
        return pow(circle_shape.radius, 2) * math.pi

    @staticmethod
    def calculate_circle_perimeter(circle_shape):
        return 2 * math.pi * circle_shape.radius

    @staticmethod
    def calculate_triangle_area(triangle_shape):
        if triangle_shape.height is not None:
            return (triangle_shape.base * triangle_shape.height) * 0.5
        else:
            s = (triangle_shape.base * 3) * 0.5
            return math.sqrt(s * (s - triangle_shape.base) * (s - triangle_shape.base) * (s - triangle_shape.base))

    @staticmethod
    def calculate_triangle_perimeter(triangle_shape):
        return triangle_shape.base * 3
