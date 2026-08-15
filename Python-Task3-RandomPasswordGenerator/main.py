import random
import string

print("==============================")
print("  RANDOM PASSWORD GENERATOR  ")
print("==============================")


while True:

    # Get password length
    while True:
        try:
            length = int(input(
                "\nEnter the length of your password (minimum 8): "
            ))

            if length < 8:
                print("ERROR: Password length must be at least 8.")
            else:
                break

        except ValueError:
            print("ERROR: Please enter a valid number.")


    # Character types
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    print("\nChoose Character Type:")
    print("1. Uppercase")
    print("2. Lowercase")
    print("3. Digits")
    print("4. Symbols")

    # Get character choices
    while True:

        choices = input(
            "Enter your choices (example: 1234 or 23): "
        )

        # Check whether input contains only numbers
        if not choices.isdigit():
            print("ERROR: Please enter numbers only (1, 2, 3, 4).")
            continue

        # Remove duplicate choices
        choices = set(choices)

        # Check whether only 1, 2, 3, 4 were selected
        if not choices.issubset({"1", "2", "3", "4"}):
            print("ERROR: Please choose only 1, 2, 3, or 4.")
            continue

        # At least 2 character types
        if len(choices) < 2:
            print("ERROR: Please select at least 2 character types.")
            continue
        break

    # Create character pool
    characters = ""

    if "1" in choices:
        characters += uppercase

    if "2" in choices:
        characters += lowercase

    if "3" in choices:
        characters += numbers

    if "4" in choices:
        characters += symbols

    password = ""

    if "1" in choices:
        password += random.choice(uppercase)

    if "2" in choices:
        password += random.choice(lowercase)

    if "3" in choices:
        password += random.choice(numbers)

    if "4" in choices:
        password += random.choice(symbols)


    # Fill the remaining password characters
    remaining_length = length - len(password)

    for i in range(remaining_length):
        password += random.choice(characters)


    # Shuffle password
    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)


    # Display password
    print("\n==============================")
    print("Your Generated Password is:")
    print(password)
    print("==============================")


    # another password
    again = input(
        "\nDo you want to generate another password? (y/n): "
    )

    if again.lower() == "y":
        continue
    else:
        print("\n-------Thank you for using Random Password Generator!-------")
        break