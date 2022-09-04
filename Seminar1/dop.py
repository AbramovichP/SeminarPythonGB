#Последовательностью Фибоначчи называется последовательность 
#чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#Требуется найти N-е число Фибоначчи.
def fibonachchi(n):
    fib = []
    for i in range(n+1):
        fib.append(i)

    i = 3
    while i < len(fib):
        fib[i] = fib[i-1] + fib[i-2]
        i+=1
    print(fib)
    return fib[n]

number = int(input('Введите N-е число Фибоначчи : '))
if number < 0:
    print('Введеное число не соответствует условиям')
else:
    print(fibonachchi(number))
