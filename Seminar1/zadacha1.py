#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
#  является ли этот день выходным.

#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

def DayOfTheWeek (n):
    if numDay <= 0 or numDay > 7:
     print('Нет такого дня недели!')
    elif numDay >= 1 and numDay <= 5:
        print('Нет')
    else:
        print('Да')
numDay = int(input('Введите число дня недели: '))    
DayOfTheWeek(numDay)