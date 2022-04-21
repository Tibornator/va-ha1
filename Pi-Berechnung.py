### https://de.acervolima.com/berechnen-sie-pi-mit-python/

import numpy
import math

k = 1
pi = 0

for i in range(100000):
  
    if i % 2 == 0: 
        pi += 4/k
    else: 
        pi -= 4/k
    k += 2

print('test 1')
print("test 2")
print('Pi ist gleich = ' + str(pi))
print(pi)

print('==========================')
'''
from math import acos 
  
def printValueOfPi(): 
  
    pi = round(2 * acos(0.0), 3) 
    print(pi) 
  
if __name__ == "__main__": 
  
    printValueOfPi() 
'''
print('========== Opt. 2 ================')
  
print( math.pi )

print('========== Opt. 3 ================')

print( numpy.pi )