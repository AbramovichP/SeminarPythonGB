#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def sum_pair_of_numbers(arr):
    result = []
    j = 0
    if len(arr) % 2 == 0:
        n = 0
    else:
        n = 1
    for i in range(int((len(arr)/2)+n)):
        sum = 0
        j = j-1
        sum = arr[i] * arr[j]
        result.append(sum)
    return result

nums = [2, 3, 4, 5, 6]
print(sum_pair_of_numbers(nums))