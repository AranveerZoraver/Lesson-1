# ASCII Value Checker
# Reveals the ASCII code behind a character and identifies its type

# Step 1: Get a character from the user
user_input = input("Enter a single character: ")

# Step 2: Validate that the input is a string of exactly one character
if type(user_input) is str and len(user_input) == 1:
    char = user_input

    # Step 3: Get the ASCII value using ord()
    ascii_value = ord(char)
    print(f"Character: {char}")
    print(f"ASCII Value: {ascii_value}")

    # Step 4: Categorize the character
    if char.isupper():
        char_type = "Uppercase letter"
    elif char.islower():
        char_type = "Lowercase letter"
    elif char.isdigit():
        char_type = "Digit"
    else:
        char_type = "Special character"

    print(f"Character Type: {char_type}")

else:
    print("Invalid input. Please enter exactly one character.")