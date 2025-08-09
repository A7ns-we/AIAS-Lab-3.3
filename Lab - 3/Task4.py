def register_user(users_db):
    print("=== Register User ===")
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already exists. Please try a different username.")
        return
    password = input("Enter a password: ")
    users_db[username] = password
    print("Registration successful!")

def login_user(users_db):
    print("=== Login User ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users_db and users_db[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password.")

def main():
    users_db = {}
    while True:
        print("\nSelect an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            register_user(users_db)
        elif choice == '2':
            login_user(users_db)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
