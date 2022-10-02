#Approach 1:  (58 bytes, 58 chars)

a=-1
b=1
c=0
x=31
while x:
	x-=1
	print(c)
	a,b,c=b,c,b+c
