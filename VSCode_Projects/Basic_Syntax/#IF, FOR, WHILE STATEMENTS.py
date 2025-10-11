#IF, FOR, WHILE STATEMENTS

#IF OPG: ASK USER FOR NUMBER (POSETIVE,NEGATIVE,ZERO)

#ask a user for a number:
number = int(input("Input a number:  "))

#if the number is negative:
if number < 0:
    print("This number is negative!")

#otherwise if the number is zero:
elif number == 0:
    print("You have inputted the number zero")

#if none of the others:
else:
    print("This number is positive!")


