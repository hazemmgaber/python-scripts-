ilist=[1,2,3,4,5,6]
ituple=(1,2)
idictionary = {
    "jan": "January",
    "feb": "February",
    "mar": "March"
}

print(ilist.pop())
print(ilist[0])
print(ilist)
print(ilist.append(11))
print(ilist)

print(ituple)
#print(ituple(1,2))

print(idictionary.get("jan"))
print(idictionary.get("feb"))
print(idictionary.get("mar"))
print(idictionary.get("any", "please enter a valid month "))


# Initialize the list
weekdays = ["Sunday", "Monday", "Tuesday","Wednesday", "Thursday","Friday", "Saturday"]
print("Seven Weekdays are:\n")
# Iterate the list using for loop
for day in range(len(weekdays)):
    print(weekdays[day])