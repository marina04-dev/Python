# exercise 7: json files
import json

try:
    with open("reminders.json") as f:
        reminders = json.load(f)
except FileNotFoundError:
    reminders = []
    
while True:
    print("1-Add Reminder")
    print("2-Remove Reminder")
    print("3-Print Reminders")
    print("4-Exit")
    choice = int(input("Please enter your choice: "))
    if (choice == 1):
        reminder = input("New reminder: ")
        reminders.append(reminder)
        with open("reminders.json") as f:
            json.dump(reminders, f)
    elif (choice == 2):
        reminder_index = int(input("Please enter the index of the reminder: "))
        reminders.pop(reminder_index)
        with open("reminders.json") as f:
            json.dump(reminders, f)
    elif (choice == 3):
        for i in range(len(reminders)):
            print(f"{i}. {reminders[i]}")
    elif (choice == 4):
        print("Exit")
        break
