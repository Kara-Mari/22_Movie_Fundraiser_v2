def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:
                if response == item[0]:
                    return item

        print("sorry, that was not a valid response")


for item in range(0, 6):
    want_snacks = string_checker("do you want "
                                 "snacks? ", ["yes", "no"])
    print("you have answered: ", want_snacks)
    print()
