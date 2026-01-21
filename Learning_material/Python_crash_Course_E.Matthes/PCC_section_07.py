# user input and while loops. Exercises with Input() and concentrating strings
# Run only with terminal -> run this file. sections dont run. Run in Python REPL.
# to run code in python REPL, type in python or py: should show:
# Python 3.12.1 (tags/...)
# >>>
# when this is shown were working with python REPL. gotta split codes before Input()
# otherwise it recognizes it as the answer and skips code. so copy-paste multiple times

message = input("Tell me something, and I will repeat it back to you: ")
print(message)
# some text eidtors wont run promts with user input, so we need to run in terminals.
# -----
name = input('Please enter your name: ')
print(f"\nHello! {name}")
# -----
prompt = "if you share your name, we can personalize the messages you see."
# “Take the current value of prompt, add this new string to it, and store the result back into prompt.”
prompt += "\nWhat is your first name?"
# += is string concentration

name = input(prompt)
print(f"\nHello, {name}")
# -----
age = input('how old are you?')
age
age >= 18  # gives error because interprets as string interpretation. a.k.a text
# error: TypeError: '>=' not supported between instances of 'str' and 'int'

# to fix this: use int'
age = input('how old are you?')
age = int(age)
age  # now displays without ''
age >= 18
# -----
height = input("how tall are you, in inches?")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYoul be able to ride when youre a little older.")
# when we use numerical inputs, gotta make sure to convert them to numerical representations, also this works too:
variable = int(input("your prompt here"))
# ----- The Modulo Operator (%), divides one number by another and returns the remainded
4 % 3
5 % 3
6 % 3
7 % 3  # useful to check odds, evens, multiples etc.
50 % 31
# Modulo operator doesnt tell how many numbers fit in to another, only the remainder
# ex:
number = int(input("Enter a number, and ill tell you if its even or odds: "))
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
# -----
# exercises 7- 1-3
car = input("Tell me what kind of rental car you would like? ")
print(f"Let me see if I can find you a {car.title()}")
# -----
q = int(input("How many people are in the dinner group? "))
if q >= 8:
    print("You will have to wait for a table")
else:
    print("Table is ready")
# -----
number_check = int(input("Tell me a number: "))
if number_check % 10 == 0:
    print(f"The number {number_check} is a 10 multiple")
else:
    print(f"The number {number_check} is not a 10 multiple")
# ====================End===========================
# While loops
# runs as long as certain conditions are true
current_number = 1
while current_number <= 5:  # runs as long as less or equal than 5
    print(current_number)
    current_number += 1  # keeps adding 1
# -----
# letting user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'Quit' to end the program: "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
# -----
# Letting the user choose when to quit
prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""  # Starting with "" ensures the loop runs at least once. othersie promts error
# this is standard sentinel loop, and we later re-define the message as input(prompt)
while message != 'quit':
    message = input(prompt)

    if message != 'quit':  # only primts the message if it doesnt match the quit value
        print(message)
# -----
# using a flag
# defining a variable that checks whether the whole program is active. TRUE-FALSE


# exercises 6-1
# ----- 6-3
prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
active = True  # flag . Program starts in an active state
while active:
    message = input(prompt)
    if message == 'quit':
        active == False  # loop stops
    else:
        print(message)
# -----
# using a break to exit a loop, without running any remaining code.
prompt = "\nPlease enter the name of a city you have visisted: "
prompt += "\nEnter 'quit' to end the program."

while True:
    city = input(prompt)
    if city == 'quit':  # break
        break
    else:
        print(f'Id love to go to {city.title()}')
# using continue in a loop
# can use continue statement to return to the begining of the loop, based on the results of a conditional test
current_number = int(input("Enter number 1 to 9: "))
while current_number < 10:
    current_number += 1  # take current number and add 1 to it
    if current_number % 2 == 0:  # shows remainder from modulo
        continue
    print(current_number)
else:
    print("Enter valid number")
# -----
# avoiding infinite loops.
# every while loop neds a way to stop running so it wont continue to run forever. example limit to 5 runs.
x = 1
while x <= 5:
    print(x)
    x += 1  # IF REMOVED WILL RUN FOREVER. Add 1 to x
# IF program gets stuck in an infinite loop can always use CTRL+C to stop

# ----- ex 123 p.
# 7-4
prompt = "\nEnter a topping for a pizza: "
prompt += "\nEnter 'quit' to quit the program: "
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f'\n\tIm adding {topping} topping to the pizza')
# 7-5
prompt = "\nEnter your age and I will tell you the ticket price: "
prompt += "\nEnter quit to quit: "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    if age <= 3:
        print("\n\tyour ticket is free")
    if age >= 3 <= 12:
        print("\n\tyour ticket is 10$")
    if age >= 15:
        print("\n\tyour ticket is 15$")
# ====================End===========================
# Using a while loop with lists and dictionaries
# modifying a list working with
# example of moving items from one list to another

# start with users that need to be verified,
# and en empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = []
# verification
while unconfirmed_users:  # runs as long as not empty list
    # .pop() removes one item from the list and returns it. shrinking the list
    current_user = unconfirmed_users.pop()
    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)
# display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# confirmed_users list is displayed in opposite order because of .pop item removal and adding
# -----
# removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:  # removes each instance of cat untill there is none left.
    pets.remove('cat')
    print(pets)
# -----
# filling a dictionary with user input
responses = {}
# set a flag to indicate that polling is active
polling_active = True
while polling_active:
    # pront for persons name and response
    name = input("\nWhat is your name? ")
    response = input("Which mounbtain would you like to climb someday? ")
    # store the response in the dictionary
    responses[name] = response
    # find out if anyone else is going to take the poll.
    repeat = input("would you like to let another person respont? (yes/no) ")
    if repeat == "no":
        polling_active = False
# polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f'{name} would like to climb {response}')
# -----
# exercises p.127
sandwich_orders = ["sub", "salami", "tuna", "salad", "wrap"]
finished_sandwiches = []
print(sandwich_orders)
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"preparing your {order.title()} order, please wait")
    finished_sandwiches.append(order)

print("\nThe following uorders have been confirmed: ")
for sandwich in finished_sandwiches:
    print(sandwich.title())
print(sandwich_orders)  # shows if order list is empty. Confirmation
# ----- 7-9
sandwich_orders = ["sub", "pastrami", "salami",
                   "tuna", "pastrami", "salad", "wrap", "pastrami"]
finished_sandwiches = []
print(f"\nWere very sorry we have ran out of Pastrami sandwiches")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"preparing your {order.title()} order, please wait")
    finished_sandwiches.append(order)

print("\nThe following uorders have been confirmed: ")
for sandwich in finished_sandwiches:
    print(sandwich.title())
# ----- 7-10
dream_vacation = {}
polling_active = True
while polling_active:
    name = input("What is your name?")
    destination = input("\nWhat is your dream destination? ")
    dream_vacation[name] = destination
    repeat = input("would you like to let another person respont? (yes/no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, destination in dream_vacation.items():
    print(f'{name} would like to climb {destination}')
# ====================End===========================
