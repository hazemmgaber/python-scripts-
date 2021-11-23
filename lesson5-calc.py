num1 = input("Enter the 1st Number =")
operation = input("Enter one of the following Opetation + , - , * , /  : ")
num2 = input("Enter the second Number =")

def sum(num1 , num2):
    return int(num1) + int(num2)

def sub(num1 , num2):
    return int(num1) - int(num2)

def mul(num1 , num2):
    return int(num1) * int(num2)

def dev(num1 , num2):
    return int(num1) / int(num2)


if operation == "+" :
     result = sum(num1 , num2)
elif operation == "-" :
    result = sub(num1 , num2)
elif operation == "*" :
    result = mul(num1 , num2)
elif operation == "/" :
    result = dev(num1 , num2)
else:
    print("the Operation is not defined")

print("the resut is " + str(result))

