file = open("myfile.txt","r")

print(file.readable())
print(file.readline())
print(file.readlines())

file.close()