# Dictionaries
# Store qualities and : values (key-value), can also be nested containing other dictionaries
# A simple dictionary describing a car
car = {
    "brand": "Toyota",
    "model": "Supra",
    "year": 1998
}
# Accessing values using keys
print(car["brand"])   # Output: Toyota
print(car["year"])    # Output: 1998
# -----

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# -----
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f'You just earned {new_points} points!')
# ----- Adding new key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0  # adds additional key and value
alien_0['y_position'] = 25  # adds additional key and value
print(alien_0)
# ----- Starting with an empty dictionary
alien_0 = {}  # define empty dictionary
alien_0['color'] = 'green'
alien_0['points'] = 10
print(alien_0)
# user input
alien_0 = {}  # define empty dictionary
# asks for user input to add values
alien_0['color'] = input('Enter color of the alien: ')
# asks for user input to add values
alien_0['points'] = int(input("Enter a number: "))
print(alien_0)
print(
    f'The properties of the alien are: \nColor: {alien_0['color']} \nPoints: {alien_0['points']}')
# -----
alien_0 = {'color': 'Green'}
print(f'The alien is {alien_0['color']}.')
alien_0['color'] = 'Yellow'  # overriding the value
print(f'The alien is now {alien_0['color']}.')
# ----- Speed example -----
# adjust medium to slow or any other values
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f'Original position: {alien_0['x_position']}')
# move the alien to the right
# determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f'New position: {alien_0['x_position']}')
# ====================End===========================
# removing key-values
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']  # deleted key or key-value pair
print(alien_0)
# ----- a dictionary of similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'terry': 'assembly',  # good practice to add last comma to to be ready to add
}
# depending on the editor, there are many ways to store dictionaries
# some may look slightly different
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")
# -----
favorite_languages = {}
favorite_languages['No.1'] = input('Enter your favorite language: ')
favorite_languages['No.2'] = input('Enter your favorite language: ')
favorite_languages['No.3'] = input('Enter your favorite language: ')
print(f'Favorite languages are: {favorite_languages}')
# ----- Using get() Access Values
# important! asking for a key in dictionary that doesnt exist, returns an error
# ex. KeyError: 'points'
alien_0 = {'color': 'green', 'speed': 'fast'}
print(alien_0['points'])

# We can use get() method to set a default value that will be returned
# if the requested key doesnt exist.
# the get() key requires a key as first argument. As second optional argument,
# we can pass the value to be returned if the key doesnt exist:
alien_0 = {'color': 'green', 'speed': 'fast', }
# if points exist we get a value,
point_value = alien_0.get('points', 'No points value assigned.')
# if not, we get the message
print(point_value)
# another examplem but Python returns none because no value defined
point_value = alien_0.get('points')  # will print 'none'
# if not, we get the message
print(point_value)
# ====================End===========================
# exercises 6-1
info = {
    'name': 'friend',
    'last name': 'best',
    'age': 31,
    'city': 'Kaunas'}
for key in info:
    print(key, info[key])
print('Info Dump Finished')
# -----
info = {
    'tom': 5,
    'andy': 7,
    'mark': 3,
    'joe': 19,
    'stever': 5,
}
for key in info:
    print(key, info[key])
# ----- 6-3
glossary = {'dictionary': 'list of keys&values',
            'key': 'title of a value',
            'value': 'value of the title',
            'slice': 'part of a list',
            'indent': 'indentation in the code',
            }
for word in glossary:
    print(f'The word {word} has a meaning: \n\t"{glossary[word]}"')
# gives values tored under the key
# {glossary[word]}
# ====================End===========================
# looping through a dictionary
user_0 = {'username': 'efermi',
          'first': 'enrico',
          'last': 'fermi',
          }
for key, value in user_0.items():
    print(f'\nKey: {key}')  # loops through dictionary for key
    print(f'\nValue: {value}')  # loops through dictionary for value
# -----
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'terry': 'assembly',
}
for name, language in favorite_languages.items():  # .items() gives pairs: Key-Value
    print(f"{name.title()}'s favorite language is {language.title()}.")
# ====================End===========================
# Looping through All the Keys in a Dictionary
# keys() is useful when we dont want to work with all of the values in the dictionary.
# Prints names of every1 who took the poll:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'terry': 'assembly',
}
for name in favorite_languages.keys():  # prints only Keys
    print(name.title())
# -----
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'terry': 'assembly',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f'Hi {name.title()}')
    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, I see you love {language}!')
# -----
# we can use keys() to also find if a particular person was polled.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'terry': 'assembly',
}
if 'erin' not in favorite_languages:
    print("Erin, please take our poll!")
