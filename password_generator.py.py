import random
import string

def generate_password(length, complexity):
    characters = string.ascii_lowercase  # Start with lowercase letters
    
    if complexity >= 2:
        characters += string.ascii_uppercase  # Add uppercase letters
    if complexity >= 3:
        characters += string.digits  # Add digits
    if complexity >= 4:
        characters += string.punctuation  # Add special characters
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator Application")
    
  
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as ve:
            print(ve)
    
   
    print("\nSelect password complexity:")
    print("1. Lowercase letters only")
    print("2. Lowercase and uppercase letters")
    print("3. Lowercase, uppercase, and digits")
    print("4. Lowercase, uppercase, digits, and special characters")
    
    while True:
        try:
            complexity = int(input("Enter complexity level (1-4): "))
            if complexity not in range(1, 5):
                raise ValueError("Complexity must be between 1 and 4.")
            break
        except ValueError as ve:
            print(ve)
    
    password = generate_password(length, complexity)
    print("\nGenerated Password:", password)

if _name_ == "_main_":
    main()
