#1.Vote  
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote") 
#2.Marks
marks = int(input("Enter marks: "))

if marks >= 90:
    print("You will get A* grade")
elif marks >=80:
    print("You will get A grade")
else:
    print("You will get B grade")
#3. Odd or Even
num = int(input("Enter a number:"))
if num %2 == 0:
    print("Print even")
else:
    print("Print Odd ")
#4.POsitive or Negative
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
#5.Licence eligible
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for driving licence")
else:
    print("Not eligible for driving licence")

