#imports numpy library for logarithm
import numpy

# Asks user for number x and y
x=int(input('x='))
y=int(input('y='))

# prints number "x" raised to power of "y" and log (base 2) of "x"
z=x**y
a=numpy.log2(x)
print(z)
print(a)
