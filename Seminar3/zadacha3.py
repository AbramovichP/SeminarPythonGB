#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части 
# элементов.
def fractional_selection(arr):
    fract = []
    for i in range(len(arr)):
        temp = round(arr[i] % 1, 3)
        if temp != 0:
            fract.append(temp)
    return fract
def difference_min_max(arr):
    result = max(fractional_selection(arr)) - min(fractional_selection(arr))
    return result

nums = [1.1, 1.2, 3.1, 5, 10.01]
print(difference_min_max(nums))