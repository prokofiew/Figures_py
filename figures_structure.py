import math


def square_field(a):
    sq_field = a * a
    return sq_field


def square_perimeter(a):
    sq_perimeter = 4 * a
    return sq_perimeter


def triangle_field(a, h):
    tri_field = (a * h) / 2
    return tri_field


def triangle_perimeter(a):
    tri_perimeter = 3*a
    return tri_perimeter


def circle_field(r):
    cir_field = pow(r, 2) * math.pi
    return cir_field


def circle_perimeter(r):
    cir_perimeter = 2 * math.pi * r
    return cir_perimeter


def rectangle_field(a, b):
    rec_field = a * b
    return rec_field


def rectangle_perimeter(a, b):
    rec_perimeter = 2 * a + 2 * b
    return rec_perimeter


def menu():
    menu = {1: 'Square', 2: 'Triangle', 3: 'Circle', 4: 'Rectangle', 5: 'Exit'}
    print('=============== MENU ==================')
    for key, value in menu.items():
        print(f'{key}. {value}')
    print('---------------------------------------')

    while True:
        user_choice = int(input('Select figure:'))
        if user_choice == 5:
            print('You exited program')
            break
        elif menu.get(int(user_choice)) is None:
            print(f'{user_choice} is not an option on the menu')

        elif user_choice == 1:
            dimension = int(input('Enter the dimension of the side of the square:'))
            field = square_field(dimension)
            perimeter = square_perimeter(dimension)
            print(f'Square field is: {field} and circumference is: {perimeter}')

        elif user_choice == 2:
            base, height = map(int, input('Enter the dimension of the base and high of the triangle:').split())
            field = triangle_field(base, height)
            perimeter = triangle_perimeter(base)
            print(f'Triangle field is: {field} and circumference is: {perimeter}')

        elif user_choice == 3:
            radius = int(input('Enter the dimension of the radius of the circle:'))
            field = circle_field(radius)
            perimeter = circle_perimeter(radius)
            print(f'Triangle field is: {field} and circumference is: {perimeter}')

        elif user_choice == 4:
            side_a, side_b = map(int, input('Enter the dimension of the sides of the rectangle (separated by space):').split())
            field = rectangle_field(side_a, side_b)
            perimeter = rectangle_perimeter(side_a, side_b)
            print(f'Rectangle field is: {field} and circumference is: {perimeter}')


if __name__ == '__main__':
    menu()
