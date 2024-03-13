from Shape.square import Square
from Shape.triangle import Triangle
from Shape.rectangle import Rectangle
from Shape.circle import Circle

from calculator_interface import CalculatorInterface


class Menu:
    def __init__(self, m_dict, calculator: CalculatorInterface):
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
