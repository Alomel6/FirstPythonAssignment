# -*- coding: utf-8 -*-
"""
basic for loop 
"""
import numpy as np 

list100 =np.linspace(1, 100, 100)
sum100 = sum(list100)
print('sum of the first 100 integers is: {}'.format(sum100))

otherSum=0 
for i in range (101):
    otherSum += i
    
print('Sum of all numbers up to 100 = {}'.format (otherSum))

