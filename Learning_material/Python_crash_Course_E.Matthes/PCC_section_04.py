
# Section 4, Lists and loops *for loop*
# insert/type mode [INS]

magicians = ['alice', 'david', 'carolina']
for magician in magicians:  # we associate ma name with a *variable* defining it
    print(f'{magician.title()} that was a great trick!')
    print(f'I cant wait to see your next trick, {magician.title()}')
# summarizes a block. Prints only once, cause outside loop
print('Thank you, everyone. That was a great show!')
# *for magician in magicians* tells Python to retrieve the first value from the list magicians,
# and associate it with the variable magician
# examples
# "for cat in cats:"
# 'for dog in dogs:'
# 'for item in item_list'
# ====================End===========================
# indentation errors
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(f'{magician.title()} that was a great trick!')
# should be indented, so gives an error ->
# IndentationError: expected an indented block after 'for' statement on line 1
# another example
magicians_2 = ['alice', 'david', 'carolina']
for magician_2 in magicians_2:
    print(f'{magician_2.title()} that was a great trick!')
# should be indented. logical error.
print(f'I cant wait to see your next trick, {magician_2.title()}')
# ====================End===========================
# unexpected indent example
# message = 'Hello Python world!'
#   print(message)
# unnecessary indentation prints an error: "IndentationError: unexpected indent"
# forgetting collon example:
magicians = ['alice', 'david', 'carolina']
for magician in magicians  # prints SyntaxError: expected ':'
# ====================End===========================
# p56 exercises
pizzas = ['margerita', 'napolitan', 'peperoni']
for pizza in pizzas:
    print(f'I like {pizza} pizza')
print('I really lobe pizza!')
# 4-2
mammals = ['bear', 'monkey', 'wolf']
for mammal in mammals:
    print(f"A {mammal.title()} is a mammal")
print('Any of these animals would make a great pet!')
# ====================End===========================
# numeric lists *range()* used to generate a series of numbers when range is defined
for value in range(1, 5):  # last value is never printed!
    print(value)

for value in range(1, 6):  # results in 1-5
    print(value)
# you can also range only one argument and it will return numbers 0 - arguments. #example
for value in range(6):
    print(value)  # 0-5
# ====================End===========================
# using range() to make a list of numbers by wrapping in list
numbers = list(range(1, 6))
print(numbers)
for number in numbers:
    print(f'{number} is an integer')
# 3rd value in range() slists every n-th number
even_numers = list(range(2, 11, 2))  # list every 2nd
print(even_numers)
even_numbers = list(range(2, 11, 3))  # list every 3rd
print(even_numbers)
# square numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    # very important, appends the original list that was empty
    squares.append(square)
print(squares)

# example nr 2., same logic but uses squares.append()
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
# ====================End===========================
# simple statistics with list of numbers
# finding min, max and sum
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)
# another example
digits_2 = []
for digit in range(1, 2000000, 4030):
    digits_2.append(digit+500)
    print(digits_2)
print(f"total number of items in the list is: {len(digits_2)}")
# List comprehension example, same output as squares
squares = [value**2 for value in range(1, 11)]  # ! good example
print(squares)
squares = [value**2+2 for value in range(1, 11)]  # ! good example
print(squares)
# ====================End===========================
# p60 exercises
numbers = list(range(1, 21))
print(numbers)
numbers = list(range(1, 1000001))
print(numbers)
min(numbers)
max(numbers)
sum(numbers)
# odd numbers list
numbers = list(range(1, 21, 2))
for number in numbers:
    print(number)
numbers_2 = list(range(3, 31, 3))
for number in numbers_2:
    print(number)
# 4-8 List comprehensions
cubes = [number**3 for number in range(1, 11)]
print(cubes)
# ====================End===========================
# working with part of a list
# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # slicing
print(players[1:4])
# starts at the beginning of the list when start index not defined
print(players[:4])
# same of other way around
print(players[3:])
print(players[-2:])  # with minus starts from the end of the list

check = print(players[-2:] == players[3:5])  # True
# can also include third slice to skip
list = []
for item in range(1, 21):
    list.append(item)
print(list)
print(
    f'This is the edited list with every second item in 5:15 range exluded: {list[5:15:2]}')
print(f'And this is without exluction 5:15 range: {list[5:15]}')
# ====================End===========================
# Looping through a slice
players_2 = ['charles', 'martina', 'michael', 'florence', 'eli']
print('here are the first 3 players on my list:')
for player in players_2[:3]:  # slice loop
    print(player.title())

