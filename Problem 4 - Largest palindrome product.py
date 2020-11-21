#!/usr/bin/env python
# coding: utf-8

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.  
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

# In[19]:


L = []
for i in range(100,1000):
    for j in range(100,1000):
        prod = i*j
        prod = str(prod)
        fsthalf = prod[:len(prod)//2] 
        sechalf = prod[len(prod)//2:]
        if fsthalf == sechalf[::-1]:
            L.append(prod)
print(max(L))


# In[ ]:




