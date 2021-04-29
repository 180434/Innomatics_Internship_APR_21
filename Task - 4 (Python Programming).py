

# Question 1:

	def swap_case(s):
   	   	n=len(s)
    		ans=""
    		for i in range(n):
        		if s[i]>='a' and s[i]<='z':
           			 ans=ans+ s[i].upper()
        		elif s[i]>='A' and s[i]<='Z':
            			ans=ans+ s[i].lower()
        		else:
            			ans=ans+s[i]        
    		return ans

	if __name__ == '__main__':
    		s = input()
    		result = swap_case(s)
    		print(result)


# Question 2:

	def split_and_join(line):
    		line=line.split(' ')
    		line="-".join(line)
    		return line

	if __name__ == '__main__':
    		line = input()
    		result = split_and_join(line)
    		print(result)


# Question 3:


	def print_full_name(first, last):
    		print("Hello "+first+" "+last+"! You just delved into python.")
    		return 
    

	if __name__ == '__main__':
    		first_name = input()
    		last_name = input()
    		print_full_name(first_name, last_name)


# Question 4:

	def mutate_string(string, position, character):
    		ans=string[:position]+character+string[position+1:]
    		return ans

	if __name__ == '__main__':
    		s = input()
    		i, c = input().split()
    		s_new = mutate_string(s, int(i), c)
    		print (s_new)


# Question 5:

	def count_substring(string, sub_string):
    		n=len(string)
    		m=len(sub_string)
    		ans=0
    		for i in range(n-m+1):
        		if string[i:i+m]==sub_string:
            		ans+=1
    		return ans

	if __name__ == '__main__':
    		string = input().strip()
    		sub_string =input().strip()
    
    		count = count_substring(string, sub_string)
    		print(count)


# Question 6:

	if __name__ == '__main__':
    		s = input()
    		n=len(s)
    		t=0
    		for i in range(n):
        		if (s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z') or (s[i]>='0' and s[i]<='9'):
            			t=1
            			break
    		if t==1:
       			 print("True")
    		else:
        		print("False")
        
    		t=0
    		for i in range(n):
        		if (s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z'):
            			t=1
            			break
    		if t==1:
        		print("True")
    		else:
        		print("False")
        
    		t=0
    
    		for i in range(n):
        		if (s[i]>='0' and s[i]<='9'):
            		t=1
            		break
    		if t==1:
       			print("True")
   		else:
        		print("False")
        
    		t=0
    
    		for i in range(n):
        		if s[i]>='a' and s[i]<='z':
            			t=1
            			break
    		if t==1:
        		print("True")
    		else:
        		print("False")
        
    		t=0
    
    		for i in range(n):
        		if s[i]>='A' and s[i]<='Z':
            			t=1
            			break
    		if t==1:
        		print("True")
    		else:
        		print("False")
        

# Question 7: 

	thickness = int(input())
	c = 'H'

	for i in range(thickness):
    		print ((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

	for i in range(thickness+1):
   		 print ((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

	for i in range((thickness+1)//2):
    		print ((c*thickness*5).center(thickness*6))   

	for i in range(thickness+1):
    		print ((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

	for i in range(thickness):
    		print (((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



# Question 8:

	import textwrap

	def wrap(string, max_width):
      
    		return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

	if __name__ == '__main__':
    		string, max_width = input(), int(input())
    		result = wrap(string, max_width)
    		print(result)


# Question 9:

	lst=list(map(int,input().split()))

	st=".|."
	t=".|."
	for i in range(lst[0]//2):
    		print(st.center(lst[1],'-'))
    		st+=t+t
    
	print("WELCOME".center(lst[1],'-'))

	st=st[6:]
	for i in range(lst[0]//2):
    		print(st.center(lst[1],'-'))
    		st=st[6:]
   

# Question 10:

	def print_formatted(number):
    		n=bin(number).replace("0b","")
    		t=len(n)
    
    		for i in range(1,number+1):
        		print(str(i).rjust(t),end=' ')
        		print(oct(i).replace("0o","").rjust(t),end=' ')
       			st=hex(i).replace("0x","")
        		st=st.replace("a","A")
        		st=st.replace("b","B")
        		st=st.replace("c","C")
        		st=st.replace("d","D")
        		st=st.replace("e","E")
        		st=st.replace("f","F")
        		print(st.rjust(t),end=' ')
        		print(bin(i).replace("0b","").rjust(t),end=' ')
        		print()

	if __name__ == '__main__':
    		n = int(input())
    		print_formatted(n)


# Question 11:

	def print_rangoli(size):
    		t=size*2-1
    		t=2*t-1
    
    		c= 97+size-1
    		ch=chr(c)
    
    		for i in range(size-1):
        		print(ch.center(t,'-'))
        		c-=1
        		n=len(ch)
        		st=ch[0:(n//2)+1]
        		ch=st+"-"+chr(c)+"-"+st[::-1]
    
    		print(ch)
    
    		for i in range(size-1):
        		n=len(ch)
        		ch=ch[0:(n//2)-1]+ch[(n//2)+3:]
        		print(ch.center(t,'-'))
        

	if __name__ == '__main__':
    		n = int(input())
    		print_rangoli(n)


# Question 12:


	import math
	import os
	import random
	import re
	import sys

	def solve(s):  
    
    		ans=""
    
    		f=0
    		for i in range(len(s)):
        		if s[i]==' ':
            			ans+=s[i]
            			f=0
        		elif f==0:
           			ch=s[i]
            			ch=ch.upper()
            			ans+=ch
            			f=1
        		else:
            			ans+=s[i]
           
    		return ans

	s = input()
	result = solve(s)
	print(result)

   

# Question 13:

	def minion_game(st):
    		n=len(st)
    
    		stuart=0
    		kevin=0
    		for i in range(n):
        		if st[i]=='A' or st[i]=='E' or st[i]=='I' or st[i]=='O' or st[i]=='U':
            			kevin+=(n-i)
        		else:
            			stuart+=(n-i)
    
    		if(stuart>kevin):
        		print("Stuart",stuart)
    		elif kevin>stuart:
        		print("Kevin",kevin)
    		else:
        		print("Draw")

	if __name__ == '__main__':
    		s = input()
    		minion_game(s)


# Question 14:

	def merge_the_tools(string, k):
   		 n=len(string)
    
    		for i in range(0,n,k):
        		st=string[i:i+k]
        		s=set()
        		ans=""
        		for j in range(k):
            			if st[j] in s:
                			continue
            			else:
                			ans+=st[j]
                			s.add(st[j])
        
        		print(ans)
                

	if __name__ == '__main__':
    		string, k = input(), int(input())
    		merge_the_tools(string, k)

