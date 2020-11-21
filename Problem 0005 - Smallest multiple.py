#!/usr/bin/env python
# coding: utf-8

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.  
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# In[32]:


L = []
for d in range(1,21):
    L.append(d)

for i in range(1,99999999999):
    if all(i % d == 0 for d in L):
        print(i)
        break


# In[39]:


from functools import reduce

def gcd(n, d):
    while d != 0:
        n, d = d, n % d
    return n

int(reduce(lambda n, d: n * d / gcd(n, d), range(1, 21)))


# In[ ]:




