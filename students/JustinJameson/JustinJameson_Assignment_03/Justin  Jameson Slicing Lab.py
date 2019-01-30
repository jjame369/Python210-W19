#**************************
#Title: Justin Jameson Slicing Lab.py
#Desc: Write some functions that take a sequence as an argument, and return a copy of that sequence:
# with the first and last items exchanged.
# with every other item removed.
# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
# with the elements reversed (just with slicing).
# with the last third, then first third, then the middle third in the new order.
# NOTE: These should work with ANY sequence – but you can use strings to test, if you like.
#   Sequence: an ordered collection of objects.
#   Object: an encapsulation of variables and functions into a single entity
#Chnage Log: (Who, When, What)
# Justin Jameson, 01272019, Pseudo Code entered, beginning scripting.
#**************************


#-- Data --#
# declare variables and constants
# origList = user input of a sequence to be evaluated.


#-- Processing --#
# perform tasks
def RunFunctions(seq):
    """
    This function runs all the other functions and outputs back to the presentation section.
    :param seq: defined by user input and to be evaluated in the following functions.
    :return: all functions required for the assignment.
    """
    return (Exchange1stLast(seq)),(EveryOtherRemoved(seq)), (First4Last4(seq)), (Reversed(seq)),\
           (ReorderedThirds(seq))

# End of function RunFunctions()

def Exchange1stLast(seq):
    """
    Take a sequence as an argument, and return a copy of that sequence with the first and last items exchanged.
    :param seq: user input passed from function 'RunFunctions(origList)'.
    :return: option1 print out of the function.
    """
    option1 = (seq[-1:]+seq[1:-1]+seq[0:1])
    return (option1)
# End of function Exchange1stLast()

def EveryOtherRemoved(seq):
    """
    take a sequence as an argument, and return a copy of that sequence with with every other item removed.
    :param seq: user input passed from function 'RunFunctions(origList)'.
    :return: option2 print out of the function.
    """
    # Define variable option2.
    option2 = ""
    for i in range(len(seq)):
        if i % 2 == 0:
            option2 = option2 + seq[i]
    return option2

  #  End of function EveryOtherRemoved()

def First4Last4(seq):
    """
    take a sequence as an argument, and return a copy of that sequence with the first 4 and the last 4 items removed,
    and then every other item in the remaining sequence.
    :param seq: user input passed from function 'RunFunctions(origList)'.
    :return: option3 print out of the function.
    """

    # remove first and last four of the sequence.
    option3 = seq[4:-4]
    # Define option3b
    option3b = ""
    for i in range(len(option3)):
        if i % 2 == 0:
            option3b = option3b + option3[i]
    return option3, option3b

# End of function First4Last4(origList)

def Reversed(seq):
    """
    take a sequence as an argument, and return a copy of that sequence with the elements reversed (just with slicing).
    :param seq: user input passed from function 'RunFunctions(origList)'.
    :return: aListb, and 4b print out of the function.
    """
    option4 = ""
    for i in range(len(seq)):
        if i == 0:
            option4b = seq[i]
            continue
        option4 = option4 + seq[(-i)]
    return (option4 + option4b)

#  End of function Reversed()
def ReorderedThirds(seq):
    """
    take a sequence as an argument, and return a copy of that sequence the last third, then first third, then the
    middle third in the new order.
    :param seq: user input passed from function 'RunFunctions(origList)'.
    :return: option5 print out of the function.
    """
    option5First3rd = (seq[0:((len(seq)) // 3)])
    option5Middle3rd = (seq[(((len(seq)) // 3)):(((len(seq) - (len(seq)) // 3)))])
    option5Last3rd = (seq[(len(seq) - (len(seq)) // 3):len(seq)])
    return (option5Last3rd+option5First3rd+option5Middle3rd)
    #  End of function ReorderedThirds()


#-- Presentation (Input/Output) --#
# get user input
seq = input("Enter a sequence you would like to evaluate. ")
print(RunFunctions(seq))
input("press enter to exit:")

# send program output
