profit = 0

name = " "
while name != "xxx":

    # name goes here, or the exit code if you want to stop the program anytime
    name = input("Name: ")

    # just use this exit code when you are done collecting names and their owed money
    if name == "xxx":
        break

    # put your age here
    age = int(input("Age: "))

    # certain age groups get a discount. depending on your age you
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    # this is the equation to calculate profit
    profit_made = ticket_price - 5
    profit += profit_made

    # receipt of name + price to pay
    print("{}: ${:.2f}".format(name, ticket_price))
    # print profits
    print("Profits: ${:.2f}".format(profit))
