# following code will have inputs for name and age, error codes for both, others are being worked on
# checks that tickets name is not blank
def not_blank(question):
    error = "This can't be left blank"

    valid = False
    while not valid:

        response = input(question)

        if response != "":
            return response
        else:
            print(error)


#   checks for an integer more than 0
def int_check(question):
    error = "Please enter a whole number that is more than 0"

    valid = False
    while not valid:

        # ask user for number and check if it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


#  * * * Main routine * * *

#   set up dictionaries / lists needed to hold data

#   Ask user if they have used the program before

#   Loop to get tickets details
#   Start of loop

#   initialise loop so that it runs at least once

# this sequence will ask the user's name and age 

name = " "
count = 0
tickets = 5

while name != "xxx" and count < tickets:

    # tells user how many seats are left
    if count < 4:
        print("There are {} seats "
              "left".format(tickets - count))

    # warning
    else:
        print("Just one left!!!")

    # get name
    name = not_blank("Name: ")

    # end loop
    if name == "xxx":
        break

    # get age between 12 and 130
    age = int_check("Age: ")

    # check if age is valid
    if age < 12:
        print("Sorry, you aren't allowed to see this content")
        continue
    elif age > 130:
        print("This doesn't seem right...")
        continue

    count += 1

    # end of tickets loop
