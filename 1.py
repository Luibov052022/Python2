# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = float(input('Введите число: '))
sum = 0
if number >= 1:
    while number >= 1:
        sum += int(number%10)
        number = int(number/10)
else:
    number *= 10
    while not int(number%10) == 0:
        sum += int(number%10)
        number = number * 10
print("сумма цифр числа равна: " + str(int(sum)))