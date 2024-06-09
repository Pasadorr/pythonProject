#def divide(first, second):
    #if second == 0:
        #print('Ошибка')
    #else:
        #return first / second

#print(divide(69, 3))
#print(divide(3, 0))

#from math import inf
#def divide(first, second):
    #if second == 0:
        #return inf
    #else:
        #return first / second


#print(divide(49, 7))
#print(divide(15, 0))

from fake_math import divide as divf
from true_math import divide as divt

divf(69, 3)
divf(3, 0)

divt(49, 7)
divt(7, 0)

