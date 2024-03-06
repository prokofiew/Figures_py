from abc import ABC, abstractmethod
import math


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


class Square(Shape):
    def __init__(self, calculator):
        super().__init__(calculator)
        self.side_a = float(input(f"Enter dimension of {self}: "))
        self.area = self.calculator.area_calculator(self)
        self.perimeter = self.calculator.perimeter_calculator(self)

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter


class Triangle(Shape):
    def __init__(self, calculator):
        super().__init__(calculator)
        self.base = float(input(f"Enter base dimension of {self}: "))
        self.height = float(input(f"Enter height of {self}: "))
        self.area = self.calculator.area_calculator(self)
        self.perimeter = self.calculator.perimeter_calculator(self)

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter


class Circle(Shape):
    def __init__(self, calculator):
        super().__init__(calculator)
        self.radius = float(input(f"Enter radius of {self}: "))
        self.area = self.calculator.area_calculator(self)
        self.perimeter = self.calculator.perimeter_calculator(self)

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter


class Rectangle(Shape):
    def __init__(self, calculator):
        super().__init__(calculator)
        self.side_a = float(input(f"Enter dimension of side_A of the {self}: "))
        self.side_b = float(input(f"Enter dimension of side_B of the {self}: "))
        self.area = self.calculator.area_calculator(self)
        self.perimeter = self.calculator.perimeter_calculator(self)

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter


class AreaPerimeterCalculator:
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


class Menu:
    def __init__(self, m_dict, calculator):
        self.m_dict = m_dict
        self.calculator = calculator

    def display_menu(self):
        print('Pick a figure:')
        for key, value in self.m_dict.items():
            print(f"{key}. {value}")

    def menu_choice(self):
        user_input = int(input("What is your choice?:"))
        return user_input

    def display_message(self, a, p, o):
        message = f"Area of {o} is: {a}, and perimeter: {p}"
        return print(message)

    def display_choice_result(self, choice, calculator):
        if choice == 1:
            square = Square(calculator)
            return self.display_message(square.get_area(), square.get_perimeter(), square)
        elif choice == 2:
            triangle = Triangle(calculator)
            return self.display_message(triangle.get_area(), triangle.get_perimeter(), triangle)
        elif choice == 3:
            circle = Circle(calculator)
            return self.display_message(circle.get_area(), circle.get_perimeter(), circle)
        elif choice == 4:
            rectangle = Rectangle(calculator)
            return self.display_message(rectangle.get_area(), rectangle.get_perimeter(), rectangle)
        elif choice == 5:
            return exit("You ended the program")
        else:
            return print("Pick an option from the menu")


calculator = AreaPerimeterCalculator()
menu_dict = {1: 'Square', 2: 'Triangle', 3: 'Circle', 4: 'Rectangle', 5: 'Exit'}
menu = Menu(menu_dict, calculator)
menu.display_menu()
while True:
    choice = menu.menu_choice()
    menu.display_choice_result(choice, calculator)
