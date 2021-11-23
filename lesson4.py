## try IF statements 
num1 = 10
num2 = 5 
operation = input("Enter one of the following Opetation sum , sub , mult , dev  : ")

if operation == "sum" :
    result =  int(num1) + int(num2)
elif operation == "sub" :
    result =  num1 - num2 
elif operation == "mul" :
    result =  num1 * num2 
elif operation == "dev" :
    result =  num1 % num2 
else:
    print("the Operation is not defined")

print("the resut is " + str(result))