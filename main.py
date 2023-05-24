# Task 1

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# import random

# money = []

# n = int(input("Enter n = "))
# if n <= 0:
#     print("Incorrect input")
# else:
#     orel = 0
#     reshka = 0
#     spisok = ["orel","reshka"]

#     for i in range(n):
#         money.append(random.choice(spisok))

#         if money[i] == "reshka":
#             reshka += 1
#         else:
#             orel += 1
    
#         print(money[i])

#     print(f"Reshka quantity = {reshka}, Orel quantity = {orel}")

#     if orel >= reshka:
#         print(f"Need to turn over {reshka} coins")
#     else:
#         print(f"Need to turn over {orel} coins")

# Task 2

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# import math

# x = int(input("x = "))
# y = int(input("y = "))

# s = x + y
# p = x * y

# x = 0 # Обнуляем для честности :D
# y = 0 # Обнуляем для честности :D

# if (x > 1000) or (y > 1000):
#     print("Incorrect input!")
# else:
#     d = (s * s) - (4 * p)
#     d = math.sqrt(d)
#     y = (s + d) / 2
#     x = (s - d) / 2
#     print(f"Загаданные числа = {x}, {y}")

# Task 3

# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Enter N >= 1 "))
dvoika = 1

if N < 1:
    print("Incorrect input")
else:
    while dvoika <= N:
        print(dvoika)
        dvoika *= 2
        