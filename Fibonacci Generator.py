# FIBONACCI GENERATOR

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_generator(terms):
    for i in range(terms):
        yield fibonacci_recursive(i)


# user input for the number of terms
terms = int(input("Enter the number of terms for Fibonacci series: "))

# Check if the input is valid
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series using recursion:")

    # Generate and print Fibonacci numbers using the generator
    fibonacci_gen = fibonacci_generator(terms)
    for _ in range(terms):
        print(next(fibonacci_gen), end=" ")

# Additional calculator functionality
while True:
    option = input("\nDo you want to perform more calculations? (yes/no): ").lower()
    if option != 'yes':
        break

    additional_terms = int(input("Enter the number of additional terms: "))
    if additional_terms <= 0:
        print("Please enter a positive integer.")
    else:
        print("Additional Fibonacci series:")

        # Create a new generator for additional calculations
        additional_gen = fibonacci_generator(additional_terms)

        for _ in range(additional_terms):
            print(next(additional_gen), end=" ")
