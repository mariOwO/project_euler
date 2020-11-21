#!/usr/bin/env python
# coding: utf-8

# 
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
# 

# In[1]:


import math
def genPrime():
    sum = 2
    prim = 3
    while prim < 2000000:
        if all([prim % i for i in range(2, int(math.sqrt(prim)) + 1)]) != 0: #Sieb des Eratosthenes
            sum += prim
        prim += 2 
    return sum


# In[2]:


time(genPrime())

