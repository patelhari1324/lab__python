Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1.String
>>> x="hello world"
>>> print(x)
hello world
>>> 
>>> #2.integer
>>> x=20
>>> print(x)
20
>>> 
>>> #3.float
>>> x=20.5
>>> print(x)
20.5
>>> 
>>> #4.complex
>>> x=lj
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x=lj
NameError: name 'lj' is not defined
>>> x=tj
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x=tj
NameError: name 'tj' is not defined
>>> print(x)
20.5
>>> x=1j
>>> print(x)
1j
>>> 
>>> #5.List
>>> x["apple","banana","cherry"]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x["apple","banana","cherry"]
TypeError: 'complex' object is not subscriptable
>>> x=["apple","banana","cherry"]
>>> print(x)
['apple', 'banana', 'cherry']
>>> 
>>> #6.list
>>> x=("apple","banana","cherry")
>>> print(x)
('apple', 'banana', 'cherry')
>>>  #6.lit
>>> x=("apple","banana","cherry")
>>> print(x)
('apple', 'banana', 'cherry')
>>> #6.tuple
SyntaxError: invalid syntax
>>> x=("apple","banana","cherry")
>>> print(x)
('apple', 'banana', 'cherry')
>>> 
>>> #7.none
>>> x=none
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x=none
NameError: name 'none' is not defined
>>> x=none
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    x=none
NameError: name 'none' is not defined
>>> print(x)
('apple', 'banana', 'cherry')
>>> #8.dict
>>> x={"apple","banana","cherry"}
>>> print(x)
{'apple', 'cherry', 'banana'}
>>> 
>>> #9.bool
>>> x = True
>>> print(x)
True
>>> 