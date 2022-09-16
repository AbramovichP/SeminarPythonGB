#Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

def smallest_divisor(n):
    i = 2
    while i < n:
        if n % i == 0:
            return i
        else:
            i += 1

n = int(input(f'Введите целое число от 2 до {10 ** 6}: '))
while n <= 1 or n > 10 ** 6:
    print('Число должно быть от 2 до 1000000')
    n = int(input('Введите число: '))
print(f'Наименьший натуральный делитель: {smallest_divisor(n)}')
