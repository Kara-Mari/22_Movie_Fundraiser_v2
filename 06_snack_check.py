
valid_snacks = [
    ["popcorn", "corn", "a"],
    ["m&ms", "m", "mms", "b"],
    ["pita chips", "chips", "pc", "c"],
    ["water", "w", "d"]
]

snack_ok = " "
snack = " "

for item in range(0, 3):
    desired_snack = input("snack: ").lower()

    for var_list in valid_snacks:

        if desired_snack in var_list:
            snack = var_list[0].title()
            snack_ok = "yes"
            break
        else:
            snack_ok = "no"

    if snack_ok == "yes":
        print("snack choice: ", snack)
    else:
        print("invalid choice")
