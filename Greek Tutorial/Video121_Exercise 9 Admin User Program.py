# exercise 9: admin-user program (admin)
import json

try:
    with open("users.json") as f:
        users = json.load(f)
except FileNotFoundError:
    users = []
    
while True:
    print("1-New User")
    print("2-Exit")
    choice = int(input("Please enter your choice: "))
    
    if choice == 1:
        user = {}
        user["full_name"] = input("Please enter your fullname: ")
        user["username"] = input("Please enter your username: ")
        user["password"] = input("Please enter your password: ")
        user["role"] = input("Please enter your role (admin or user): ")
        users.append(user)
    elif choice == 2:
        with open("users.json", "w") as f:
            json.dump(users,f)
        break
