#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Question :1

import numpy

def arrays(arr):
    
    a=numpy.array(arr,float)
    
    n=len(a)
    k=n//2
    i=0
    while i<k:
        t=a[n-i-1]
        a[n-i-1]=a[i]
        a[i]=t
        i+=1
    
    return a
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# In[4]:


# Question 2:

import numpy

num=list(map(int,input().split(' ')))

arr=numpy.array(num)

ar=numpy.reshape(arr,(3,3))

print(ar)


# In[5]:


# Question 3:

import numpy

lst=list(map(int,input().split(' ')))
n=lst[0]
m=lst[1]

num=[]

for i in range(n):
    nu=list(map(int,input().split(' ')))
    num.append(nu)
    
arr2d=numpy.array(num)

print(arr2d.T)
print(arr2d.flatten())


# In[6]:


# Question 4:

import numpy

lst=list(map(int,input().split(' ')))

n=lst[0]
m=lst[1]
p=lst[2]

num1=[]
for i in range(n):
    num1.append(list(map(int,input().split(' '))))
    
num2=[]
for i in range(m):
    num2.append(list(map(int,input().split(' '))))
    
arr1=numpy.array(num1)
arr2=numpy.array(num2)

arr=numpy.concatenate((arr1,arr2),axis=0)
print(arr)


# In[7]:


# Question 5:

import numpy

nums = tuple(map(int, input().split()))
print (numpy.zeros(nums, dtype = numpy.int))
print (numpy.ones(nums, dtype = numpy.int))


# In[8]:


# Question 6:

import numpy
numpy.set_printoptions(legacy='1.13')

lst=list(map(int,input().split(' ')))
n=lst[0]
m=lst[1]

print(numpy.eye(n,m))


# In[9]:


# Question 7:

import numpy

lst=input().split(' ')
n=int(lst[0])
m=int(lst[1])

lst=[]
for i in range(n):
    lst.append(list(map(int,input().split(' '))))
    
arrA=numpy.array(lst,int)

lst=[]
for i in range(n):
    lst.append(list(map(int,input().split(' '))))
    
arrB=numpy.array(lst,int)

print(arrA+arrB)
print(arrA-arrB)
print(arrA*arrB)
print(arrA//arrB)
print(arrA%arrB)
print(arrA**arrB)


# In[10]:


# Question 8:

import numpy
numpy.set_printoptions(legacy='1.13')

arr=numpy.array(list(map(float,input().split(' '))))

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))


# In[11]:


# Question 9:

import numpy

lst=list(map(int,input().split(' ')))
n=lst[0]
m=lst[1]

lst=[]
for i in range(n):
    lst.append(list(map(int,input().split(' '))))
    
arr=numpy.array(lst,int)

arr=numpy.sum(arr,axis=0)

print(numpy.prod(arr))


# In[12]:


# Question 10:

import numpy

lst=list(map(int,input().split(' ')))
n=lst[0]
m=lst[1]

lst=[]
for i in range(n):
    lst.append(list(map(int,input().split(' '))))
    
arr=numpy.array(lst)

arr=numpy.min(arr,axis=1)

print(numpy.max(arr))
    


# In[13]:


# Question 11:

import numpy

lst=list(map(int,input().split(' ')))
n=lst[0]
m=lst[1]

lst=[]
for i in range(n):
    lst.append(list(map(int,input().split(' '))))
    
arr=numpy.array(lst)

print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(round(numpy.std(arr),11))


# In[14]:


# Question 12:

import numpy


n=int(input())

lst=[]
for i in range(n):
    lst.append(list(map(int,input().split(' '))))
    
arrA=numpy.array(lst)

lst=[]
for i in range(n):
    lst.append(list(map(int,input().split(' '))))
    
arrB=numpy.array(lst)

print(numpy.matmul(arrA,arrB))


# In[15]:


# Question 13:

import numpy

arrA=numpy.array((list(map(int,input().split(' ')))))
arrB=numpy.array((list(map(int,input().split(' ')))))

print(numpy.inner(arrA,arrB))
print(numpy.outer(arrA,arrB))


# In[16]:


# Question 14:

import numpy

arrA=numpy.array((list(map(float,input().split(' ')))))

n=int(input())

print(numpy.polyval(arrA,n))


# In[18]:


# Question 15:

import numpy

n=int(input())
lst=[]
for i in range(n):
    lst.append(list(map(float,input().split(' '))))
    
arr=numpy.array(lst)

print(round(numpy.linalg.det(arr),2))


# In[ ]:




