
# PROJECT 3: RANDOM PASSWORD GENERATOR
# DecodeLabs Industrial Training

import random
import string

print("================================")
print("     RANDOM PASSWORD GENERATOR")
print("================================")

# Ask the user for password length
try:
    length = int(input("Enter password length: "))

    if length < 2:
        print("Password length must be at least 2.")

    else:
        # Create letters and numbers
        characters = string.ascii_letters + string.digits

        # Generate password
        password = [
            random.choice(string.ascii_letters),
            random.choice(string.digits)
        ]

        # Generate remaining characters
        for i in range(length - 2):
            password.append(random.choice(characters))

        # Shuffle password characters
        random.shuffle(password)

        # Convert list to string
        final_password = ''.join(password)

        # Display password
        print("\nYour generated password is:")
        print(final_password)

        print("\nPassword generated successfully!")

except ValueError:
    print("Please enter a valid number.")