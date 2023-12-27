import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Create a username")
    password = getpass.getpass("create a new password")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("You now have an account!")

def login():
    username = input("Enter your username")
    password = getpass.getpass("Enter your password")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("login successful")
    else:
        ("Invalid username or password")
     

def main():
    while True:
        choice = input("Enter 1 to create a new account, 2 to login to an existing account, or 3 exit")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid input please try again")

if __name__ == "__main__":
    main()