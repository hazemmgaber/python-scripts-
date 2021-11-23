import time 
## Smart Game to get what you are Guissing 
print("##############################################")
print("        ARE YOU READY FOR THE CHALLENG")
print("##############################################\n")

time.sleep(3)

print("##############################################")
print("     I WILL KNOW WHAT YOU ARE THINK ABOUT    ")
print("##############################################\n")
time.sleep(3)
print("     Select you Favourate Color from the below list     ")

color_list =  ["White" ,"Black" , "Yellow" , "Orange" , "Red"  , "Blue" , "Gray"]

for color in range(len(color_list)):
    print(color_list[color])

time.sleep(10)
print("##############################################")
print("     I can hear you  :) :) :) :)            ")
time.sleep(1)
print("     I can hear you  :) :) :) :)            ")
time.sleep(1)
print("     I can hear you  :) :) :) :)            ")
print("##############################################\n")

time.sleep(3)
print("     Let's start     !!!!!!             ")
time.sleep(3)
print("     Check the list and answer the Question      ")

Result = 0 

################# 1 ##########################
color_list1 =  ["White"  , "Yellow" ,  "Red"  ,  "Gray"]
for color in range(len(color_list1)):
    print(color_list1[color])
answer = input("     Is you color in this list ??   (y/n)        \n ")

if answer=="y":
    Result += 1
   # print(Result)

################# 2 ##########################
color_list1 =  ["Black" , "Yellow" ,  "Blue" , "Gray"]
for color in range(len(color_list1)):
    print(color_list1[color])
answer = input("  Is you color in this list ??   (y/n)         \n ")

if answer=="y":
    Result += 2
  #  print(Result)


################# 4 ##########################
color_list1 =  ["Orange" , "Red"  , "Blue" , "Gray"]
for color in range(len(color_list1)):
    print(color_list1[color])
answer = input("     Is you color in this list ??     (y/n)      \n ")

if answer=="y":
    Result += 4
   # print(Result)

#print(Result-1)

time.sleep(1)
print("m m m m m m m  !!!!!! ")
time.sleep(3)

print("##############################################")
print("Now I Know the color you Guess             ")
print("##############################################")

time.sleep(3)
print("##############################################")
print("    Your Selected Color is             ")
print("##############################################")

time.sleep(3)
print("               |            ")
print("               |            ")
print("               |            ")
print("               |            ")
print("              \/            ")
print("\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ ")
if (Result-1 <0 ):
    print( "       Are you kidding me !!!!!! ")
    print( "       You select nothing  ")
else :
    print( "       Your Color is " + color_list[Result-1])

print("/\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ \n")
print("I AM VERY SMART \n")

