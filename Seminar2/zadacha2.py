#Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

def array_of_integer(n):
    nums = []
    for i in range(1,n+1):
        nums.append(i)
    return nums
    
def sum_of_integers(arr):
    sum = 0
    for e in range(len(arr)):
        sum = sum + arr[e]
    return sum

n = int(input('Введите число: '))
while n <= 0 or n > 10 ** 4:
    print('Число должно быть больше нуля и меньше 10000')
    n = int(input('Введите число: '))
result = sum_of_integers(array_of_integer(n))
print(f'Сумма целых чисел от 1 до {n} : {result}')