#**************************
#Title: file name
#Desc: describe you work
#Chnage Log: (Who, When, What)
# Justin Jameson, 01162019, created template
#**************************


#-- Data --#
# declare variables and constants
dictInfo = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print(dictInfo)
dictInfo.pop("cake")
print(dictInfo)
dictInfo["fruit"] = "Mango"
print(dictInfo)
for k in dictInfo:
    print(k)
print(dictInfo.keys())
print(dictInfo.values())
print(dictInfo.items())

ifKey = input("What Key would you like to check? ")
if ifKey in dictInfo:
    print("yes", ifKey, "is a Key.")
else: print(ifKey, "is not a Key")

ifValue = input("What Key would you like to check? ")
if ifValue in dictInfo.values():
    print("yes", ifValue, "is a Value.")
else: print(ifValue, "is not a Value")


#-- Processing --#
# perform tasks
#-- Presentation (Input/Output) --#
# get user input
# send program output
