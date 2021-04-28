#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Question 1:
    
print("Hello, World!")


# In[3]:


# Question 2:

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2==1:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")


# In[4]:


# Question 3

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)


# In[5]:


# Question 4:

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)


# In[6]:


# Question 5:

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i*i)


# In[10]:


# Question 6:

def is_leap(year):
    leap = False
    
    if year%400==0 or year%100!=0 and year%4==0:
        leap=True
    
    return leap

year = int(input())
print(is_leap(year))


# In[8]:


# Question 7:

if __name__ == '__main__':
    n = int(input())
    
    for i in range(1,n+1):
        print(i,end='')


# In[ ]:




