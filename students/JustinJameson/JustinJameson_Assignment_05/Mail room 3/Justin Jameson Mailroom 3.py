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
# Justin Jameson 12 Feb 2019
# 1. Added dict Switch functionality.
# 2. Added Try Except Blocks
# 3. General cleanup and adding comments as needed.
# 4. trying to reformat variables and function names to pep standard (lowercase).
# **************************

import sys  # imports go at the top of the file

# -- Data -- #
# declare variables and constants
# heading for the table
donorTableHeading = ['First/Last Name', 'Donation Totals', 'Number of donations', 'Average donation amount']
# Include Donor Name, total donated, number of donations, and average donation amount as values in each row.
listOfDonors = {"Dana Spam": [39, 700500, 10], "Jay Byrd": [10, 343553235, 90], "Jo Jo": [6, 2353],
                "Kilee Boss": [2352315124], "Katee Pie": [3, ], "Ethon George": [25, 23423443, 52352]}

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
    """
    Function receives main prompt information as an argument then processes through a dict Switch to allow the user to
    continually make choices for the program.
    :param mprompt: Argument fed into the function to give the main prompt options.
    :param mdict: Argument fed into the function to give the main dictionary for manipulation.
    :return:none
    """
    while True:
        try:
            response = int(input(mprompt))  # continuously collect user selection
            v0 = margdict.get(response)
        except ValueError:
            print("You must input an integer.")
        try:
            mdict.get(response)(v0[0], v0[1])
        except UnboundLocalError:
            print("You entered a letter, which in turn made a variable get called before it had benn assigned.")

# End of main function.

def send_a_thankyou(typrompt, tdict):
    """
    Function receives thank you letter prompt information as an argument then processes through a dict Switch to allow
    the user to continually make choices for the program.
    :param typrompt: Argument fed into the function to give the thank you promt options.
    :param tdict: Argument fed into the function to feed the dict Switch arguments.
    :return: none
    """
    while True:

        try:
            response = int(input(typrompt))  # continuously collect user selection
            v0 = tydict.get(response)
        except ValueError:
            print("You must input an integer.")
        try:
            tdict.get(response)(v0[0], v0[1])
        except UnboundLocalError:
            print("You entered a letter, which in turn made a variable get called before it had benn assigned.")

# End of Send a Thank you function.

# perform tasks #


def update_list_of_donors(ldonors, placeholder):
    """
    Function is called from send_a_thankyou function to update the list of donors.
    :param ldonors: a Dictionary list of donors for updating.
    :param placeholder: used for second list for the arguments dict.
    :return:
    """
    # prompt user for a Full Name.
    donorFirstName = input("Enter the donors First name or enter to exit: ")
    donorLastName = input("Enter the donors Last name: ")
    # prompt for a donation amount and add it to the donation history of the selected user.
    try:
        donorDonationAmount = int(input("Enter the Donation amount: "))
    except ValueError:
        print("Enter numbers only please.")
    donorFullName = donorFirstName.capitalize() + " " + donorLastName.capitalize()
    # check to see if the name exists
    if donorFullName in ldonors:
        for v in ldonors.values():
            try:
                v.append(donorDonationAmount)
            except UnboundLocalError:
                print("You entered a letter, which in turn made a variable get called before it had benn assigned.")

    # If the name is not in the dict, add that name and use it.
    else:
        try:
            ldonors[donorFullName] = [donorDonationAmount]
        except UnboundLocalError:
            print("You entered a letter, which in turn made a variable get called before it had benn assigned.")

    thank_you_letter(donorFirstName, donorDonationAmount)
    main(mainPrompt, dictMainPrompt)


def thank_you_letter(fname, damount):
    """
    This function prints out a thank you letter to the screen for copy and paste to the donor.
    :param fname: Argument from dict ldonors for formating.
    :param damount: amount from ldonors for letter.
    :return: should be a formatted string to the output, but has not been completed yet.
    """
    print(f"Thank you {fname}, your donation of $ {damount} is appreciated!")

# End of thank_you_letter function.

def create_a_report(rheading, rtable):
    """
    Create a Report
    1) print a list of your donors, sorted by total historical donation amount.
    2) Include Donor Name, total donated, number of donations, and average donation amount as values in each row.
    3) do not print out all of each donor’s donations, just the summary info.
    4) Using string formatting, format the output rows as nicely as possible. The end result should be
    tabular (values in each column should align with those above and below).
    5) After printing this report, return to the original prompt.

    :param rheading: Sequence passed in to represent the header information of the table, currently a list.
    :param rtable: Dict representing donors.
    :return: working on the return to presentation portion of the script.
    """

    print("|{:^17}|""{:^18}""|{:^21}|""{:^25}|".format(rheading[0], rheading[1], rheading[2], rheading[3]))
    print("{:_>85}".format("_"))
    for k, v in rtable.items():
        print("{:<18}""${:>18,.2f}""{:^22}""${:>25,.2f}".format(k, sum(v), len(v), (sum(v) / len(v))))
    print("\n\n")
    main(mainPrompt, dictMainPrompt)

# End of create_a_report function.

def send_bulk_thankyou(ldonors, placeholder):
    """
    generates a thank you letter for all donors in listOfDonors and writes each letter to disk as a text file.
    :param ldonors: pass in a dict of donors.
    :return: returns nothing, creates txt files.
    """
    for k, v in ldonors.items():
        fName = str('C:\\Python210\\' + k+".txt")
        with open(fName, 'w') as f:
            f.write(" Dear {}, \n Thank you for your donation of ""${:,.2f}; it is very appreciated!"
                    "\n\n The team!".format(k, sum(v)))
    main(mainPrompt, dictMainPrompt)

# End of thank_you_letter function.

def exit_program(a,b):
    """
    This function exits the program.
    :return: none
    """
    print("Thank you for using this program, bye!")
    sys.exit()  # exit the interactive script

# End of exit program function.


# -- Presentation (Input/Output) --#
# get user input

dictThankYouPrompt = {1: update_list_of_donors,
                      2: create_a_report,
                      3: main}


dictMainPrompt = {1: send_a_thankyou,
                  2: create_a_report,
                  3: send_bulk_thankyou,
                  4: exit_program}

margdict = {1: [thankYouPrompt, dictThankYouPrompt],
            2: [donorTableHeading, listOfDonors],
            3: [listOfDonors, None],
            4: [None, None]}
tydict = {1: [listOfDonors, None],
          2: [donorTableHeading, listOfDonors],
          3: [mainPrompt, dictMainPrompt]}


# send program output


if __name__ == "__main__":
    # guards against Justin Jameson Mailroom code running automatically if this module is imported
    main(mainPrompt, dictMainPrompt)
