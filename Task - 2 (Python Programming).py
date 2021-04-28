#!/usr/bin/env python
# coding: utf-8


# Question 1

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    lst=[]
    
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                sum=i+j+k
                if sum!=n:
                    l=[]
                    l.append(i) 
                    l.append(j)
                    l.append(k)
                    lst.append(l)
    
    print(lst)
                   

# Question 2

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst=[]
    
    for i in arr:
        lst.append(i)
    lst.sort()
    
    for i in range(n-1,0,-1):
        if lst[i]!=lst[i-1]:
            print(lst[i-1])
            break
        

# Question 3

def sortSecond(val):
    return val[1] 
    
if __name__ == '__main__':
    
    lst=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        l=[]
        l.append(name)
        l.append(score)
        lst.append(l)
    
    lst.sort(key=sortSecond)
    k=0
    for i in range(len(lst)):
        if lst[i][1]!=lst[i+1][1]:
            k=lst[i+1][1]
            break
    
    l=[]
    for j in range(i+1,len(lst)):
        if k==lst[j][1]:
            l.append(lst[j][0])
        else:
            break
    
    l.sort()
    for i in range(len(l)):
        print(l[i])
        
        
# Question 4

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for x in student_marks:
        if x==query_name:
            lst=student_marks[x]
            marks=0
            for i in range(len(lst)):
                marks+=lst[i]
            
            a=marks/len(lst)
            print ('%.2f'%a)
           


# Question 5:

if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        x=input().split(' ')
        if x[0]=="insert":
            k=int(x[1])
            l=int(x[2])
            lst.insert(k,l)
        elif x[0]=="print":
            print(lst)
        elif x[0]=="remove":
            lst.remove(int(x[1]))
        elif x[0]=="append":
            lst.append(int(x[1]))
        elif x[0]=="sort":
            lst.sort()
        elif x[0]=="pop":
            lst.pop()
        else:
            lst.reverse()
    
    
# Question 6:

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    lst=[]
    for x in integer_list:
        lst.append(x)
    
    tu=tuple(lst)
    
    print(hash(tu))



# Question 7:

def average(array):
    se={}
    se=set()
    for i in range(len(array)):
        se.add(array[i])
    
    marks=0
    for x in se:
        marks+=x
    
    return (marks/len(se))
        

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# Question 8:

n=int(input())

se={}
se=set()
for i in range(n):
    se.add(input())
    
print(len(se))



# Question 9:
    
N=input().split(' ')
n=int(N[0])
m=int(N[1])

lst=input().split(' ')
for i in range(n):
    lst[i]=int(lst[i])

A=input().split(' ')
B=input().split(' ')

k=set()
t=set()
for i in range(m):
    k.add(int(A[i]))
    t.add(int(B[i]))
diff=0

for i in lst:
    if i in k:
        diff+=1
        
    if i in t:
        diff+=-1
print(diff)


# Question 10:

n=int(input())
a=set(input().split(' '))
m=int(input())
b=set(input().split(' '))

t=set(a.difference(b))
v=set(b.difference(a))

lst=[]
for x in t:
    lst.append(int(x))
for x in v:
    lst.append(int(x))
lst.sort()

for i in lst:
    print(i)



# Question 11:

n = int(input())
s = set(map(int, input().split()))

m=int(input())

for i in range(m):
    x=input().split(' ')
    if x[0]=="pop":
        s.pop()
    elif x[0]=="remove":
        s.remove(int(x[1]))
    else:
        s.discard(int(x[1]))

ans=0
for x in s:
    ans+=x
print(ans) 



# Question 12:

n=int(input())
a=set(map(int,input().split(' ')))
m=int(input())
b=set(map(int,input().split(' ')))

a=a.union(b)
print(len(a))



# Question 13:


n=int(input())
a=set(map(int,input().split(' ')))
m=int(input())
b=set(map(int,input().split(' ')))

a=a.intersection(b)

print(len(a))



# Question 14:


n=int(input())
a=set(map(int,input().split(' ')))
m=int(input())
b=set(map(int,input().split(' ')))

a=a.difference(b)

print(len(a))



# Question 15:


n=int(input())
a=set(map(int,input().split(' ')))
m=int(input())
b=set(map(int,input().split(' ')))

t=set(a.union(b))
v=set(a.intersection(b))

print(len(t)-len(v))




#Question 16:
    
    
n=int(input())
A=set(map(int,input().split(' ')))
m=int(input())

for i in range(m):
    x=input().split(' ')
    if x[0]=="intersection_update":
        b=set(map(int,input().split(' ')))
        A&=b
    elif x[0]=="update":
        b=set(map(int,input().split(' ')))
        A|=b
    elif x[0]=="symmetric_difference_update":
        b=set(map(int,input().split(' ')))
        A^=b
    else:
        b=set(map(int,input().split(' ')))
        A-=b 

ans=0
for x in A:
    ans+=x
print(ans)



# Question 17:


k=int(input())
lst=list(map(int,input().split(' ')))
dic={}
se=set()
for i in range(len(lst)):
    se.add(lst[i])

for x in se:
    dic[x]=0

for i in lst:
    dic[i]=dic[i]+1

for x in dic:
    if dic[x]==1:
        print(x)
        break
    


# Question 18:

t=int(input())

while t!=0:
    n=int(input())
    a=set(map(int,input().split()))
    m=int(input())
    b=set(map(int,input().split()))
    b=b-a
    
    if len(b)==(m-n):
        print("True")
    else:
        print("False")
    
    t-=1



# Question 19:

A=set(map(int,input().split()))

n=int(input())
f=1
for i in range(n):
    a=set(map(int,input().split()))
    t=set(a-A)
    u=set(A-a)
    
    if len(t)!=0 or len(u)==0:
        f=0
        break
    
    
if f==1:
    print("True")
else:
    print("False")
        
    





