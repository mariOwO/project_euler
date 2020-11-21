#!/usr/bin/env python
# coding: utf-8

# 
# 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a² + b² = c²
# 
# For example, 3² + 4² = 9 + 16 = 25 = 5².
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 

# In[4]:


def Pythagoren():
    for a in range(1, 999):
        for b in range(a+1, 999):
            for c in range(b+1, 999):
                if (a**2 + b**2) == c**2 and (a + b + c) == 1000: return a*b*c


# In[5]:


time(Pythagoren())

