# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# позиции задаются с клавиатуры через пробел.

number = int(input("Введите число N ->")) 
position = input("Введите позицию первого и второго элемента для умножения через пробел (отсчет с 0) ->") 
position_1=int(position[0]) 
position_2=int(position[2]) 
 
def subseq_and_multiplex(numm, pos_1, pos_2): 
    subseq=[] 
    for i in range(-numm,numm+1): 
        subseq.append(i) 
    multiplication=subseq[pos_1]*subseq[pos_2] 
    return(subseq,multiplication) 
     
print(subseq_and_multiplex(number, position_1, position_2))



