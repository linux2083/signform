import getpass

def authenticate_user():
    # Prompt user for username
    username = input("Enter your username: ")

    # Prompt user for a password securely
    user_password = getpass.getpass("Enter your password: ")

    # Simulate basic authentication logic
    if validate_credentials(username, user_password):
        print(f"Welcome, {username}! Authentication successful!")
        access_dashboard(username)
    else:
        print("Authentication failed. Incorrect username or password.")

def validate_credentials(username, password):
    # In a real-world scenario, validate credentials against a database or external service
    # For simplicity, using hardcoded values here
    return username == "user123" and password == "securepassword"

def access_dashboard(username):
    # Simulate accessing a user's dashboard or main menu
    print(f"\n{username}'s Dashboard:")
    print("1. View Profile")
    print("2. Change Password")
    print("3. Logout")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_profile(username)
    elif choice == "2":
        change_password(username)
    elif choice == "3":
        print("Logout successful. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

def view_profile(username):
    # Simulate displaying the user's profile information
    print(f"\nProfile Information for {username}:")
    print("Full Name: John Doe")
    print("Email: john.doe@example.com")
    print("Joined: January 1, 2022")

def change_password(username):
    # Simulate allowing the user to change their password
    new_password = getpass.getpass("Enter your new password: ")
    print(f"Password for {username} changed successfully!")

if __name__ == "__main__":
    authenticate_user()
