import random
import string

def generate_password(length=12):
    # Define the characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter desired password length: "))
    password = generate_password(password_length)
    print("Generated Password:", password)
