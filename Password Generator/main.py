import random
import string
import sys

print("\n🔐 Welcome to Devanshu's Advanced Password Generator 🔐\n")

length = int(input("Enter your password length: "))
num_password = int(input("How many passwords do you want?: "))

include_digits   = input("Include digits? (y/n): ").lower() == "y"
include_upper    = input("Include uppercase letters? (y/n): ").lower() == "y"
include_lower    = input("Include lowercase letters? (y/n): ").lower() == "y"
include_symbols  = input("Include symbols? (y/n): ").lower() == "y"

all_chars = ""

if include_digits:
    all_chars += string.digits
if include_upper:
    all_chars += string.ascii_uppercase
if include_lower:
    all_chars += string.ascii_lowercase
if include_symbols:
    # Using all punctuation + custom symbols (optional)
    all_chars += string.punctuation + "@#$%&"

if not all_chars:
    print("❌ Error: No character set selected!")
    sys.exit()

print("\n🧾 Generated Passwords:")

for i in range(num_password):
    password = "".join(random.choice(all_chars) for _ in range(length))

    if length < 6:
        strength = "Weak"
    elif 6 <= length <= 10:
        strength = "Medium"
    else:
        strength = "Strong"

    print(f"\n🔐 Password {i+1}: {password}  \n➤ Strength: {strength}")
