# this code defines a formatted function for later I think???
# it should be useful for the main code
def yes_no(question):
    # just a little something to get the user on the right track if needed
    error = "Please choose an answer: yes/no"

    valid = False
    while not valid:

        # answer will be converted to lowercase for easier utility
        response = input(question).lower()

        # This sequence the system will identify the user's response,
        # if it is not the expected response it will respond with the error to redirect the user
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(error)


for item in range(0, 6):
    # yes_no starts the def function!
    want_snacks = yes_no("Would you like to purchase snacks? ")
    print("You answered:", want_snacks)
    print()
