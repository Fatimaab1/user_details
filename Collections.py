# Data Collection
## Lists, Tuples, Dictionaries

#### Lists
# What are lists?
# correct syntax []
# lists are mutable
# indexing; same concept applies

shopping_list =["bat", "milk", "bread"]
#print(shopping_list)

# find out the type of shopping list
#print(type(shopping_list))
#print(type("bat"))
#print(type("milk"))
#print(type("bread"))

# find out the len of shopping list
#print(len(shopping_list))

# how to add to shopping list
#shopping_list.append("oreos") # this line of code adds oreos to the end of the shopping list
#print(shopping_list)

# how to remove an item from shopping list
#shopping_list.remove("milk") # this line of code removes the specified item from the shopping list
#print(shopping_list)

# find out how to replace an item from the list and replace bat with milk
#shopping_list =["bat", "milk", "bread"]
#shopping_list[0] = "milk"
#print(shopping_list)

#mixed_list = [1, 2, 3, "one", "two", "three"]
#print(mixed_list)

# print 2 & 3 from the above list
#print(mixed_list[1]) # outcome would be 2
#print(mixed_list[2]) # outcome would be 3
#print(mixed_list[1:3])

# Tuples
# why do we need tuples
# lists[] are mutable VS Tuples() are immutable
# Syntax for tuple ()
# What are the use cases?

#essential = ("city", "DOB", "place of birth")
            #  0       1           2
#print(essential)
#print(type(essential))
#print(essential[1])
#essential[0] = "town" # *ERROR* Tuple is immutable, you cannot try to reassign item values
#print(essential)

#What is a Dict {}
# Dictionary can have all types of collections
# Dict work as "KEY": "VALUE" pair

devops_student_1 = {
    "key" : "value",
    "name": "James",
    "stream": "tech",
    "completed_lessons": 3,
    "completed_lessons_names": ["lists", "operations", "built in methods"]
}


#print(devops_student_1)
#print(devops_student_1.keys())
#print(devops_student_1.values)
#print(type(devops_student_1))
#print(devops_student_1["name"])

# find out how to delete in item from dict and delete operations
# The pop() method removes the item with the specified key name:

#devops_student_1.pop("name")
#print(devops_student_1)

# The del keyword can also delete the dictionary completely:

#del devops_student_1
#print(devops_student_1) #this will cause an error because "thisdict" no longer exists.

# find out how to change completed lesson from 3 to 2
#devops_student_1["completed_lessons"] = 2
#print(devops_student_1)

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




