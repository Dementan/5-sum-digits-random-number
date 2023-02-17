# Calculate the sum of the digits of a random three-digit number

import random
n = random.randint(100, 999)  #random three-digit number
print(n)
a = n//100  #looking for first position
b = (n//10) % 10  #looking for second position
c = n % 10  #looking for third position
print(a+b+c) #sum of digits of three positions
