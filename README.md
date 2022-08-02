## creating a gitignore file in pyCharm
- Right click anywhere in the project window 
- then select new file
- name the file `.gitignore`

# Python topics

### Operators
Operators are special symbols in Python that carry out arithmetic or logical computation.

`+ - * /`
- `+` adds two operands (var) together
- `-` subtract
- `*` multiply
- `/` divide

### Comparison Operators
Comparison operators are used to compare two values:

- `>` greater than
- `<` less than
- `==`equal
- `!=`does not equal to
- `>=`greater than or equal to
- `<=`less than or equal to

Comparison Operators Example:
````
a = 4
b = 2

print(a > b) #True - This line of code returns True because 4 is greater than 2
print(b < a) #False - This line of code returns False because 4 is not less than 2
print(a == b) #False - This line of code returns False because 4 does not equal to 2
print(a != b) #True - This line of code returns true because 4 does not equal to 2
````

### Built in methods

Python has several functions that are readily available for use and perform a task.

Note: python lists are 0-indexed. So the first element is 0, second is 1, so on

Here are a few examples:

`len()` Returns the length of an object
`upper()` Returns string in caps 
`isdigit()` Returns True if all characters are digits, otherwise False

````
greeting = "Hello World"

print(len(greeting)) output: 11
print(greeting.upper()) output: HELLO WORLD
print(greeting.isdigit()) output: False
````

### Strings Concatenation
String concatenation is the process of merging two or more string together.

The + operator adds a string to another string.

Note: to add space insert double quotation marks with a space between them (" ")
````
Example:
first_name = "James"
last_name = "Bond"
print(first_name, " " + last_name)
output:
James Bond
````

### Casting
Type Casting is the process in which a literal of one type is converted to another.

Casting in python is done using constructor functions:

`int()` - takes a string or float as an argument converts it to an integer.

`float()` - takes an integer or string as an argument and converts it to a float.

`str()` - takes an integer or float as an argument and converts it to a string.
````
Example:
a = int(5)
print (a) #5

b = float("12")
print(b) #12.0

c = str(6)
print(c) # '6'
````

# Data Collection
Collections in Python are container data types such as:
- Lists 
- Tuples
- Dictionary

Lists are declared in square brackets, it is mutable, stores duplicate values and elements can be accessed using indexes.

#### List Example:
````
shopping_list =["bat", "milk", "bread"]
print(shopping_list)

output:
['bat', 'milk', 'bread']
````
Note: In this code we have created a list called shopping and have added three items, the shopping list is then printed to the console and wil display content inside.

### Finding the type of shopping list
````
shopping_list =["bat", "milk", "bread"]

print(type(shopping_list))
print(type("bat"))
print(type("milk"))
print(type("bread"))

output:
<class 'list'>
<class 'str'>
<class 'str'>
<class 'str'>
````
Note: This code displays the type of the shopping list and the types of the items.

### Finding the length of shopping list
````
shopping_list =["bat", "milk", "bread"]
print(len(shopping_list))

output:
3
````
Note: This code returns the number of items in the shopping list.

### Adding to shopping list
````
shopping_list =["bat", "milk", "bread"]
shopping_list.append("oreos")
print(shopping_list)

output:
['bat', 'milk', 'bread', 'oreos']
````
Note: In this code we are adding additional items to the shopping list, here we have added oreos to the end of the shopping list.

### Removing an item from shopping list
````
shopping_list =["bat", "milk", "bread"]
shopping_list.remove("milk")  
print(shopping_list)

output:
['bat', 'bread']
````
Note: this line of code removes the specified item from the shopping list, in this case we remove "milk".

### Replacing an item from the list and replace bat with milk
````
shopping_list =["bat", "milk", "bread"]
shopping_list[0] = "milk"
print(shopping_list)

output:
['milk', 'milk', 'bread']
````
Note: In this code we replace bat with milk by directly assigning a new value to the first index. 

### Print 2 & 3 from the list
````
mixed_list = [1, 2, 3, "one", "two", "three"]
print(mixed_list[1:3])

output:
[2, 3]
````
Note: In this code we print specific elements from the list using their index.

## Dictionary 
A dictionary is an unordered and mutable Python container that stores mappings of unique keys to values.

### Dictionary syntax:
Dictionaries are written with curly brackets `({})`, including key-value pairs separated by commas `(,)`. A colon `(:)` separates each key from its value.

Dictionary Example:

````
devops_student_1 = {
    "name": "James",
    "stream": "tech",
    "completed_lessons": 3,
    "completed_lessons_names": ["lists", "operations", "built in methods"]
}

print(devops_student_1.keys()) 
output: dict_keys(['key', 'name', 'stream', 'completed_lessons', 'completed_lessons_names'])
print(devops_student_1.values)
output: <built-in method values of dict object at 0x1092a4240>
print(type(devops_student_1))
output: <class 'dict'>
print(devops_student_1["name"])
output: James
````

### Deleting an item from dict and delete operations
The `pop()` method removes the item with the specified key name:
````
devops_student_1.pop("name")
print(devops_student_1)

output:
{'key': 'value', 'stream': 'tech', 'completed_lessons': 3, 'completed_lessons_names': ['lists', 'operations', 'built in methods']}
````

The `del` keyword can also delete the dictionary completely:
````
del devops_student_1
print(devops_student_1) #this will cause an error because "thisdict" no longer exists.

output:
ERROR
````
Change 'completed lesson' from 3 to 2
````
devops_student_1["completed_lessons"] = 2
print(devops_student_1)

output:
{'key': 'value', 'name': 'James', 'stream': 'tech', 'completed_lessons': 2, 'completed_lessons_names': ['lists', 'operations', 'built in methods']}
````

### Control Flow