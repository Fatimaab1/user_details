# Control Flow
# if , elif, else statement - conditional statements
# Sudo coding
#weather = "dry" # True or false

#if weather == "sunny":
   # print("Lets do a BBQ") # If true this line of code will be executed
#elif weather == "dry":
 #   print("getting there")
#else:
    #print("hope for the best") # this line of code will be executed if weather is not sunny


# if elif and else

# loops - for and while loops
# not to repeat yourself
# loops help us to ITERATE through data collections - DATA

# lets create a list to use for loop to iterate through it

#shopping_list = ["fruits", "milk", "cream", "bread"]
#print(shopping_list)
# print each item of the list as a list
# fruits
# milk
# cream
# bread
#print(shopping_list[0])
#print(shopping_list[1])
#print(shopping_list[2])
#print(shopping_list[3])

#shopping_list = ["fruits", "milk", "cream", "bread"]

#for item in shopping_list:
   # print(item)
    # does the list have brad
    # if bread is found in the list stop the program

    #if item == "milk":
    # break

# create a dictionary with 6 key value pairs
# NOTE: "key" : "value",

#colour_list = {
   # "colour1": "red",
   # "colour2": "blue",
    #"colour3": "pink",
    #"colour4": "yellow",
    #"colour5": "orange",
    #"colour6": "purple"
#}
# use for loop to iterate through it
#for item in colour_list:
   # print(item)

# print only keys
#print(colour_list.keys())

# print only value
#print(colour_list.values())

# print key with matching value
#for key, value in colour_list.items():
    #print(key,value)


# use case of multiple conditions
# create a list with int value 1-4
#data_list = [1, 2, 3, 4]
# iterate through the list using for loop
#for number in data_list:

# find 3 and print if found
  #  if number == 3:
     #   print("3")
# or else list number greater than 3 print gone too far
   # elif number > 3:
           # print("gone too far")
# otherwise print too soon
#else:
    #print("too soon")


# while loop
# while loop is mostly used as a monitor rather than handling

#numbers = 0
# iterate while number is less than 10
#while numbers < 10:

# print the number with message stating it's working
    #print(f'its working --> {numbers}')

# add +1 in each iteration
#numbers += 1

#age = input("please Enter your age")
# print a message stating your age is user input
#print(f" your age is {age}")

user_prompt = True

while user_prompt:
    age = input("Please enter your age ")
    if age.isdigit() and int(age) < 117:
        user_prompt = False #stop prompting the user (we received what we needed)
    else:
        print("please enter numbers only")
print(f"Your age is {age}")



# using the above use case also check if the user age is less than 117 years
# before you and the while loop
# in order to do that you may need to use casting -
# in other words may need to convert age to int
