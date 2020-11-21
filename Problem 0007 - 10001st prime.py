#!/usr/bin/env python
# coding: utf-8

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?
# 

# In[9]:


import math
prim = 2
count = 0
while True:
    if all([prim % i for i in range(2, int(math.sqrt(prim)) + 1)]) != 0:
        count += 1
        if count == 10001: 
            print(prim)
            break
    prim += 1 


# In[ ]:




