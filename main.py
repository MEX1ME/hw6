# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# firstNum = int(input("Введите первое число арифм прогрессии: "))
# count = int(input("Введите количество членов прогрессии: "))
# step = int(input("Введите разность (шаг прогрессии): "))


# def progression(firstNum, count, step):
#     newList = []
#     i = 1
#     while i <= count:
#         newList.append(firstNum + (i - 1) * step)
#         i += 1
#     return newList


# newlist = progression(firstNum, count, step)
# print(newlist)

# Задача 32: Определить индексы элементов массива (списка),
#  значения которых принадлежат заданному диапазону (т.е. не меньше заданного
#  минимума и не больше заданного максимума). Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

nums = int(input("Введите количество элементов массива: "))
minHel = int(input("Введите начало диапазона: "))
maxHel = int(input("Введите конец диапазона: "))


def genList(nums):
    newlist = []
    i = 0
    while i < nums:
        newlist.append(random.randint(0, 100))
        i += 1
    return newlist


def findIndex(newList, minHel, maxHel):
    indexList = []
    k = 0
    while k < len(newList):
        if minHel <= newList[k] <= maxHel:
            indexList.append(k)
        k += 1
    return indexList

newList = genList(nums)
print(newList)
indexList = findIndex(newList, minHel, maxHel)
print(indexList)
