import random
import string

# Function to calculate password strength based on length
def calculate_strength(password):
    score = 0
    
    # Length criteria (weak, fair, strong)
    length = len(password)
    if length >= 13:
        score = 3  # Strong password
    elif length > 8 and length <= 12:
        score = 2  # Fair password
    else:
        score = 1  # Weak password

    return score

# Function to generate a stronger password
def generate_stronger_password():
    # Define the character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+[]{|};:,.<>?/~`\"'"
    
    # Ensure the password meets the minimum requirements
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the remaining characters with random choices to ensure at least 12 characters
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=5)  # Adding more characters to make the length 12 or more
    
    # Shuffle to make the password random
    random.shuffle(password)
    
    # Convert the list to a string
    return ''.join(password)

# Display password requirements to the user
print("Your password must meet the following requirements:")
print("- At least 2 uppercase letters")
print("- At least 2 lowercase letters")
print("- At least 2 digits")
print("- At least 1 special character (e.g., !@#$%^&*)")
print("- Minimum length of 8 characters")

# Step 1: Take user input and ensure the password meets all conditions
while True:
    password = input("\nEnter your password: ")

    # Check password length and character diversity together
    uppercase_count = sum(1 for c in password if c.isupper())  # Count uppercase letters
    lowercase_count = sum(1 for c in password if c.islower())  # Count lowercase letters
    digit_count = sum(1 for c in password if c.isdigit())  # Count digits
    special_count = sum(1 for c in password if c in "!@#$%^&*()_+[]{|};:,.<>?/~`\"'")  # Count special characters

    # Check if the password meets all conditions
    if len(password) >= 8 and uppercase_count >= 2 and lowercase_count >= 2 and digit_count >= 2 and special_count >= 1:
        # Calculate and display password strength
        strength_score = calculate_strength(password)

        # Give feedback based on score
        if strength_score == 1:
            print("Password Strength: Weak")
            # Suggest a stronger password
            print("Suggested Stronger Password:", generate_stronger_password())
        elif strength_score == 2:
            print("Password Strength: Fair")
        else:
            print("Password Strength: Strong")

        break  # Exit the loop if the password meets all conditions
    else:
        print("Password is missing some requirements. Please try again.")
        
        # Display which types are missing
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
        
        # Explicitly tell the user the password is weak
        print("Password Strength: Weak")

        # Suggest a stronger password
        print("Suggested Stronger Password:", generate_stronger_password())
