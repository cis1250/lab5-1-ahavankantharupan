#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def positive_integer(prompt):
    user_input = input(prompt)

    # Repeat until a valid positive integer is entered will not except a negeative number 
    while not user_input.isdigit() or int(user_input) <= 0:
        print("Please enter a number greater than 0.")
        user_input = input(prompt)

    return int(user_input)

def make_fibonacci(x):
    fib_sequence = []
    num1= 0
    num2= 1

    for i in range(x):
        fib_sequence.append(num1)
        temp = num1 + num2
        num1 = num2
        num2 = temp

    return fib_sequence

def main():
    print("Fibonacci Sequence Generator")
    num_terms = get_positive_integer("Enter the number of terms: ")

    print("\nFirst", num_terms, "terms of the Fibonacci sequence:")
    fibonacci = generate_fibonacci(num_terms)

    for num in fibonacci:
        print(num)

# Run the program
main()
