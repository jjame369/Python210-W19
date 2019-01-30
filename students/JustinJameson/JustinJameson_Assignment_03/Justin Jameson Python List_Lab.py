#**************************
#Title: file name
#Desc: describe you work
#Chnage Log: (Who, When, What)
# Justin Jameson, 01162019, created template
"""Series 1
    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Display the list (plain old print() is fine…).
    Ask the user for another fruit and add it to the end of the list.
    Display the list.
    Ask the user for a number and display the number back to the user and the fruit corresponding to that number
    (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    Add another fruit to the beginning of the list using “+” and display the list.
    Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.

   Series 2
    Using the list created in series 1 above:
    Display the list.
    Remove the last fruit from the list.
    Display the list.
    Ask the user for a fruit to delete, find it and delete it.
    (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

   Series 3
    Again, using the list from series 1:
    Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit
    all lowercase).
    For each “no”, delete that fruit from the list.
    For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values
    (a while loop is good here)
    Display the list.

   Series 4
    Once more, using the list from series 1:
    Make a new list with the contents of the original, but with all the letters in each item reversed.
    Delete the last item of the original list. Display the original list and the copy.
"""

# **********************************************************************************************************************


#-- Data --#
# declare variables and constants
origList = ['Apples', 'Pears', 'Oranges', 'Peaches']
# newFruit = a variable to use for appending new fruit to the list.
# fr    uitNumber = the assumed value of the fruit.


#-- Processing Series 1: ***********************************************************************************--#


def AddFruitEndOfList(List1, Input1):
    """
    Adding a fruit to the end of the list.
    :param List1: passed in default list of fruit.
    :return: a new fruit lis added to the end of the origonal list.
    """
    List1 = List1 + [Input1]
    return List1

# End of AddFruitEndOfList().
def FruitByIndex(List1, Input1):
    """
    print out the fruit based on index.
    :param List1:
    :return:
    """

    requestedFruit = (List1[int(Input1) - 1])
    return requestedFruit

def NewFruitBegin(List1,newEntry1):
    """
    add a fruit to the beginning of the list with a + and display
    :param List1: passed in default list of fruit.
    :return: new list with the fruit added to the beginning of the list.
    """

    List1 = [newEntry1] + List1
    return List1

# End of NewFruitBegin()

def AddFruitUsingInsert(List1, newEntry1):
    """
    Add another fruit to the beginning of the list using insert() and display the list.
    :param List1: passed in default list of fruit.
    :return: new fruit added to the front of the list.
    """

    List1.insert(0, newEntry1)
    return List1
# End of AddFruitUsingInsert()

def ReturnFruitsBeginWithP(List1):
    """
    Display all the fruits that begin with “P”, using a for loop.
    :param List1: passed in default list of fruit.
    :return: list of fruits that begin with P.
    """
    List2 = ""
    for fruit in List1:
        seq = fruit.lower()
        if seq[0] == "p" in seq:
           List2 = List2.__add__("\n"+seq)
    return List2
#************************************************************************* END SERIES ONE PROCESSING********************
#****** Processing SERIES TWO ******************************************************************************************
#************************************************************************* END SERIES TWO PROCESSING********************
#****** Processing SERIES THREE ****************************************************************************************
#************************************************************************* END SERIES THREE PROCESSING******************
#****** Processing SERIES Four  ****************************************************************************************
#************************************************************************* END SERIES FOUR PROCESSING*******************


# perform tasks
#-- Presentation (Input/Output) --#

# # Output
# print("\n\n\n******************************* SERIES 1 *************************************************************")
# # Display the list.
# print("Your current list of fruit is: ", origList)
#
# # get user input
# newFruit = input("Please add another fruit to the list. ")
# print("The fruit "+newFruit+" has been added the end of the list, but not saved.\n",
#       AddFruitEndOfList(origList, newFruit))
#
# fruitNumber = input("Starting from the Left, count the fruit from 1 to n."
#                     "Then enter the number of your 'choice' fruit. ")
# print("Number "+fruitNumber+" is a: ", FruitByIndex(origList,fruitNumber))
# print("The fruit "+newFruit+" has been added to the beginning of the list using a plus sign, but has not been saved.",
#       NewFruitBegin(origList, newFruit))
# print("The fruit "+newFruit+" has been added to the beginning of the list using insert, but has not been saved. ",
#       AddFruitUsingInsert(origList, newFruit))
# print("The following fruits begin with the letter 'p'.\n", ReturnFruitsBeginWithP(origList))
#
# print("\n\n\n*******************************  SERIES 2  *************************************************************")
# # Display the list
# print(origList)
# # copy the list for series two.
# origListSeries2 = origList
# # remove last item on the list
# origListSeries2.remove('Peaches')
# # Display the list
# print(origListSeries2)
# origListSeries2.remove(input("enter a fruit from the list to remove: "))
# print(origListSeries2)
# print("\n\n\n*******************************  SERIES 3  *************************************************************")
# # creating the like list
#
# likeFruitsList = origList
# for items in likeFruitsList[:]: # https://docs.python.org/3/reference/compound_stmts.html seen note in 8.3. temp slice!
#     fruitQuestion = input("Do you like, " + items.lower() + " yes/no?")
#     if fruitQuestion.lower() == "no":
#         likeFruitsList.remove(items)
#         continue
#     elif fruitQuestion.lower() == "yes":
#         continue
#     else:
#         print("Not a valid Entry")
#
# print (likeFruitsList)
#

print("\n\n\n*******************************  SERIES 4  *************************************************************")
origList = ['Apples', 'Pears', 'Oranges', 'Peaches']
origListRevSpell = ""
for Fruit in origList:
    fruitNameReversed = ""
    for splice in range(len(Fruit)):
        if splice == 0:
            fruitSplice0 = Fruit[splice]
            continue
        fruitNameReversed = fruitNameReversed + Fruit[(-splice)]
        fruitNameRevComplete = (fruitNameReversed + fruitSplice0)
    origListRevSpell = origListRevSpell + fruitNameRevComplete + " "

fList = []
for i in origListRevSpell.split(" "):
    if i == " ":
        break
    fList.insert(0,i)
fList.reverse()
fList.remove('sehcaeP')
print(fList)
print(origList)