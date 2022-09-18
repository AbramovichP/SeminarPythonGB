#Задайте список из нескольких чисел. 
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


def sum_odd_numbers(arr):
    sum = 0
    for i in range(1,len(nums),2):
        sum += nums[i]
    return sum
    
nums = [2, 3, 5, 9, 3]        
print(sum_odd_numbers(nums))
