from Disposable_Proto import age, name


def ticket_count(question):

    profit = 0

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
