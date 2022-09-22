
def not_blank(question, error):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error)


# Main routine:
name = not_blank("Name: ", "This can't be blank")
