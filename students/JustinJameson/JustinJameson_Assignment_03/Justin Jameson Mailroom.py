#**************************
#Title: Justin Jameson Mailroom.py
#Desc: command-line script that is executable. The script should accomplish the following goals:
# 1) have a data structure that holds a list of your donors and a history of the amounts they have donated.
# This structure should be populated with at least five donors, with 1 to 3 donations each.
# storage of the data structure will be in the global namespace.
# 2) The script should prompt the user to choose from a menu of 3 actions:
#   “Send a Thank You”
#   “Create a Report”
#   “quit”
#Chnage Log: (Who, When, What)
# Justin Jameson, 01282019, created file
#**************************

import sys  # imports go at the top of the file

#-- Data --#
# declare variables and constants
donorTableHeading = ("First Name", "Last Name", "Donation Totals")
listOfDonors = (("Dana Spam", 39, 700500, 0), ("Jay Byrd", 10, 343553235, 0), ("Jo Jo", 6, 2353, 0),
                ("Kilee Boss", 235235124, 0), ("Katee Pie", 3, 0, 0), ("Ethon George", 25, 23423443, 52352))
sortedListOfDonors = sorted(listOfDonors,key=lambda key2: key2[1])

mainPrompt = "\n".join(("Be grateful you have a job!",
          "Please choose from below options:",
          "1 - Send a Thank You note",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

thankYouPrompt ="\n".join(("Lets get that Thank You note done!",
          "Please choose from below options:",
          "1 - Enter the recipients full name.",
          "2 - Review the List of donors.",
          "3 - Quit",
          ">>> "))


#-- Processing --#



def Send_a_ThankYou(thankYouPrompt):
    """

    :param thankYouPrompt:
    :return:
    """
    while True:
        response = input(thankYouPrompt)  # continuously collect user selection
        # redirect to feature functions based on the user selection
        if response == "1":
            UpdateListOfDonors(listOfDonors)
        elif response == "2":
            # Show a list of the donor names and re-prompt.
            # TODO: make the list of donors easier to read. Can you call the list from function 'create a report fun'?
            Creat_A_Report(sortedListOfDonors)
        elif response == "3":
            break
        else:
            print("Not a valid option!")


def UpdateListOfDonors(seq):
    # prompt user for a Full Name.
    donorFullName = input("Enter the donors full name: "),
    # TODO:Check, evaluation worked in test environment, test to see if it works in function.
    # check to see if the name exists
    for i in seq[:]:
        if donorFullName in i: #TODO: running out of time, this for loop should look at the tuples inside and eval. not working.
            donorNameAdd= i.index(donorFullName)  # If the user types a name in the list, use it.
            print(f"Thank you {seq[donorNameAdd]}")
        else:  # If the user types a name not in the list, add that name to the data structure and use it.
            # Once a name has been entered, prompt for a donation amount,
            # and add that amount to the donation history of the selected user.
            donorDonationAmount = input("Enter the amount of the donation: "),
            donorData = donorFullName + donorDonationAmount
            seq += donorData
            print(f"Thank you {donorFullName}, your donation of {donorDonationAmount} is appreciated!")
            break


def Creat_A_Report(rTable):
    """
    Create a Report
    1) print a list of your donors, sorted by total historical donation amount.
    2) Include Donor Name, total donated, number of donations, and average donation amount as values in each row.
    3) do not print out all of each donor’s donations, just the summary info.
    4) Using string formatting, format the output rows as nicely as possible. The end result should be
    tabular (values in each column should align with those above and below).
    5) After printing this report, return to the original prompt.
    6) At any point, the user should be able to quit their current task and return to the original prompt."""
    for r in rTable:
        if r == donorTableHeading:
            print(f"|{r[0]:^15}|{r[1]:^15}|{r[2]:^15}|")
        else:
            print(f"|{r[0]:<15}|{r[1]:<15}|{r[2]:<15}|")
    # TODO: Sort: I know you said don't use lambda, but I cant figure out the getitem way.
    #  print(sorted(listOfDonors,key=lambda key2: key2[1]))

def exit_program():
    print("Thank you for using this program, bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(mainPrompt)  # continuously collect user selection
        # redirect to feature functions based on the user selection
        if response == "1":
            Send_a_ThankYou(thankYouPrompt)
        elif response == "2":
            Creat_A_Report(sortedListOfDonors)
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")




# perform tasks
#-- Presentation (Input/Output) --#
# get user input


# send program output


if __name__ == "__main__":
    # guards against Justin Jameson Mailroom code running automatically if this module is imported
    main()
