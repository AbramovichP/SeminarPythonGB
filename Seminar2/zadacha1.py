#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.


from random import randint

def creating_an_array_of_coins(n):
    coin = []
    for i in range(n):
        coin.append(i)
        coin[i] = randint(0,1)
    return coin

def replacing_numbers_with_words(arr):
    words_array = []
    for i in range(len(arr)):
        words_array.append(i)
        if arr[i] == 0:
            words_array[i] = 'Решко'
        else:
            words_array[i] = 'Орёл'
    print(words_array)

def couting_coins(arr):
    eagle = 0
    reshko = 0
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            eagle = eagle + 1
        else:
            reshko = reshko + 1
        i = i + 1
    if eagle > reshko:
        return reshko
    elif reshko > eagle:
        return eagle
    else:
        return reshko

n = int(input('Введите кол-во монеток: '))
arr_coin = creating_an_array_of_coins(n)
replacing_numbers_with_words(arr_coin)
print(f'Минимальное число монеток, которые нужно перевернуть,\
 чтобы все монетки были повернуты вверх одной и той же стороной: {couting_coins(arr_coin)}')