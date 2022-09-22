def not_blank(question):
    error = "This can't be left blank"

    valid = False
    while not valid:

        response = input(question)

        if response != "":
            return response
        else:
            print(error)

    name = input(print("Name: "))

