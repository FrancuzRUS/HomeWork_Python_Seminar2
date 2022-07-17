# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     Пример:
#     - 6782 -> 23
#     - 0,56 -> 11

number=input("Введите число -> ") 
 
number.split() 
sum=0 
for i in range (len(number)): 
    if number[i] != ',': 
        sum=sum+int(number[i]) 
 
print(sum)



