#Sets er udordede samlimger af unikke elementer
list = [1,2,2,3,4,4]
s = set(list)
print (s) #output {1,2,3}

#OPGAVE 
list = [1,2,5,2,6,2,6,2,7,1,8]
s = set(list)
s.add(3)
s.add(9)
s.add(0)
s.add(4)
print(s) #output {0,1,2,3,4,5,6,7,8,9}

#SETS I PY + super sets
even = {2,4,6,8,10,12,14,16,18,20}
odd = {1,3,5,7,9,11,13,15,17,19}
prime = {1,3,5,7,11,13,17,19} #har fjernet 2 så den er superset med odd
odd_and_prime = odd.issuperset(prime)
print(odd_and_prime)

