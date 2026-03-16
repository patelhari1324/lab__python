#1.postive indexing
import array
arr = array('i', [10, 20, 30, 40, 50])
    print(arr[0])  
    print(arr[2])  
    print(arr[4])  

#2.negavite indexing
import array
arr = array('i', [10, 20, 30, 40, 50])  
    print(arr[-1])  
    print(arr[-2])  
    print(arr[-5])  
#3.diagram indexing
Array: [10, 20, 30, 40, 50]
Indexes:  0,   1,   2,   3,   4
Negative Indexes: -5, -4, -3, -2, -1

#4.modifiying elements using index
import array
arr = array('i', [10, 20, 30, 40, 50])
arr[2] = 35  
    print(arr)    

#5.index error
import array
arr = array('i', [10, 20, 35, 45, 50]) 
    print(arr[5])  