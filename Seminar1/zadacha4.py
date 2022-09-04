#Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


def coordinate_range(n):
    unicode_charter = "\u221E"
    if n == '1':
        print(f'X(1; + {unicode_charter}) and Y(1; + {unicode_charter})')
    elif n == '2':
        print(f'X(-1; - {unicode_charter}) and Y(1; + {unicode_charter})')
    elif n == '3':
        print(f'X(-1; - {unicode_charter}) and Y(-1; - {unicode_charter})')
    elif n == '4':
        print(f'X(1; + {unicode_charter}) and Y(-1; - {unicode_charter})')
    else:
        print('Нет такой четверти')
num = input('Введите цифру четверти от 1 до 4: ')
coordinate_range(num)