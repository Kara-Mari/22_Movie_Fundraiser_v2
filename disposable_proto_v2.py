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


def string_check(choice, options):
    for var_list in options:

        if choice in var_list:

            chosen = var_list[0].title()
            is_valid = "yes"
            break

        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


valid_snacks = [
    ["popcorn", "corn", "a"],
    ["m&ms", "m", "mms", "b"],
    ["pita chips", "chips", "pc", "c"],
    ["water", "w", "d"]
]
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("do you want to order snacks?").lower()
    check_snack = string_check(want_snack, yes_no)

for item in range(0, 6):
    desired_snack = input("snack: ").lower()

    snack_choice = string_check(desired_snack, valid_snacks)
    print("snack choice: ", snack_choice)
