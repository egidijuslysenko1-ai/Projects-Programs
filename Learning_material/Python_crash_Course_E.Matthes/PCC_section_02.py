# Section 2 exercises. Section 1 focused on installation+setup of VS editor
# useful commands to exit cmd 1. ctrl+z and enter, also if print vas previously defined as variable use "del print"

import this
import this  # The Zen of Python, by Tim Peters
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = (f"Hey, {full_name.title()}!")
print(message)
print(f"How are you today, {full_name.title()}?")

print("Languages: \nPython\nC\nC#\nC++")
print("Languages: \n\tPython\n\tC\n\tC#\n\tC++")

name = " Einstein "
name
name = name.lstrip()
name
name = name.rstrip()
name

# .removeprefix use
nostarch_url = "https://yourwebsite.com"
nostarch_url
nostarch_url.removeprefix("https://")

new_website_removed = nostarch_url.removeprefix("https://")
new_website_removed


famous_person = "albert einstein"
message = '"A person who never made a mistake never tried anything new"'
print(f'{famous_person.title()} once said, \n{message}\n\t{famous_person}')

# .lstrip() .rstrip() and .strip() section
name = " Albert Einstein "
name
print(name.lstrip(), "\tThis example strips whitespace from left side")
print(name.rstrip(), "\tThis example strips whitespace from right side")
print(name.strip(), "\tThis example strips whitespace from both sides")

# remove suffix
filename = "pytho_notes.txt"
filename.removesuffix(".txt")

# Numbers operations (integers, floats)
3 ** 2
2 + 3*4
(2 + 3) * 4
2 * 0.2

# =========================
# explanation about floats, run this code snippet
# =========================


def f():
    calc = 0.2 + 0.1
    explanation = (
        "Good example of float arithmetic: 0.2 + 0.1 does not equal 0.3 exactly.\n"
        "That's why we avoid comparing floats with == and instead use thresholds."
    )

    print(f"Result of 0.2 + 0.1: {calc}")
    print(explanation)

    # demonstration
    print("\nChecking if calc == 0.3:")
    check = calc == 0.3
    # This will print FALSE cause of the difference of e-17. This is due to PYTHON internal calculations/representation
    print(check)


f()
# =========================

4/2  # dividing integers always gets a float
1+2.0  # same for integer + float arithmetics, will always yield a float
universe_age = 14_000_000_000
print(universe_age)  # large numbers sometimes grouped by _
x, y, z = 1, 0, 2  # assign values to multiple variables
MAX_CONNECTIONS = 5000  # for variables uppercases

# =========================
# important concept of Python Zen simplicity
# import this  <--- Python philosophy explanation, enter in to terminal
# python
# import this
# =========================
