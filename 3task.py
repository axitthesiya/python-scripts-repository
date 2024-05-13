import re

def check_username(username):
    errors = []
    if '.' not in username:
        errors.append("Username should have at least one '.' 🔐🔴")
    if '_' not in username:
        errors.append("Username should have at least one '_' 🔐🔴")
    if len(username) < 8:
        errors.append("Username should be at least 8 characters long 🔐🔴")
    return errors

def check_password(password):
    errors = []
    if not re.search(r'[!@#$%]', password):
        errors.append("Password should have at least one of '@', '#', '$', or '%' 🔐🔴")
    if not re.search(r'[A-Z]', password):
        errors.append("Password should have at least one uppercase letter 🔐🔴")
    if not re.search(r'[a-z]', password):
        errors.append("Password should have at least one lowercase letter 🔐🔴")
    if not re.search(r'[0-9]', password):
        errors.append("Password should have at least one digit from 0-9 🔐🔴")
    return errors

def main():
    print("🔴 🟡 🟢 Your Whole System Will Lock Please Enter Your Secrate Code And Unlock Your Systeam... 🔴 🟡 🟢")
    username = input("Enter username: ")
    password = input("Enter password: ")

    username_errors = check_username(username)
    password_errors = check_password(password)

    if username_errors:
        print("Username errors:")
        for error in username_errors:
            print(error)
    if password_errors:
        print("Password errors:")
        for error in password_errors:
            print(error)

    if not username_errors and not password_errors:
        print("That Username and password requirements are fullfilled...🔓🟢🚀")
        print("\n")
        print("Login successfully in whole system are crashed...!!!📂🟢🚀")

if __name__ == "__main__":
    main()

