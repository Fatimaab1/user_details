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

new_shopping_list = {
    "colour1": "red",
    "colour2": "blue",
    "colour3": "pink",
    "colour4": "yellow",
    "colour5": "orange",
    "colour6": "purple"
}
# use for loop to iterate through it
for item in new_shopping_list:
    print(item)

# print only keys
print(new_shopping_list.keys())

# print only value
print(new_shopping_list.values())

# print key with matching value
for key, value in new_shopping_list.items():
    print(key,value)


