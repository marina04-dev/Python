# Hour Presentation Program (with error input checking)
# Exercise 9 (If)
while True:
    hours = input("Enter the amount of hours: ").strip()
    minutes = input("Enter the amount of minutes: ").strip()
    seconds = input("Enter the amount of seconds: ").strip()
    if hours.isdigit() and minutes.isdigit() and seconds.isdigit():
        new_hours = int(hours)
        new_minutes = int(minutes)
        new_seconds = int(seconds)
        if len(hours)==1 and len(hours)>=2:
            n_hours = "0" + str(new_hours)
        elif len(hours)>2:
            print("Wrong amount of numbers! They must be at least 2!")
            continue
        else:
            n_hours = str(new_hours)
        if len(minutes)==1 and len(minutes)>=2:
            n_minutes = "0" + str(new_minutes)
        elif len(minutes)>2:
            print("Wrong amount of numbers! They must be at least 2!")
            continue
        else:
            n_minutes = str(new_minutes)
        if len(seconds)==1 and len(seconds)>=2:
            n_seconds = "0" + str(new_seconds)
        elif len(seconds)>2:
            print("Wrong amount of numbers! They must be at least 2!")
            continue
        else:
            n_seconds = str(new_seconds)
        print(n_hours + ":" + n_minutes + ":" + n_seconds)
        break
    else:
        print("Wrong Input! Please enter only digits and not more than 2 digits!")
        continue
    
    
