# Section 3, Lists and storing information
# in python lists are indicated by [] and (,) used as separator
# pep8 formatting always sorts Import libraries at the top

import random
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# Accessing elements in a list, by index
print(bicycles[0])  # index position starts at 0, not 1
print(bicycles[2])
print(bicycles[0].title(), bicycles[2].title())  # For multiple indexes
print(bicycles[0].title() + "\n" + bicycles[2].title())  # splits with \n
# -1 returns last item, also works for items items from the back -2, -3 etc.
print(bicycles[-1].title())
print(bicycles[-2].title())
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)
# ==================================================
# To use random here, make sure you have:
# import random
index = random.randint(0, len(bicycles) - 1)
message = f"My first bicycle was a {bicycles[index].title()}"
print(message)
# ====================End===========================
# Names exercise
names = ['mark', 'tom', 'Peter', 'Luke']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print(f"Dear " + names[0].title() + ",")
print(f"Dear " + names[1].title() + ",")
print(f"Dear " + names[2].title() + ",")
print(f"Dear " + names[3].title() + ",")
# runs random name from the f list, structure {list[random-function or index]}
index2 = random.randint(0, len(names) - 1)
print(f"Dear {names[index2].title()},")
print(f"Dear {names[index2].title()}, \nI hope this E-mail finds you well...")
# ====================End===========================
# changing elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
for bike in motorcycles:
    print(bike.title())

# adding elements to a list using append
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')  # adds to the end of the list
print(motorcycles)

# appending to an empty list
motorcycles_1 = []
motorcycles_1.append('ducati')
motorcycles_1.append('honda')
motorcycles_1.append('suzuki')
print(motorcycles_1)
for bike2 in motorcycles_1:
    print(bike2.title())
# adding to the list example
motorcycles_1.insert(-2, 'yamaha')  # adds to a specific position in the list
print(motorcycles_1)

# removing from the list
motorcycles_3 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_3)
del motorcycles_3[1]
print(motorcycles_3)
# ====================End===========================
# removing items using pop() method
# allows removing last item from the list and re-using it later.
motorcycles_4 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_4)
popped_motorcycle = motorcycles_4.pop()  # takes out last variable
print(motorcycles_4)  # displays list with lat variable edited-out
print(popped_motorcycle)  # prints out only the last variable

motorcycles_5 = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles_5.pop()
print(f'Last motorcycle I owned was a {last_owned.title()}')

# example from popping from any index position
motorcycles_5 = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles_5.pop(-2)
print(f'Last motorcycle I owned was a {last_owned.title()}')

# removing item by value, when we dont know the position
motorcycles_6 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_6)
motorcycles_6.remove('suzuki')  # removes this value
print(motorcycles_6)

# removing with a reasoning statment
motorcycles_7 = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles_7.remove(too_expensive)

print(f"\nA {too_expensive.title()} is too expensive for me. The rest I can afford:")

for bike3 in motorcycles_7:  # always prints as new sentences, entries (loops)
    print(bike3.title())
# important! remove() only deletes the first instance of a value, to remove re-occuring ones loop has to be used.
# ====================End===========================
# exercise p.41
guests = ['lincoln', 'cobain', 'williams']
print(guests)
for name in guests:
    print(f'Dear {name.title()}, You are invited to the a dinner party')
# part 2
print(
    f'unfortunately, {guests[1].title()} cant make it so a new person will be invited, "Malcolm"')
del guests[1]
guests.insert(1, 'malcolm')
print(guests)

for name_2 in guests:
    # replaced [1] guest with new variable
    print(f'Dear {name_2.title()}, You are invited to the a dinner party')

# 3-6 exercise
print('additional guests will be invited')
guests.append('Tom')
guests.append('Mark')
guests.append('Shaq')
list_appended = guests
print(list_appended)
for name_3 in list_appended:
    print(f'Dear {name_3.title()}, You are invited to the a dinner party')

# 3-7 exercise
print('Sadly can only invite two guests...')
list_minusone = list_appended.pop()
print(
    f'Im saddened to inform you that {list_minusone}, you are no longer invited..')
list_minustwo = list_appended.pop()
print(
    f'Im saddened to inform you that {list_minustwo}, you are no longer invited..')
list_minuthree = list_appended.pop()
print(
    f'Im saddened to inform you that {list_minuthree}, you are no longer invited..')
list_minusfour = list_appended.pop()
print(
    f'Im saddened to inform you that {list_minusfour}, you are no longer invited..')

print(f'Remaining guests are: {list_appended}')  # check remaining guests
for remaining in list_appended:
    print(f'Dear {remaining.title()}, you are still invited')

# print empty list
list_appended.clear()  # clears list completely
print(list_appended)
# ====================End===========================
# list Organizing
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # sorts list permanently, alphabetically
print(cars)
# can also sort in reverse-alphabet
cars.sort(reverse=True)  # reverse=true
print(cars)
# sorting list temporarily. we use sorted()
cars_2 = ['bmw', 'audi', 'toyota', 'subaru']
print(f'Here is the original list: {cars_2}')
# type in as {sorted(list)}
print(f'And here is the sorted list: {sorted(cars_2)}')
# list order did not change.
print(f'And here is the original list again: {cars_2}')
print(f'Reverse-sorted list: {sorted(cars_2, reverse=True)}')
print(f'And here is the original list again: {cars_2}')

# Printing a list in reverse order reverse(). Chronologically
cars_3 = ['bmw', 'audi', 'toyota', 'subaru']
original = cars_3.copy()
print(cars_3)
# Reverses the list chronologincally, not alphabetically like sort(reverse=true)!
cars_3.reverse()
print(cars_3)
print(cars_3 == original)  # compare, prints False
# this changes the list permanently but, we can reverse it again using .reverse() a second time
cars_3.reverse()
print(cars_3 == original)  # compare, prints True
# finding length of a list using function len()
len(cars_3)  # prints index numbers
# python starts counting items starting 1, using len()
print(f'The number of indexes in our Cars_3 list is: {len(cars_3)}')
# ====================End===========================
# p45. exercises
countries = ['iceland', 'states', 'hawaii', 'new zealand', 'peru']
print(countries)
# alphabetical
print(f'Printing in sorted" {sorted(countries)}')
print(f'List is still in its original form: " {countries}')
# alphabetical-reverse
print(f'Reverse-sorted list: {sorted(countries, reverse=True)}')
print(f'List is still in its original form (2nd check):  {countries}')
# List in reverse chronological order
countries.reverse()
print(f'Reverse-chronological list: {countries}')
countries.reverse()
print(f'List is again back in its original form (3nd check):  {countries}')
countries.sort()
print(f'sorted list:  {countries}')
countries.sort(reverse=True)
print(f'reverse sorted list:  {countries}')
# final exercise
motorcycles_7 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(f'Im inviting {len(motorcycles_7)} people')
# ====================End===========================
# abbout errors when working with lists.
motorcycles_4 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_4[3])
# example of error, "IndexError: list index out of range" only 3 items in list. ! starts as [0]
# very useful, as it always returns last item despite list length
print(motorcycles_4[-1])
motorcycles_empty = []
# the only time will return an error, cause empty list "IndexError: list index out of range"
print(motorcycles_empty[-1])
# this is an easy area to make a mistake in -- good recommendation -- to print out your list,
# as it may look different than intended
