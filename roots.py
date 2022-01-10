import cmath
a = float(input("Enter number"))
b = float(input("Enter number"))
c = float(input("Enter number"))
# calculate the discriminant
d = (b*b)-(4*a*c)
# find two solutions
val1 = (-b-cmath.sqrt(d))/(2*a)
val2 = (-b+cmath.sqrt(d))/(2*a)
print(val1,val2)