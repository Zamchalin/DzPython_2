# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите пожалуйста число: "))
k = 0
number = 0
while 2**k < n:
    number = 2**k
    k+=1
    print(number, end = " ")
   