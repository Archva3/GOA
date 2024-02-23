def register_user():
    # Get user input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")

    # Print user information
    print("\nRegistration Details:")
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Age:", age)


if __name__ == "__main__":
    register_user()


def perform_operations():
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        # Perform operations
        print("\nResults:")
        print("Multiplication:", num1 * num2 * num3)
        print("Division:", num1 / num2 / num3)
        print("Addition:", num1 + num2 + num3)
        print("Subtraction:", num1 - num2 - num3)


if __name__ == "__main__":
    perform_operations()