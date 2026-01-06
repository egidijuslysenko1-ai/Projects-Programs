# Section 5, if statements
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':  # conditional test (if is a conditional expression)
        print(car.upper())
    else:
        print(car.title())

# checking for equality in python is case sensitive
# 'Audi' is not equal 'audi'
car = 'Audi'
car.lower() == 'audi'  # this value is not stored/overriden
car  # still prints the original value
# ====================End===========================
# checking for inequality !=
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':  # if other than, print
    print('Hold the anchovies!')
# in this example if anchovies entered nothing prints, as value not defined in this case
user_menu_input = 'd'
if user_menu_input != 'c':  # if other than, print
    print('exiting the program')
# ----
answer = 41
if answer != 42:
    print('thats not the correct answer')
answer = 16
if answer <= 21:
    print('Show ID')
# ====================End===========================
# Multiple conditions
# testing two conditions, if both pass True, if one or both fail False
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21  # prints False

age_1 = 24  # change age, prints True
check1 = age_0 >= 21 and age_1 >= 21
if check1 == True:
    print(f'Ages of people are {age_0} and {age_1}')
# ====================End===========================
# checking for value in a list
# check lists with `variable` in list/array
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings  # prints true
'pepperoni' in requested_toppings
# very good for testing lists to see if value is in your list

# checking if a value is not in the list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:  # to check if user not in list, then:
    print(f'{user.title()}, you can post a response if you wish.')
# p.77 exercises
guests = ['marry', 'gary', 'sally']
new_guest = 'marry'
if new_guest in guests:
    print(f'Hey {new_guest} welcome back!')
# -----
user1 = 'Lithuania'
user2 = 'Japan'

user1 == 'Lithuania' and user2 == 'Japan'
user2 = 'Argentina'
user1 == 'Lithuania' and user2 == 'Japan'
# for basic conditionals  use and. for booleans if
user1 == 'Russia' or user2 == 'Argentina'
# -----
list_laundry = ['soap', 'detergent', 'whitener']
item_list = 'soap'
if item_list in list_laundry:
    print(f'{item_list} is in the list')
item_list = 'softener'
if item_list not in list_laundry:
    print(f'{item_list} is not yet in the list')
# -----
Answer3 = 45
if Answer3 <= 50 and Answer3 >= 43:
    print('Your answer is very close')
# quick quadratics check program
print("What are the answers to this quadratic equation?")
answer4 = (-2, 2)
# Check if both answers are correct
if set(answer4) == {3, -3}:
    print(f"Your answers {answer4} are correct!")
# Check if at least one answer is correct
elif 3 in answer4 or -3 in answer4:
    print(f"You got at least one correct value in {answer4}!")
# None are correct
else:
    print("None of the answers are correct.")
# -----
list_laundry = ['soap', 'detergent', 'whitener']
item_laundry = 'softener'
if item_laundry not in list_laundry:
    print(f'{item_laundry.title()} not yet in the list')
# -----
array = []
for digit in range(1, 21):
    array.append(digit/2)
print(array)
if 6/2 in array:
    print("Digit 3 is in the array")
# ====================End===========================
# if statements p.78
# if conditional_test
 # do somethings
# if-else syntax, allows to define an action when when condition fails.

age = int(input("Input your age: "))  # run whole file, we define input as int
if age >= 17:
    print("You are old enough to vote!")
else:
    print("Sorry, too young to vote.")
# ============================================================
# Why "Run Selected Code" fails for input() and if/else blocks
# ------------------------------------------------------------
# VS Code's "Run Selected Code" uses the Code Runner extension,
# NOT the real Python interpreter.
#
# Code Runner:
#   - does NOT support input()
#   - does NOT support multi-line Python blocks (if/else, loops)
#   - does NOT preserve Python indentation rules
#   - sends code to PowerShell instead of Python
#
# As a result:
#   - input() causes: "The term 'input' is not recognized"
#   - if/else causes PowerShell syntax errors
#   - indentation inside blocks causes "unexpected indent"
#
# This is NOT a Python error. The code works perfectly when run
# in a real Python environment.
#
# To run code with input() or multi-line blocks:
#   1. Run the entire file (Ctrl+F5), OR
#   2. Use the integrated terminal: python myfile.py, OR
#   3. Disable Code Runner for Python.
#
# Summary:
#   "Run Selected Code" is fine for simple prints and expressions,
#   but NOT for interactive or multi-line Python logic.
# ====================End===========================
# The if-elif-else Chain
# used when we have two and more conditions
age = 13
if age < 4:
    print('Your admission cost is 0$')
elif age < 18:
    print('Your admission cost is 25$')
else:
    print('Your admission csot is 40$')
