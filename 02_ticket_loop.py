name = " "
count = 0
tickets = 5

while name != "xxx" and count < tickets:

    # tells user how many seats are left
    if count < 4:
        print("There are {} seats "
              "left".format(tickets - count))
    # warning last call
    else:
        print("Just one left!!!")

        # get users details

        # get name

    name = input("Name: ")
    count += 1
    print()

    if count == tickets:
        print("All the tickets have been sold")
    else:
        print("You have sold {} tickets.    \n"
              "There are {} places still available"
              .format(count, tickets - count))
