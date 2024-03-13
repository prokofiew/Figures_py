from area_perimeter_calculator import AreaPerimeterCalculator
from menu import Menu

if __name__ == '__main__':
    calculator = AreaPerimeterCalculator()
    menu_dict = {1: 'Square', 2: 'Triangle', 3: 'Circle', 4: 'Rectangle', 5: 'Exit'}
    menu = Menu(menu_dict, calculator)
    menu.display_menu()
    while True:
        choice = menu.menu_choice()
        menu.display_choice_result(choice, calculator)
