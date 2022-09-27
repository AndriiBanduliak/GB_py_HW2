'''1. Напишите программу, которая принимает на
вход вещественное число и показывает сумму его цифр.'''

a = int(input('Enter the number '))

suma = 0

while a>0:
    s = a % 10
    suma +=s
    a = a//10
    
print(suma)