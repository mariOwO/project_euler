#!/usr/bin/env python
# coding: utf-8

# The sum of the squares of the first ten natural numbers is,
# $$1^2 + 2^2 + ... + 10^2 = 385$$
# 
# The square of the sum of the first ten natural numbers is,
# $$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$
# 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# In[5]:


def sumofsquares(L):
    sum = 0
    for i in L:
        j = i**2
        sum += j
    return sum

def squareofsum(L):
    sum = 0
    for i in L:
        sum += i
    j = sum**2
    return j


# In[8]:


L = []
for i in range(1,101): L.append(i)
print(squareofsum(L) - sumofsquares(L))

