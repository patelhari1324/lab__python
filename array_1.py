#1. len () -number of elements 
import array

a = array.array('i', [10,20,30,40,50])
print(len(a))

#2.apped()- add element at the end of the array
import array
arr = array.array('i',[10,20,30])
arr.append(40)
print(arr)

#3.insert() - add element at the specified position
import array

arr = array.array('i', [10,20,40])
arr.insert(2, 30)

print(arr)

#4. remove() - remove the first occurrence of the specified element
import array
arr = array.array('i',[10,20,30,20,40])
arr.remove(20)
print(arr)

#5. pop() - remove and return the element at the specified position
import array

arr = array.array('i', [10,20,30,40])
x = arr.pop()

print("removed:", x)
print(arr)