#Bubblesort opgave:

#Make a random list
from random import randint
import time as t
import numpy as np
import matplotlib as plt
 
#Bubblesort
def bubblesort(L):
    for i in range (0,len(L)):
        for j in range (0,len(L)-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    print(L)
n = 10
list = []
for i in range(0,n):
    r = randint(0,10*n)
    list.append(r)
print(list)

#Mesure the time (mili seconds)
før = t.perf_counter()
bubblesort(list)
efter = t.perf_counter()
tid = (efter - før)*1000
print(tid)


#PLOT
#a = []
#b = []
#c = []

#coaf = np.polyfit(a,b,2)
#poly1d_fn = np.poly1d(coaf)
#plt.plot(a, b, 'yo', c, poly1d_fn(c), 'k')
#plt.xlim(0, 5)
#plt(0, 7)
#plt.show()