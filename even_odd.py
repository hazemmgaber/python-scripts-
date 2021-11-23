''' 
input the range of the numbers from - to 
loop in the rang and write the number and is it even or odd 
even the result of / 2 = zero 
odd the result of / 2 != zero 

'''

x= input("start of the range")
y= input("End  of the range")
i = x

#print(i)

while ( int(i) >= int(x) and int(i) <= int(y)):
    result = int(i) % 2 
#print(result)
    if result == 0 :
        print(str(i) + " The Number of Even  ")
        i = int(i) +1
    else:
        print(str(i) + " The Number of Odd  ")
        i =  int(i) +1 
