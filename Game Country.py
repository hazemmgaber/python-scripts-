import time 
import os

os.system('cls||clear')

## Smart Game to get what you are Guissing 
print("##############################################")
print("        ARE YOU READY FOR THE CHALLENG")
print("##############################################\n")

time.sleep(3)

print("##############################################")
print("     I WILL KNOW WHAT YOU ARE THINK ABOUT    ")
print("##############################################\n")
time.sleep(3)
print("     Select you Favourate country from the below list     ")

country_list =  ["Saudia","Qatar","Emarite","Yaman","Palastine","China","Japan","Koreia","Netherland","Rasia","France","Egypt","Germany ","USA","UK"]

for country in range(len(country_list)):
    print(country_list[country])

time.sleep(10)
print("##############################################")
print("     I can hear you  :) :) :) :)            ")
time.sleep(1)
print("     I can hear you  :) :) :) :)            ")
time.sleep(1)
print("     I can hear you  :) :) :) :)            ")
print("##############################################\n")
time.sleep(3)
os.system('cls||clear')
print("     Let's start     !!!!!!             ")
time.sleep(3)
print("     Check the list and answer the Question      ")

Result = 0 

################# 1 ##########################
country_list1 =  ["Saudia","Emarite","Palastine","Japan","Netherland","France","Germany ","UK"]
for country in range(len(country_list1)):
    print(country_list1[country])
answer = input("     Is you country in this list ??   (y/n)        \n ")

if answer=="y":
    Result += 1
   # print(Result)
os.system('cls||clear')

################# 2 ##########################
country_list1 =  ["Qatar","Emarite","China","Japan","Rasia","France","USA","UK"]
for country in range(len(country_list1)):
    print(country_list1[country])
answer = input("  Is you country in this list ??   (y/n)         \n ")

if answer=="y":
    Result += 2
  #  print(Result)
os.system('cls||clear')

################# 4 ##########################
country_list1 =  ["Yaman","Palastine","China","Japan","Egypt","Germany ","USA","UK"]
for country in range(len(country_list1)):
    print(country_list1[country])
answer = input("     Is you country in this list ??     (y/n)      \n ")

if answer=="y":
    Result += 4
   # print(Result)
os.system('cls||clear')

################# 8 ##########################
country_list1 =  ["Koreia","Netherland","Rasia","France","Egypt","Germany ","USA","UK"]
for country in range(len(country_list1)):
    print(country_list1[country])
answer = input("     Is you country in this list ??     (y/n)      \n ")

if answer=="y":
    Result += 8
   # print(Result)
time.sleep(1)
os.system('cls||clear')
#print(Result-1)


print("m m    ")
time.sleep(1)
os.system('cls||clear')
print("m m m m   ")
time.sleep(1)
os.system('cls||clear')
print("m m m m m m  ")
time.sleep(1)
os.system('cls||clear')
print("m m m m m m m m m   ")
time.sleep(1)
os.system('cls||clear')
print("m m m m m m m m m m m   ")
time.sleep(1)
os.system('cls||clear')
print("m m m m m m m m m m m m m  ")
time.sleep(1)
os.system('cls||clear')
print("m m m m m m m m m m m m m m m  !!!!!! ")

time.sleep(3)

print("##############################################")
print("Now I Know the country you Guess             ")
print("##############################################")

time.sleep(3)
print("##############################################")
print("    Your Selected country is             ")
print("##############################################")

time.sleep(3)
print("               |            ")
print("               |            ")
print("               |            ")
print("               |            ")
print("              \/            ")
print("\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \n")
if (Result-1 <0 ):
    print( "       Are you kidding me !!!!!! ")
    print( "       You select nothing  ")
else :
    print( "       Your country is " + country_list[Result-1] )

print("\n /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ \n")
print("I AM VERY SMART \n")

