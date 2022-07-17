# 3. Задайте список из n чисел последовательности  (1 + 1/n)^n и выведите на экран их сумму. Делать через функции.
#     Пример:
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input("Введите число N ->")) 
 
def subseq(numm): 
    subsequence=[] 
    sum=0 
    for i in range(1,numm+1): 
        subsequence.append((1+(1/i))**i) 
        sum+=1+(1/i)**i 
    return (subsequence, sum) 
print(subseq(number))