# ------------------------------------------------------------
# Python if / elif / else logic summary
#
# 1. Use "if + else" when there are only TWO possible outcomes.
#    Example:
#        if condition:
#            ...
#        else:
#            ...
#
# 2. Use "if + elif + else" when there are THREE or more outcomes.
#    Example:
#        if condition1:
#            ...
#        elif condition2:
#            ...
#        else:
#            ...
#
# 3. You can have as many "elif" blocks as you need.
#    Example with 5 conditions:
#        if cond1:
#            ...
#        elif cond2:
#            ...
#        elif cond3:
#            ...
#        elif cond4:
#            ...
#        else:
#            ...
#
# 4. The "else" block is optional.
#    Use it only when you want a guaranteed fallback case.
#    A fallback case means: "everything else that didn't match above".
#
# 5. Every chain must start with "if".
#    "elif" and "else" cannot appear without an initial "if".
#
# 6. Only ONE block in the chain will run.
#    Python checks from top to bottom and stops at the first True condition.
#
# ------------------------------------------------------------
# another example of previous script:
age = int(input('Enter age:'))
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f'Your admission cost is {price}$')
# -----
age = 73
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f'Your admission cost is {price}$')
# -----
age = 73
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f'Your admission cost is {price}$')
# else block is a catchall statement and can sometimes include invalid or even malicious data
# it is more confident to run code only under certain conditions using if-elif

# For code that needs two conditions and more to be True we can use if statements only. Example: !
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('coming right up')
if 'pepperoni' in requested_toppings:  # will not be printed
    print('adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('adding extra cheese')
print('Finished making your pizza')

# this code would not work using only if-elif-else, because after satisfying one condition, stops
# ====================End===========================
# exercises p.84 5-3
alien_color = 'green'  # pass
if alien_color == 'green':
    print('you get five points')
else:
    print('No points given')
# -----
alien_color = 'red'  # fail
if alien_color == 'green':
    print('you get five points for shooting the alien')
else:
    print('No points given')
# -----
alien_color = 'green'  # pass
if alien_color == 'green':
    print('you get five points')
else:
    print('You earned 10 points')
# -----
alien_color = 'blue'  # pass
if alien_color == 'green':
    print('you get five points')
if alien_color != 'green':
    print('You earned 10 points')
# 5-5
alien_color = 'red'  # 1
if alien_color == 'green':
    print('you get five points')
elif alien_color == 'yellow':
    print('you get ten points')
elif alien_color == 'red':
    print('you get fifteen points')
#
alien_color = 'yellow'  # 2
if alien_color == 'green':
    print('you get five points')
elif alien_color == 'yellow':
    print('you get ten points')
elif alien_color == 'red':
    print('you get fifteen points')
#
alien_color = 'green'  # 3
if alien_color == 'green':
    print('you get five points')
elif alien_color == 'yellow':
    print('you get ten points')
elif alien_color == 'red':
    print('you get fifteen points')
# 5-6
age = 4
if age < 2:
    print('Person is a baby')
elif age >= 2 and age < 4:
    print('Person is a toddler')
elif age >= 4 and age < 13:
    print('Person is a kid')
elif age >= 13 and age < 20:
    print('Person is a teenager')
elif age >= 20 and age < 65:
    print('Person is an adult')
elif age >= 65:
    print('Person is an elder')
# 5-7
favorite_fruits = ['mango', 'mandarins', 'peach', 'pear', 'apple']
fruits = ['mango', 'mandarins', 'peach', 'pear', 'apple', 'ananas' 'berries']

for f in fruits:  # 1. loop through the big list
    if f in favorite_fruits:  # 2. check if the item is in the favorites list
        print(f'I really like {f}!')
# In a for-loop, the variable name (like f) is just a placeholder.
# Using if statements with lists
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry were out of green peppers')
    else:
        print(f'Adding {requested_topping}')
print('Finished making your pizza!')
# -----
requested_toppings = []
if requested_toppings:  # checks if there are items inside ! Important check
    for requested_topping in requested_toppings:  # loop
        print(f'Adding {requested_topping}')
    print('\nFinished making your pizza!')
else:
    print(f'Are you sure you want a plain pizza?')
# -----
available_toppings = ['mushrooms', 'green peppers', 'extra cheese',
                      'olives', 'pineapple', 'pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:  # simmilar to previous. checks for items in original list
        print(f'Adding {requested_topping}')
    else:
        print(f'Sorry we dont have {requested_topping}')
print('\nFinished making your pizza!')
# -----
# p.88 5-8
usernames = ['admin', 'tom', 'mark', 'sal', 'bob']
for u in usernames:
    if u == 'admin':
        print(f'Hello {u.title()}, would you like to see a status report?')
    else:
        print(f'Hello {u.title()}, thank you for logging in again')
# p.88 5-9
usernames = []
if usernames:  # checks if list empty
    for u in usernames:
        if u == 'admin':
            print(f'Hello {u.title()}, would you like to see a status report?')
        else:
            print(f'Hello {u.title()}, thank you for logging in again')
else:
    print('We need to find some users!')
# p.88 5-10
current_users = ['mark', 'tom', 'mark', 'sal', 'bob']
new_users = ['TOM', 'jerry', 'filippe']
current_users_lower = [u.lower()
                       # turns all to lower cases by making a new set
                       for u in new_users]
# then we check new user set against current user
for u in current_users_lower:
    if u in current_users_lower:
        print(f'Username "{u}" already taken')
    else:
        print(f'Username "{u}" is available')
# p.88 5-11
numbers_list = list(range(1, 10))
for n in numbers_list:
    if n == 1:
        print(f'{n}st')
    elif n == 2:
        print(f'{n}nd')
    elif n == 3:
        print(f'{n}rd')
    else:
        print(f'{n}th')
# ====================End===========================
