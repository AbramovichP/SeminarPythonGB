#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def conversion_binary(n):
    binary = []
    while n / 2 >= 1:
        binary.insert(0,(int(n % 2)))
        n = n / 2
    binary.insert(0,(int(n % 2)))    
    return binary
num = int(input('Введите десятичное число: '))
print('Преобразуем в двоичную: ')
print(*conversion_binary(num))