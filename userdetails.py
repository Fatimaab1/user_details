def users_details():
    firstName = input('What is your first name?')
    print(firstName)

    lastName = input('What is your last name?')
    print(lastName)

    age = int(input('How old are you?'))
    print(age)

    address = input('What is your address?')
    print(address)

    houseNumber = input("enter door number")
    if houseNumber.isdigit():
        print(houseNumber)
    else:
        print("house number entered is invalid")


#users_details()
#def print_users_details(firstName, lastName, age, address, houseNumber):
    print("Hello", firstNameame + "!\n\nYou are", str(age), "years old \n\nAnd live in", address, "Your house number is", houseNumber)