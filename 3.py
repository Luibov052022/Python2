#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#Пример:

#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Введите число: '))
sum = 0
for i in range (1, number+1):
    sum += (1 + 1/i) ** i

print(round(sum, 2))    
