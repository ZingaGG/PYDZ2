# Task 1

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

money = []
n = int(input("Enter n = "))
orel = 0
reshka = 0
spisok = ["orel","reshka"]

for i in range(n):
    money.append(random.choice(spisok))

    if money[i] == "reshka":
        reshka += 1
    else:
        orel += 1
    
    print(money[i])

print(f"Reshka quantity = {reshka}, Orel quantity = {orel}")

if orel >= reshka:
    print(f"Need to turn over {reshka} coins")
else:
    print(f"Need to turn over {orel} coins")