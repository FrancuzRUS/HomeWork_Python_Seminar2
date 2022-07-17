# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. (факториалы чисел)
#     Пример:
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Введите число N ->")) 
 
def subseq_factorial(numm): 
    subseq=[1] 
    factorial=1 
    for i in range(2,numm+1): 
        factorial=i*factorial 
        subseq.append(factorial) 
    return subseq 
 
print(subseq_factorial(number))



