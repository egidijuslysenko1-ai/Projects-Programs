import random
from fractions import Fraction

# Function to calculate f(x) given coefficients and variable values


def f(coeffs, values):
    return sum(coeffs[v] * values[v] for v in coeffs)


while True:
    choice = input(
        "\nLinear Equation Program. For values, please enter Integers or numbers with decimals only\n"
        "Press [A] to define variables (compute f(x))\n"
        "Press [D] to solve for x\n"
        "Press any other key to exit\n"
        "Your choice: "
    ).lower()

    if choice == "a":   # ===A MODE: complex — multiple variables + constants===
        n_vars = random.randint(2, 6)  # random number of variables, up to 2-6
        variables = [f"x{i+1}" for i in range(n_vars)]
        coeffs = {v: random.randint(-10, 10) for v in variables}
        values = {v: random.randint(-5, 5) for v in variables}

        # Build and print equation string
        eq_string = " + ".join(f"{coeffs[v]}*{v}" for v in variables)
        print(f"\nEquation: f(x) = {eq_string}")

        # Ask user for each variable value individually
        user_values = {}
        for v in variables:
            user_values[v] = float(input(f"Enter value for {v}: "))

        result = f(coeffs, user_values)
        print("f(x) =", result)

    elif choice == "d":      # ===D MODE: simple — single variable linear equation===
        a = random.randint(-10, 10)
        while a == 0:  # avoid division by zero
            a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        x_real = random.randint(-10, 10)

        y = a * x_real + b

        print(f"\nSolve for x:")
        print(f"{a}x + {b} = {y}")

        x_guess = float(input("Enter x: "))

        # Float number comparison for actual answer, 1e-6 defined as smallest margin of difference
        if abs(x_guess - x_real) < 1e-6:
            print("Correct!")
        else:
            print(f"Incorrect. The correct x was {x_real}")

    else:
        print("\nGoodbye!")
        break
