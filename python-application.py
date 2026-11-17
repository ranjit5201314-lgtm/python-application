def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def main():
    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
    }

    while True:
        print("\nSimple Calculator")
        print("-----------------")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select 1-5.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        name, func = operations[choice]
        try:
            result = func(a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
