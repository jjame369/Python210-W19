# **************************
# Title: Justin Jameson Mailroom 2.py
# Desc: command-line script that is executable. The script should accomplish the following goals:
# 1) have a data structure that holds a list of your donors and a history of the amounts they have donated.
# This structure should be populated with at least five donors, with 1 to 3 donations each.
#
# 2) The script should prompt the user to choose from a menu of 3 actions:
#   “Send a Thank You”
#   “Create a Report”
#   “quit”
# Change Log: (Who, When, What)
# Justin Jameson, 01282019, created file
# Justin Jameson, 01282019,
# 1. Modified listOfDonors to be a dictionary.
# 2. Modified report to display format properly.
# 3. Added function to save bulk emails to txt files.
# **************************

import sys  # imports go at the top of the file

# -- Data -- #
# declare variables and constants
# heading for the table
donorTableHeading = ['First/Last Name', 'Donation Totals', 'Number of donations', 'Average donation amount']
# Include Donor Name, total donated, number of donations, and average donation amount as values in each row.
listOfDonors = {"Dana Spam": [39, 700500, 10], "Jay Byrd": [10, 343553235, 90], "Jo Jo": [6, 2353],
                "Kilee Boss": [235235124], "Katee Pie": [3, ], "Ethon George": [25, 23423443, 52352]}

# -- Processing -- #
# Running Prompts: #


mainPrompt = "\n".join(("Be grateful you have a job!",
                        "Please choose from below options:",
                        "1 - Send a Thank You note",
                        "2 - Create a Report",
                        "3 - Send a letter to all Donors",
                        "4 - Quit",
                        ">>> "))

thankYouPrompt = "\n".join(("Lets get that Thank You note done!",
                            "Please choose from below options:",
                            "1 - Enter the recipients full name.",
                            "2 - Review the List of donors.",
                            "3 - Quit",
                            ">>> "))

# Begin Functions.


def main(mprompt, mdict):
    while True:
        response = int(input(mprompt))  # continuously collect user selection
        v0 = margdict.get(response)
        try:
            mdict.get(response)(v0[0], v0[1])
        except KeyError:
            print("You must input an integer.")


# End of main function.

def send_a_thankyou(typrompt, tdict):
    """

    :param typrompt:
    :param tdict:
    :return:
    """
    while True:
        response = int(input(typrompt))  # continuously collect user selection
        v0 = tydict.get(response)
        try:
            tdict.get(response)(v0[0],v0[1])

        except KeyError:
            print("You must input an integer.")

# End of Send a Thank you function.

# perform tasks #


def UpdateListOfDonors(lDonors, placeholder):
    # prompt user for a Full Name.
    donorFirstName = input("Enter the donors First name or enter to exit: ")
    donorLastName = input("Enter the donors Last name: ")
    # prompt for a donation amount and add it to the donation history of the selected user.
    donorDonationAmount = int(input("Enter the Donation amount: "))
    donorFullName = donorFirstName.capitalize() + " " + donorLastName.capitalize()
    # check to see if the name exists
    if donorFullName in lDonors:
        for v in lDonors.values():
            v.append(donorDonationAmount)
    # If the name is not in the dict, add that name and use it.
    else:
        lDonors[donorFullName] = [donorDonationAmount]
    ThankYouLetter(donorFirstName, donorDonationAmount)
    main(mainPrompt,dictMainPrompt)


def ThankYouLetter(fName, dAmount):
    print(f"Thank you {fName}, your donation of $ {dAmount} is appreciated!")

# End of ThankYouLetter function.

def Create_A_Report(rHeading, rTable):
    """ Create a Report
    1) print a list of your donors, sorted by total historical donation amount.
    2) Include Donor Name, total donated, number of donations, and average donation amount as values in each row.
    3) do not print out all of each donor’s donations, just the summary info.
    4) Using string formatting, format the output rows as nicely as possible. The end result should be
    tabular (values in each column should align with those above and below).
    5) After printing this report, return to the original prompt.

    :param rHeading: Sequence passed in to represent the header information of the table, currently a list.
    :param rTable: Dict representing donors.
    :return: working on the return to presentation portion of the script.
    """

    print("|{:^17}|""{:^18}""|{:^21}|""{:^25}|".format(rHeading[0],rHeading[1],rHeading[2],rHeading[3]))
    print("{:_>85}".format("_"))
    for k, v in rTable.items():
        print("{:<18}""${:>18,.2f}""{:^22}""${:>25,.2f}".format(k, sum(v), len(v), (sum(v) / len(v))))
    print("\n\n")
    main(mainPrompt, dictMainPrompt)

# End of Create_A_Report function.

def Send_Bulk_ThankYou(lDonors, placeholder):
    """generates a thank you letter for all donors in listOfDonors and writes each letter to disk as a text file.
    :param lDonors: pass in a dict of donors.
    :return: returns nothing, creates txt files.
    """
    for k, v in lDonors.items():
        fName = str('C:\\Python210\\' + k+".txt")
        with open(fName, 'w') as f:
            f.write(" Dear {}, \n Thank you for your donation of ""${:,.2f}; it is very appreciated!"
                    "\n\n The team!".format(k, sum(v)))
    main(mainPrompt, dictMainPrompt)

# End of ThankYouLetter function.

def exit_program():
    print("Thank you for using this program, bye!")
    sys.exit()  # exit the interactive script

# End of exit program function.


#-- Presentation (Input/Output) --#
# get user input

dictThankYouPrompt = {1: UpdateListOfDonors,
                      2: Create_A_Report,
                      3: main}


dictMainPrompt = {1: send_a_thankyou,
                  2: Create_A_Report,
                  3: Send_Bulk_ThankYou,
                  4: exit_program}

margdict = {1: [thankYouPrompt, dictThankYouPrompt],
            2: [donorTableHeading, listOfDonors],
            3: [listOfDonors, None]}
tydict = {1: [listOfDonors, None],
          2: [donorTableHeading, listOfDonors],
          3: [mainPrompt, dictMainPrompt]}


# send program output


if __name__ == "__main__":
    # guards against Justin Jameson Mailroom code running automatically if this module is imported
    main(mainPrompt, dictMainPrompt)
