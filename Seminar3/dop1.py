#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Доп)

def fibonachi(n):
    fib = [0,1]
    temp = 2
    for i in range(n-1):
        fib.append(fib[temp-1] + fib[temp -2])
        temp +=1 
    return fib

def negofibonachi(arr):
    negfib = arr
    for i in range(0,len(negfib),2):
        negfib[i] = negfib[i] * (-1)
    negfib1 = negfib[::-1]
    return negfib1

n = int(input('Введите число: '))
fib = fibonachi(n)
negfib = negofibonachi(fibonachi(n))
fib.pop(0)
sliyanie = negfib + fib
print(sliyanie)