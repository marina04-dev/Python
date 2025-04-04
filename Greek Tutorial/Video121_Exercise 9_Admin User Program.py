# exercise 9: admin-user program (user)
import json

try:
    with open("users.json") as f:
        users = json.load(f)
except FileNotFoundError:
    users = []
    
username = input("Please enter username: ")
password = input("Please enter password: ")

for user in users:
    if username == user["username"] and password == user["password"]:
        if user["role"] == "admin":
            print("Welcome Admin")
        elif user["role"] == "user":
            print("Welcome " + user["full_name"])
        break
    else:
        print("Wrong username or password!")
