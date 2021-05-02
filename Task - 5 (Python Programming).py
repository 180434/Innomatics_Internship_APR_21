
# Question 1:

t=int(input())

while t:
    
    num=input()
    k=0
    if num[0]=='+' or num[0]=='-':
        k=1
        
    ct=0
    
    for i in range(k,len(num)):
        if num[i]=='.':
            if ct==0:
                ct=1
            else:
                break
        elif num[i]>='0' and num[i]<='9':
            continue
        else:
            break
     
    if len(num)==1:
        print("False")
    elif i==len(num)-1:
        print("True")
    else:
        print("False")
    
    t-=1
        

# Question 2:

regex_pattern = r"[,.]+"

import re
print("\n".join(re.split(regex_pattern, input())))


# Question 3:

st=input()
f=0
for i in range(len(st)-1):
    if (st[i]>='a' and st[i]<='z') or(st[i]>='A' and st[i]<='Z') or(st[i]>='0' and st[i]<='9'):
        if st[i]==st[i+1]:
            f=1
            break
        
if f==1:
    print(st[i])
else:
    print("-1")


# Question 4:

st=input()

vow=0
ct=0
for i in range(len(st)):
    if st[i]=='a' or st[i]=='e' or st[i]=='i' or st[i]=='o' or st[i]=='u' or st[i]=='A'      or st[i]=='E' or st[i]=='I' or st[i]=='O' or st[i]=='U':
        vow+=1
        
    else:
        if vow>=2:
            ct+=1
            print(st[i-vow:i])
        vow=0

if ct==0:
    print("-1")


# Question 5:

import re

st=input()
k=input()

lst=[-1,-1]
ct=0
for i in range(len(st)-len(k)+1):
    f=1
    for j in range(len(k)):
        if st[i+j]!=k[j]:
            f=0
            break
    
    if f==1:
        lst[0]=i
        lst[1]=i+len(k)-1
        ct=1
        t=tuple(lst)
        print(t)


t=tuple(lst)
if ct==0:
    print(t)


# Question 6:

n=int(input())

for i in range(n):
    line=input()
    
    if len(line)==0:
        print()
        continue
    
    if line[0]=='#':
        print(line)
        continue
    
    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")
    print(line)
        

# Question 7:

import re

thousand = "(?:(M){0,3})?"
hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"

regex_pattern = r"^" + thousand + hundred + ten + unit + "$"

print(str(bool(re.match(regex_pattern, input()))))



# Question 8:

t=int(input())

while t:
    num= input()
    
    n=len(num)
    if n!=10:
        print("NO")
    else:
        f=1
        if num[0]=='7' or num[0]=='8' or num[0]=='9':
            for i in range(1,10):
                if num[i]>='0' and num[i]<='9':
                    continue
                else:
                    f=0
                    break
            
            if f==1:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
                
                
    t-=1
                


# Question 9:

import email.utils
import re

def main():
    pattern = re.compile(r"^[a-zA-Z][\w\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$")
    for i in range(int(input())):
        u_name, u_email = email.utils.parseaddr(input())
        if pattern.match(u_email):
            print(email.utils.formataddr((u_name, u_email)))

if __name__ == "__main__":
    main()


# Question 10:

import re
for i in range(int(input())):
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if matches:
        print(*matches, sep='\n')



# Question 11:


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for j in range(len(attrs)):
            print("->",attrs[j][0],">",attrs[j][1])
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])

n=int(input())
parser = MyHTMLParser()
for i in range(n):
    line=input().strip()
    parser.feed(line)
    
        

# Question 12:

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        number_of_line = len(data.split('\n'))
        if number_of_line>1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

            
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()



# Question 13:


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for j in range(len(attrs)):
            print("->",attrs[j][0],">",attrs[j][1])
    
    def handle_startendtag(self, tag, attrs):
        print (tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])

n=int(input())
parser = MyHTMLParser()
for i in range(n):
    line=input().strip()
    parser.feed(line)
    


# Question 14:

t=int(input())
while t:
    uid=input()
    s=set()
    ct_num=0
    ct_alp=0
    f=1
    
    for i in range(len(uid)):
        s.add(uid[i])
    
    if(len(uid)==10 and len(s)==10):
        for i in range(len(uid)):
                 
            if uid[i]>='0' and uid[i]<='9':
                ct_num+=1
            elif uid[i]>='A' and uid[i]<='Z':
                ct_alp+=1
            elif uid[i]>='a' and uid[i]<='z':
                continue
            else:
                f=0
                break
    else:
        f=0
                       
    if f==1 and ct_num>=3 and ct_alp>=2:
        print("Valid")
    else:
        print("Invalid")
    
    t-=1
    


# Question 15:

import re

for _ in range(int(input())):
    s = input()

    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1", s.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")


# Question 16:

regex_integer_in_range = r"[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)



# Question 17:

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

st=""
for j in range(m):
    for i in range(n):
        st+=matrix[i][j]
        
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", st))       






