Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1.Int
>>> age=int(input("Enter your age: "))
Enter your age: 19
>>> print("Age:", age)
Age: 19
>>> 
>>> #2.Float
>>> price = float(input("Enter number in decimal value: "))
Enter number in decimal value: 123.45
>>> print("price:",price)
price: 123.45
>>> 
>>> #3.Boll
>>> name = input("Enter your name: ")
Enter your name: Ajay
>>> print("Name:",name)
Name: Ajay
>>> 
>>> #4.str
>>> is_student:input("Are you a student? (True/False): ")
Are you a student? (True/False): True
>>> print(("Student:", is_student))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(("Student:", is_student))
NameError: name 'is_student' is not defined
>>> is_student = input("Are you a student? (True/False): ")
Are you a student? (True/False):  True
>>> print("Student:", is_student)
Student:  True
>>> 