# -----
# Looping through a dictionary's keys in a particular order.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'terry': 'assembly',
}
for name in sorted(favorite_languages.keys()):  # sorts the names alphabetically
    print(f'{name.title()}, thank you for taking the poll')
# -----
# looping through all the values in a dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'terry': 'assembly',
}
print('following languages have been mentioned')
for language in favorite_languages.values():  # when only need values
    print(language.title())
# -----
# checking for unique values only./ no repeats *ignores repeats)
favorite_languages = {
    'jen': 'python',  # repeat
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'terry': 'assembly',
    'david': 'python',  # repeat
}
print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())
# prints only rust, python, assembly C
# important note: unlike lists and dictionaries, sets do not retain items in any specific order.
# -----
languages = {'python', 'rust', 'python', 'c'}
print(languages)  # <-- doesnt print duplicates!
# ====================End===========================
# ----- 6-4 exercises
glossary_2 = {'dictionary': 'list of keys&values',
              'key': 'title of a value',
              'value': 'value of the title',
              'slice': 'part of a list',
              'indent': 'indentation in the code',
              'set': 'do not retain items in a specific order',
              'list': 'list of values using [] brackets'
              }

for word, definition in glossary_2.items():
    print(f'{word}, {definition}')
# ----- 6-5 exercises
rivers = {'egypt': 'nile',
          'brasil': 'amazon',
          'china': 'yellow river',
          'usa': 'missisippi',

          }
for country in rivers:
    print(f'The {rivers[country].title()} runs through {country.title()}')
for country in rivers:
    print(country.title())
for country in rivers:
    print(rivers[country].title())
# ----- 6-6 exercises
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'terry': 'assembly',
    'david': 'python',
}
new_names = ['terry', 'garry', 'david', 'israel']
for name in favorite_languages.keys():
    print(f'Dear {name.title()}, thank you for taking the poll')
for name in new_names:
    if name not in favorite_languages:  # yay!
        print(f'Dear {name.title()}, please take the languages poll')
# ====================End===========================
# Useful dictionary methods:
# .keys()   → returns all keys in the dictionary
# .values() → returns all values
# .items()  → returns key–value pairs (used for looping with: for key, value in dict.items())
# list(dict) → converts dictionary keys into a list
# dict.get(key, default) → safely access a key without errors if it doesn't exist
# --------------------------------------------------
# nestng storing multiple dictionaries in a list
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# -----
# [] → list (ordered, changeable)
# () → tuple (ordered, immutable)
# {} → dictionary (key–value pairs)
# -----
aliens = []
# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:6]:  # changes firt 6 alien properties if green, to yellow
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
for alien in aliens[:3]:
    if alien['color'] == 'yellow':  # changes first 3 yellow to red again
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'

# show first 5 aliens
for alien in aliens[:10]:
    print(alien)  # 3 red, 3 yellow and 4 green
print('...')
# show how many aliens have been created.
print(f'total number of aliens: {len(aliens)}')
# -----
# a list in a dictionary
# store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],  # this stores multiple values!
}
# summarize the order.
print(f'you ordered a {pizza['crust']}-crust pizza '
      'with the following toppings:')
for topping in pizza['toppings']:
    print(f'\t{topping}')
# -----
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python'],
    'terry': ['assembly', 'holy c'],
    'david': ['haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:  # checks if more than 1 language, then:
        print(f"\n{name.title()}'s favorite languages are: ")
        for language in languages:
            print(f'{language.title()}')
    else:  # if 1 language then:
        print(f"\n{name.title()}'s favorite language is: ")
        for language in languages:
            print(f'{language.title()}')
# shouldnt nest items too deep, always an easier way to solve. simplicity is key
# ====================End===========================
# ----- a dictionary in a dictionary
users = {  # example of double nesting
    'aeinsten': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'ecurie',
        'location': 'paris',
    },
}
for username, user_info in users.items():  # define items
    print(f'\nUsername: {username}')
    # combine to full name
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']  # pull location
    print(f'\tFull name: {full_name.title()}')
    print(f'\tlocation: {location.title()}')
# -----
# exercices p. 111 6-7 people
info_1 = {
    'name': 'tom',
    'last name': 'liddle',
    'age': 31,
    'city': 'Kaunas'
}
info_2 = {
    'name': 'steve',
    'last name': 'newman',
    'age': 20,
    'city': 'Vilnius'
}
info_3 = {
    'name': 'sal',
    'last name': 'montano',
    'age': 18,
    'city': 'Tokyo'
}

people = [info_1, info_2, info_3]

for person in people:
    print("\nPerson:")
    for key, value in person.items():
        print(f"\t{key.title()}: {value}")
