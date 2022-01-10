a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("1.add\n2.sub \n3.div \n 4.mul"))
if(c==1):
	print(a+b)
elif(c==2):
	print(a-b)
elif(c==3):
	print(a/b)
else:
	print(a*b)