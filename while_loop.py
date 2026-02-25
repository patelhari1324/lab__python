#1. print number from 1 to 5 
i = 1
while i <= 5:
    print(i)
    i += 1 
    
#2.sum of numbers take user input
n = int(input("Enter a number: "))
sum_numbers = 0
i = 1

while i <= n:
    sum_numbers += i  
    i += 1 
    print("Sum of numbers:", sum_numbers)


#3.print odd number betweeen 1 to 20
   
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

#4.print table of 4
    
i = 1
while i <= 10:
    print("4 x", i, "=", 4 * i)
    i = i + 1
  

#5.print reverse number 
number = 10

print("Reversing the number 10:")

while number != 0:
    digit = number % 10     
    print(digit, end="")
    number = number     
     
#6. find largest number in list  
    numbers = [12, 34, 56, 78, 45, 23]
largest = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1
print("The largest number is:", largest)  
    
#7.print even nuber between 1 and 20
i = 2
while i <= 20:
    print(i)
    i += 2 