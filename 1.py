#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.  Определите минимальное число
#монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
#Выведите минимальное количество монет, которые нужно перевернуть
#5 -> 1 0 1 1 0'

from random import randint

n = int(input("Введите колличество монеток: "))


list = list(randint(0, 1) for i in range(n))
print (f'монеты: {list}')
count0, count1 = 0, 0

for e in list:
     if e == 0:
         count0 += 1
     else:
        count1 += 1

if count0 > count1:
     print(f'Надо перевернуть {count1} монеты')
else:
     print(f'Надо перевернуть {count0} монеты')