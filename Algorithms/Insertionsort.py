from random import randint

def insertionsort(l):
    for j in range (1, len(l)):
        key = l[j]
        i = j-1
        while i >= (0) and l[i] > key:
            l[i+1] = l[i]
            i = i-1
        l[i+1] = key
    print(l)

n = 10
list = []
for i in range(0,n):
    r = randint(0,10*n)
    list.append(r)
print(list)

insertionsort(list)


