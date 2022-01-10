a=int(input("Enter a year"))
if (a % 400 == 0):
	print("It is leap year")
elif (a % 100 == 0):
	print("It is not leap year")
elif (a% 4 == 0):
	print("It is leap year")
else:
	print("Not a leap year")
