
#Types

x = 5
y = 5.7
z = 2+3j

print(type(x))
print(type(y))
print(type(z))

a = '24'
print(type(a))
a = int(a)
print(type(a))
print(a*3)

b = 3.14
print(int(b))

x = 3        #real
y = 5        #imaginary
print(complex(x,y))


#Math Operator

print(2 + 3)    #Addition
print(5 - 2)    #Subtraction
print(4 * 5)    #Multiplication
print(7 / 2)    #Division
print(7 // 2)   #Floor Division
print(9 % 2)    #Remainder
print(2 **3)    #Exponential


x = 3
#x = x + 5
x += 5
print(x)

x -= 4
print(x)

#Measure distance
print(abs(2 - 10))

#Rounding Numbers
import math

price = 35.54897342

print(round(price))
print(round(price, 2))
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))
print(int(price))

#Random
import random as rn

print(rn.random())  #returns a random float between 0.0 and 1.0
print(rn.randint(1,5))      #gets a random whole number from start to end (including both)

#Validation
x = 7.0
y = 7.1
print(x.is_integer())   #is_integer() checks if a float has no decimal part(is a whole number)
print(y.is_integer())

a = 70.4
print(isinstance(a, int))   #isinstance() checks if a value belongs to a certain data type
print(isinstance(a, float))


#Generate a random interger between 1 and 100.
#and check if the result is an even number.

import random

m = random.randint(1, 100)
print(m)

if m%2==0:
    print('Even Number')
else: print('Not Even Number')
