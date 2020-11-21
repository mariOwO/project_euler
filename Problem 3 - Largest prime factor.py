#!/usr/bin/env python
# coding: utf-8

# The prime factors of 13195 are 5, 7, 13 and 29.  
# 
# What is the largest prime factor of the number 600851475143 ?

# In[20]:


n = 600851475143


# In[26]:


def prim(n):
    arr = []
    fact = 2
    while fact**2 <= n:
        while n > 1:
            while n % fact == 0:
                arr.append(fact)
                n = n/fact
            fact += 1
    print(arr)
    return max(arr)


# In[27]:


prim(n)


# In[30]:


def prim_fast(n):
    fact = 2
    while fact**2 <= n:
        if n % fact != 0:
            fact += 1
        else:
            n /= fact
    return int(n)


# In[31]:


prim_fast(n)


# In[ ]:




