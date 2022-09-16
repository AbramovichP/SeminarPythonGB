#Шеренга
#Петя впервые пришел на урок физкультуры в новой школе. 
# Перед началом урока ученики выстраиваются по росту, в порядке невозрастания. 
# Напишите программу, которая определит на какое место в шеренге Пете нужно встать, 
# чтобы не нарушить традицию, если заранее известен рост каждого ученика 
# и эти данные уже расположены по невозрастанию 
# (то есть каждое следующее число не больше предыдущего). 
# Если в классе есть несколько учеников с таким же ростом, как у Пети, 
# то программа должна расположить его после них.
#Натуральное число N (N ≤ 100) – количество учеников (не считая Петю). 
# Ai (Ai ≤ 200) – рост учеников в сантиметрах в порядке невозрастания. 
#Натуральное число X (X ≤ 200) – рост Пети.
from random import randint

def creat_array_students(n):
    students = []
    for i in range(n):
        students.append(i)
        students[i] = randint(150,200)
    return students

def array_ordering(arr):
    for run in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    print(arr)
    return arr

def search_for_peter_position(arr,x,n):
    peter_array = []
    peter_array = arr
    if peter_array[n-1] >= x:
        peter_array.append(x)
        print(f'Петя встанет на {n+1} место')
        return peter_array
    for i in range(len(arr)):
        if peter_array[i] < x:
            peter_array.insert(i,x)
            print(f'Петя встанет на {i+1} место')
            return peter_array

n = int(input('Введите Кол-во учеников в шеренге от 1 до 100: '))
while n <= 0 or n > 100:
    n = int(input('Введите Кол-во учеников в шеренге от 1 до 100: '))
students_arr = creat_array_students(n)
ordering_array = array_ordering(students_arr)
x = int(input('Введите рост Пети: '))
while x < 100 or n > 200:
    x = int(input('Введите рост Пети: '))
result = search_for_peter_position(ordering_array,x,n)
print(result)