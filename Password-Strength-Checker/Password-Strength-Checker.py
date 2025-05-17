import random
import string

def calculate_strength(password):
    score = 0
    
    length = len(password)
    if length >= 13:
        
        score = 3  # Strong password

    elif length > 8 and length <= 12:

        score = 2  # Fair password

    else:
        score = 1  # Weak password

    return score

def generate_stronger_password():
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+[]{|};:,.<>?/~`\"'"
    
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=5)
    
    random.shuffle(password)
    
    return ''.join(password)

print("Your password must meet the following requirements:")
print("- At least 2 uppercase letters")
print("- At least 2 lowercase letters")
print("- At least 2 digits")
print("- At least 1 special character (e.g., !@#$%^&*)")
print("- Minimum length of 8 characters")

while True:
    password = input("\nEnter your password: ")

    uppercase_count = sum(1 for c in password if c.isupper())
    lowercase_count = sum(1 for c in password if c.islower())
    digit_count = sum(1 for c in password if c.isdigit())
    special_count = sum(1 for c in password if c in "!@#$%^&*()_+[]{|};:,.<>?/~`\"'")

    if len(password) >= 8 and uppercase_count >= 2 and lowercase_count >= 2 and digit_count >= 2 and special_count >= 1:

        strength_score = calculate_strength(password)

        if strength_score == 1:
            print("Password Strength: Weak")
            print("Suggested Stronger Password:", generate_stronger_password())
        elif strength_score == 2:
            print("Password Strength: Fair")
        else:
            print("Password Strength: Strong")

        break
    else:
        print("Password is missing some requirements. Please try again.")
        
        if len(password) < 8:
            print("- Minimum length of 8 characters")
        if uppercase_count < 2:
            print("- At least 2 uppercase letters")
        if lowercase_count < 2:
            print("- At least 2 lowercase letters")
        if digit_count < 2:
            print("- At least 2 digits")
        if special_count < 1:
            print("- At least 1 special character")
        
        print("Password Strength: Weak")

        print("Suggested Stronger Password:", generate_stronger_password())