# Copying a list [:] copies identical list
my_foods = ['coke', 'pizza', 'falafel', 'carrot cake']
# creates identical list from sate start : end ! VERY important syntax
friend_foods = my_foods[:]

print(f'My favorite foods are {my_foods}')
print(f'My friends favorite foods are: {friend_foods}')
# append to show that each list tracks items independantly
my_foods.append('cannoli')
friend_foods.append('ice cream')

print(f'My favorite foods are {my_foods}')
print(f'My friends favorite foods are: {friend_foods}')
print(f'Are both lists identical: {my_foods == friend_foods}')  # boolean check


# ------------------------------------------------------------
# IMPORTANT: The difference between assignment and copying lists
#
# new_list = old_list
#   → This does NOT create a new list.
#   → Both variables point to the SAME list in memory.
#   → Changing one will also change the other.
#
# new_list = old_list[:]
#   → This DOES create a NEW list (a shallow copy).
#   → Both lists start with the same contents.
#   → Changing one will NOT affect the other.
# ------------------------------------------------------------

# Example:
old_list = ['coke', 'pizza', 'falafel']
# proper copy there is also inbuilt function new_list = old_list.copy()
new_list = old_list[:]

old_list.append('carrot cake')
new_list.append('ice cream')

print("Old list:", old_list)
print("New list:", new_list)

# Check equality vs identity
print("Same contents?", old_list == new_list)   # False (different items)
print("Same object?", old_list is new_list)     # False (different lists)
# These two are identical "old_list[:]   ==   old_list.copy()" !!!
# example of linking the same list:
cars = ['Toyota', 'BMW', 'Audi', 'Honda', 'Ford']
same_cars = cars   # NOT a copy — just another name for the same list

# Append items to each variable
same_cars.append('Tesla')
cars.append('Mazda')

print("cars:", cars)
print("same_cars:", same_cars)

# Boolean check: are the contents the same?
print("Same contents?", cars == same_cars)   # True

# Identity check: are they the same object in memory?
print("Same object?", cars is same_cars)     # True
# ====================End===========================
# 4-10 exercises
cars = ['Toyota', 'BMW', 'Audi', 'Honda', 'Ford']
print(f'first three cars in the list are: {cars[:3]}')
print(f'three cars from the middle of the list are: {cars[1:4]}')
print(f'last three cars from the list are: {cars[-3:]}')

# pizzas exercise
pizzas = ['margerita', 'napolitan', 'peperoni']
friend_pizzas = pizzas[:]  # or firnd_pizzas = pizzas.copy()
pizzas.append('salami')
friend_pizzas.append('tuna')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('My friends favorite pizzas are:')
for pizza_2 in friend_pizzas:
    print(pizza_2)
#
alphabet = ['a', 'b', 'c']
alphabet_new = alphabet.copy()
alphabet_new.append('d')
print(f'old list: {alphabet} and new list is {alphabet_new}')
# ====================End===========================
# Tuples
# python refers to values that cannot change as `immutable` and and immutable list is called a `tuplse`
dimensions = (200, 50)  # define tuple dimensions !!!
print(dimensions[0],
      dimensions[1])

# example when trying to change one of the dimensions
dimensions_2 = dimensions[:]
print(dimensions_2)
dimensions_2[0] = 250  # changing dimension in tuple
print(dimensions_2[0],  # we get an error `TypeError: 'tuple' object does not support item assignment`
      dimensions_2[1])
# this is beneficial behavior when some1 wants to try and change a tuple
# tuples are typically defined by parentheses, this makes them more readable as per PEP8.
# if we want to define a tuple with one element we can include a railing comma
my_t = (3, )
# can also loop through all tuple items using for loop
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# we cant edit dimensions individually but we cant ovveride them
dimensions = (200, 50)
print(f'original dimensions: {dimensions[0],
      dimensions[1]}')
dimensions = (400, 100)  # override
print(f'modified dimensions: {dimensions[0],
      dimensions[1]}')

# p67 exercises
menu = ('water', 'coke', 'ice-coffee', 'tea', 'beer')
new_menu = menu[:]
for drink in menu:
    print(drink)
# get an error `TypeError: 'tuple' object does not support item assignment`
menu[2] = ('juice')
# change menu
menu = ('sake', 'coke', 'juice', 'tea', 'beer')
for drink in menu:
    print(drink)
print(f'are the menus same?: {menu == new_menu}')
print(f'because old menu is: {new_menu} and new menu is {menu}')
# additional comments about PEP8 and style
# historically guidelines suggested to fit only 79 characters  per line length
# PEP8 recommends 72^. also using blank lines is encouraged
# ====================End===========================