# exercices p. 111 6-8 pets
pet_info = {
    'animal': 'cat',
    'owner': 'tom',
}
pet_info_1 = {
    'animal': 'dog',
    'owner': 'mark',
}
pet_info_2 = {
    'animal': 'rat',
    'owner': 'eddie',
}
pets = [pet_info, pet_info_1, pet_info_2]
for pet in pets:
    print('Pet info: ')
    for key, value in pet.items():
        print(f'\t{key.title()}: {value.title()}')
# exercices p. 111 6-9 pets
favorite_places = {
    'tom': ['london', 'moscow', 'new-york'],
    'eddie': ['tokyo', 'madrid', 'paris'],
    'eji': ['osaka', 'kaunas', 'new-york'],
    'sal': ['tokyo', 'madrid', 'brussels'],
}
for key, places in favorite_places.items():
    print(
        f"{key.title()}'s favorite places are: ")
    for place in places:
        print(f"\t{place.title()}")

# exercices p. 111 6-10 pets
users = {
    'aeinsten': {
        'first': ['albert'],
        'last': ['einstein'],
        'lnumbers': [5, 7, 8, 19],
    },
    'mcurie': {
        'first': ['marie'],
        'last': ['ecurie'],
        'lnumbers': [2, 8, 34, 11],
    },
}
for user, values in users.items():
    print(f'{user.title()}')
    for value in values:
        print(f"{value.title()}: {values[value]}")
# exercices p. 111 6-11 cities
cities = {
    'london': {
        'country': 'england',
        'population': '9.1 Million population',
        'fact': 'Highest GDP city in Europe'
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 Million population',
        'fact': 'One of the largest cities on earth'
    },
    'vilnius': {
        'country': 'lithuania',
        'population': '0.54 Million population',
        'fact': 'Has the oldest university in Europe'
    },
}

print('Here is information about a few of worlds most famous cities:')

for city, info in cities.items():
    print(f'\n{city.title()}:')
    for key, value in info.items():
        print(f"  {key.title()}: {value}")
# exercices p. 111 6-12 cities
cities = {
    'london': {
        'country': 'england',
        'population': '9.1 Million population',
        'fact': 'Highest GDP city in Europe'
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 Million population',
        'fact': 'One of the largest cities on earth'
    },
    'vilnius': {
        'country': 'lithuania',
        'population': '0.54 Million population',
        'fact': 'Has the oldest university in Europe'
    },
}

print('Here is information about a few of worlds most famous cities:')

for city, info in cities.items():
    print(f'\n{city.title()}:')
    for key, value in info.items():
        print(f"  {key.title()}: {value}")

# Add a new city
cities['berlin'] = {
    'country': 'germany',
    'population': '3.7 Million population',
    'fact': 'Fifth largest city in Europe'
}

print('\nHere is information after adding Berlin:')

for city, info in cities.items():
    print(f'\n{city.title()}:')
    for key, value in info.items():
        print(f"  {key.title()}: {value}")
# ====================End===========================
# ------------------------------------------------------------
# Notes on lists, dictionaries, and adding new entries in Python
# ------------------------------------------------------------
#
# 1. Lists vs Dictionaries:
#    - Lists grow with .append()
#      Example:
#          my_list.append('new item')
#
#    - Dictionaries DO NOT have .append()
#      Dictionaries grow by assignment:
#          my_dict['new_key'] = value
#
# 2. Looping through dictionaries:
#    - Looping through a dict gives you KEYS:
#          for key in my_dict:
#              print(key)          # key only
#              print(my_dict[key]) # value
#
#    - To get both key and value directly, use .items():
#          for key, value in my_dict.items():
#              print(key, value)
#
# 3. When dictionary values are lists:
#    - You must index into the dictionary to get the list:
#          for key in my_dict:
#              print(my_dict[key])   # prints the list
#
#    - Then you can loop the list if needed:
#          for item in my_dict[key]:
#              print(item)
#
# 4. Adding a new nested dictionary entry:
#    - Correct way:
#          cities['berlin'] = {
#              'country': 'germany',
#              'population': '3.7 Million population',
#              'fact': 'Fifth largest city in Europe'
#          }
#
#    - Wrong way:
#          cities.append(...)   # DOES NOT exist for dicts
#
# 5. Common mistake to avoid:
#    - Looping over a string by accident:
#          for c in city:   # city is a string like 'london'
#              ...
#      This loops over letters, not dictionary keys.
#
#    - Correct inner loop for nested dictionaries:
#          for key, value in info.items():
#              print(key, value)
# ------------------------------------------------------------
