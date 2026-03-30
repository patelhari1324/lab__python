src = open("one.txt", "r")
data = src.read()
src.close()

dst = open("taskwhile.txt", "w")
dst.write(data)
dst.close()

print("File copied successfully.")