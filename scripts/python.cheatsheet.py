# Create an empty list using square brackets.
numbers = []
print(numbers) # Output: []

# Create an empty list using list().
numbers = list()
print(numbers) # Output: []

# Create a list of numbers.
numbers = [1, 2, 3]
print(numbers) # Output: [1, 2, 3]

# Create a list of numbers in a range.
numbers = list(range(1, 4))
print(numbers) # Output: [1, 2, 3]

# Create a list of tuples.
tuples_list = [(1, 2), (2, 4), (3, 6)]
print(tuples_list) # Output: [(1, 2), (2, 4), (3, 6)]

# Create a list of lists.
list_of_lists = [[1, 2], [2, 4], [3, 6]]
print(list_of_lists) # Output: [[1, 2], [2, 4], [3, 6]]

# Create a list with items of different data types.
random_list = [1, "hey", [1, 2]]
print(random_list) # Output: [1, "hey", [1, 2]]

# Get length of list by using len() method.
numbers = [5, 8, 8]
print(len(numbers)) # Output: 3

# Access elements of a list by indexing.
str_list = ["hey", "there!", "how", "are", "you?"]
print(str_list[0]) # Output: "hey"
print(str_list[len(str_list) - 1]) # Output: "you?"
print(str_list[-1]) # Output: "you?"

# Slicing a list.
str_list = ["hey", "there!", "how", "are", "you?"]
print(str_list[2:]) # Output: ["how", "are", "you?"]
print(str_list[:2]) # Output: ["hey", "there!"]
print(str_list[-3:]) # Output: ["how", "are", "you?"]
print(str_list[:-3]) # Output: ["hey", "there!"]
print(str_list[1:4]) # Output: ["there!", "how", "are"]
# Get a copy of list by slicing.
print(str_list[:]) # Output: ["hey", "there!", "how", "are", "you?"]

# Append to a list.
numbers = [1, 2]
print(numbers) # Output: [1, 2]
numbers.append(3)
print(numbers) # Output: [1, 2, 3]

# Concatenate lists.
numbers = [1, 2]
strings = ["Hey", "there"]
print(numbers + strings) # Output: [1, 2, "Hey", "there"]

# Mutate a list, that is, change its contents.
numbers = [1, 2, 3]
numbers[0] = 100
print(numbers) # Output: [100, 2, 3]
numbers[0:2] = [300, 400]
print(numbers) # Output: [300, 400, 3]
numbers[1:3] = []
print(numbers) # Output: [300]
numbers[:] = []
print(numbers) # Output: []

# Insert item to a list.
greeting = ["how", "you?"]
greeting.insert(1, "are")
print(greeting) # Output: ["how", "are", "you?"]

a = 'corge', 'back'
s = 'haha'
try:
    print(a.index('corge'))
except ValueError:
    print(s, 'not found in list.')
