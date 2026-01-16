Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print("Welcome to Python Programming!")

Welcome to Python Programming!

#2
print("Rajesh Kumar")
print("\tFlat No. 101, Sunshine Apartments")
print("\tMG Road, Sector 15")
print("\tRajkot")
print("\tPincode: 360004")
print("\tIndia")

SyntaxError: multiple statements found while compiling a single statement

print("Rajesh Kumar")
print("\tFlat No. 101, Sunshine Apartments")
print("\tMG Road, Sector 15")
print("\tRajkot")
print("\tPincode: 360004")
print("\tIndia")

SyntaxError: multiple statements found while compiling a single statement
print("Rajesh Kumar")
Rajesh Kumar
print("Rajesh Kumar","\tFlat No. 101, Sunshine Apartments","\tMG Road, Sector 15"
,"\tRajkot","\tPincode: 360004","\tIndia")
Rajesh Kumar 	Flat No. 101, Sunshine Apartments 	MG Road, Sector 15 	Rajkot 	Pincode: 360004 	India

#3
a = 150
b = 120.50

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)

SyntaxError: multiple statements found while compiling a single statement
a = 150
 b = 120.50
 
SyntaxError: unexpected indent
print("Addition =", a + b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print("Addition =", a + b)
NameError: name 'b' is not defined
a = 150
b = 120.50
print("Addition =", a + b)
Addition = 270.5
print("Subtraction =", a - b)
Subtraction = 29.5
print("Multiplication =", a * b)
Multiplication = 18075.0
print("Division =", a / b)
Division = 1.2448132780082988

#4
radius = float(input("Enter radius: "))
Enter radius: circumference = 2 * 3.14 * radius
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    radius = float(input("Enter radius: "))
ValueError: could not convert string to float: 'circumference = 2 * 3.14 * radius'
radius = float(input("Enter radius: "))
Enter radius: 
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    radius = float(input("Enter radius: "))
ValueError: could not convert string to float: ''

radius = float(input("Enter radius: "))
Enter radius: 
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    radius = float(input("Enter radius: "))
ValueError: could not convert string to float: ''
Enter radius:3.14*radius*radius
SyntaxError: invalid syntax
radius = float(input("Enter radius: "))
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius

print("Area of circle =", area)

print("Circumference of circle =", circumference)
Enter radius:5.2
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: invalid syntax

radius = float(input("Enter radius: "))
Enter radius: 5.5
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius

print("Area of circle =", area)
Area of circle = 94.985
print("Circumference of circle =", circumference)
Circumference of circle = 34.54

#5
P = float(input("Enter Principal amount: "))
Enter Principal amount: 500.6
R = float(input("Enter Rate of interest: "))
Enter Rate of interest: 450.82
T = float(input("Enter Time (in years): "))
Enter Time (in years): 850.12
SI = (P * R * T) / 100
print("Simple Interest =", SI)
Simple Interest = 1918554.9985904

#6
length = float(input("Enter length: "))
Enter length: 450
>>> width = float(input("Enter width: "))
Enter width: 500
>>> perimeter = 2 * (length + width)
>>> print("Perimeter of rectangle =", perimeter)
Perimeter of rectangle = 1900.0
>>> 
>>> #7
>>> length = float(input("Enter length: "))
Enter length: 5000
>>> width = float(input("Enter width: "))
Enter width: 100
>>> area = length * width
>>> perimeter = 2 * (length + width)
>>> print("Area of rectangle =", area)
Area of rectangle = 500000.0
>>> 
>>> #8
>>> a = float(input("Enter side a: "))
Enter side a: 750
>>> b = float(input("Enter side b: "))
Enter side b: 826
>>> c = float(input("Enter side c: "))
Enter side c: 324
>>> perimeter = a + b + c
>>> print("Perimeter of triangle =", perimeter)
Perimeter of triangle = 1900.0
>>> 
>>> #8
>>> side = float(input("Enter side of square: "))
Enter side of square: 9
>>> area = side * side
>>> perimeter = 4 * side
>>> print("Area of square =", area)
Area of square = 81.0
>>> print("Perimeter of square =", perimeter)
Perimeter of square = 36.0
>>> 
>>> #10
>>> side = float(input("Enter side of square: "))
... 
Enter side of square: 45
>>> perimeter = 4 * side
... 
>>> print("Perimeter of square =", perimeter)
Perimeter of square = 180.0
