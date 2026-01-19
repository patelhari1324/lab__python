Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1
>>> p=float(input("enter principal amount:"))
enter principal amount:500
>>> r=float(input("enter rate of interset:"))
enter rate of interset:850.30
>>> t=float(input("enter timein yerars:"))
enter timein yerars:4.8
>>> si=(p*r*t)/100
>>> print("simple interst =",si)
simple interst = 20407.2
>>> 
>>> #2
>>> for i in range(1,6):
	print(i)

	
1
2
3
4
5
>>> 
>>> #3
>>> for i in range(1,3):
	print(i)

	
1
2
>>> a = 5
>>> b = 8
>>> print(max(a,b))
8
>>> 
>>> #4
>>> my_string="hello,pyhton!"
>>> length = len(my_string)
>>> print(length)
13
>>> 
>>> #5
>>> print("welcome")
welcome
>>> 
>>> #6
>>> text = "Pyhton"
>>> print(text[0])
P
>>> #7
>>> print(text[5])
n
>>> #8
>>> n = int(input("enter number:"))
enter number:5
>>> print(["Negative or zero","postive"][n > 0])
postive
>>> -9
-9
>>> 
>>> #9
>>> a = int(input("enter first number"))
enter first number78
>>> b = int(input("enter second number:"))
enter second number:45
>>> c = int(input("enter third number:"))
enter third number:39
>>> print("sum=", a+b+c)
sum= 162
>>> 
>>> #10
>>> n = int(input("enter text:"))
enter text:print("square=",n*n)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    n = int(input("enter text:"))
ValueError: invalid literal for int() with base 10: 'print("square=",n*n)'
>>> n = int(input("enter text:"))
enter text:48
>>> print("square=",n*n)
square= 2304
>>> 