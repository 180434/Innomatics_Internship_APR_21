
# Question 1:

	import math
  	import cmath

   	n=input()
	t=0
	s=""
	st=""
	if(n[0]=='-'):
    		s+='-'
    		t=1 

	for i in range(t,len(n)):
   		 if(n[i]=='-' or n[i]=='+'):
       		 break 
    	s+=n[i]

	t=i

	if(n[t]=='-'):
    		st+='-'
    
	t+=1 
   
	for i in range(t,len(n)):
    		if(n[i]=='-' or n[i]=='+' or n[i]=='j'):
        		break 
    	st+=n[i]

	x=int(s)
	y=int(st)
	print(abs(complex(x,y)))
	print(cmath.phase(complex(x, y)))


# Question 2:

	import math
	import string

	pq=int(input())
	pr=int(input())
	qr=(pq*pq+pr*pr)**0.5

	ans=math.asin(pq/qr)

	ans=round(math.degrees(ans))

	ch=chr(176)

	k=str(ans)
	print(k+ch)



# Question 3:

	for i in range(1,int(input())+1):
    		print((((10**i)-1)//9)**2)



# Question 4:

	import math

	a=int(input())
	b=int(input())

	print(a//b)
	print(a%b)
	print(divmod(a,b))



# Question 5:

	import math
	a=int(input())
	b=int(input())
	m=int(input())

	print(pow(a,b))
	print(pow(a,b,m))



# Question 6:

	import math

	a=int(input())
	b=int(input())
	c=int(input())
	d=int(input())

	print(pow(a,b)+pow(c,d))



# Question 7:

	for i in range(1,int(input())): 
    		print(((pow(10,i)-1)//9)*i)
    




