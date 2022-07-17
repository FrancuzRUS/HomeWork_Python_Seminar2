# 5. Реализуйте алгоритм перемешивания списка.

import random 

list_example=[1,2,3,4,5,6,7,8,9] 
 
def list_shuffle(list_for_shuffle): 
    count=len(list_for_shuffle) 
    while count!=0: 
        i=random.randint(0,count) 
        box=list_for_shuffle[i] 
        list_for_shuffle[i] = list_for_shuffle[-1] 
        list_for_shuffle[-1] = box 
        count-=1 
    return list_for_shuffle 
        
print(list_shuffle(list_example))





