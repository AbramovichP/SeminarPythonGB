#Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def assertion_check(x,y,z):
    one = not(x or y or z)
    two = not x and not y and not z
    together = one == two
    return together

def input_of_variables(a):
    res = True
    if a == '0' or a == 'False':
        res = False
    else:
        res = True

    return res
    
print('Проверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ')
print('Для ввода значения типа False: вводите 0 или False. В остальных случаях будет True')
x = input('Введите значение X: ')
x = input_of_variables(x)
y = input('Введите значение Y: ')
y = input_of_variables(y)
z = input('Введите значение Z: ')
z = input_of_variables(z)

result = assertion_check(x,y,z)
print(f'при X = {x}, Y = {y}, Z = {z} Утверждение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z будет {result}')