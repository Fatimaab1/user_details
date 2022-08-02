firstName = input('What is your first name?')
print(firstName)

lastName = input('What is your last name?')
print(lastName)

age = int(input('How old are you?'))
print(age)

address = input('What is your address?')
print(address)

houseNumber = input("enter door number")
if houseNumber.isdigit() == True:
    print(houseNumber)
else:
    print("house number entered is invalid")


print("Hi", firstName, lastName + " You're", str(age), "You live in", address, "And your door number is",
      houseNumber)