import math

#power of numbers
print(pow(3,4,6)) # first - base, second - expon, third - mod, result 3

#factorial of number
print(math.factorial(5)) # result 120

#The greatest common divisor
print(math.gcd(18,24)) # result 6

###
frac,whole = math.modf(3.14)
print(whole) # result 3
print(frac) # result 0.14