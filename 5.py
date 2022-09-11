# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

N = int(input('Введите число: '))
my_list = []
resault = 1
for i in range (N):
    my_list.append(random.randint(-N, N))
print(my_list)

count_file = random.randint(1, N)
with open('file.txt', 'w') as data:
    for i in range (count_file):
        data.write(str(random.randint(0, count_file - 1)) + '\n')
 
with open('file.txt', 'r') as data:
    for i in data:
        resault *= my_list[int(i)]
   
print(resault)