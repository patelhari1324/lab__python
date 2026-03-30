#1. Using read() method to read a file
f = open("one.txt", "r")  
data = f.read()            
print("file content:", data)  
f.close()                

#2. Reading specific number of characters
f = open("one.txt", "r")  
data = f.read(10)          
print("first part:", data)  
f.close() 

#3.redlines()
f=open("one.txt","r")
lines=f.readlines()
    print("List of lines:",len(lines))
f.close() 

#4.readline()-read one line
f=open("one.txt","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line1:",line1)
print("line2:",line2)
print("line3:",line3)
f.close()

#5.reading specific line
f=open("one.txt","r")
lines=f.readlines()
print(lines[1].strip())
f.close()