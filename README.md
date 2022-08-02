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

### Finding the length of shopping list
````
shopping_list =["bat", "milk", "bread"]
print(len(shopping_list))

output:
3
````

### Adding to shopping list
````
shopping_list =["bat", "milk", "bread"]
shopping_list.append("oreos") # this line of code adds oreos to the end of the shopping list
print(shopping_list)

output:
['bat', 'milk', 'bread', 'oreos']
````

### Removing an item from shopping list
````
shopping_list =["bat", "milk", "bread"]
shopping_list.remove("milk") # this line of code removes the specified item from the shopping list
print(shopping_list)

output:
['bat', 'bread']
````

### Replacing an item from the list and replace bat with milk
````
mixed_list = [1, 2, 3, "one", "two", "three"]
print(mixed_list)

output:
[1, 2, 3, 'one', 'two', 'three']
````

### Print 2 & 3 from the list
````
mixed_list = [1, 2, 3, "one", "two", "three"]
print(mixed_list[1]) # outcome would be 2
print(mixed_list[2]) # outcome would be 3
print(mixed_list[1:3])

output:
2
3
[2, 3]
````