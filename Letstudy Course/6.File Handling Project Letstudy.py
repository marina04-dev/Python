choice = True
while choice:
    print("Menu")
    print("1-Insert Email")
    print("2-List All Emails")
    print("3-Search For An Email")
    print("0-Exit")
    choice = int(input("Enter your choice (1,2,3) or 0 to exit: "))
    if choice == 1:
        email = input("Enter an email address: ")
        with open('data.txt', 'a') as myfile:
            myfile.write(email+'\r')
    if choice == 2:
        with open('data.txt', 'r') as myfile:
            print(myfile.read())
    if choice == 3:
        found = False
        email = input("Enter the email you want to find: ")
        with open('data.txt', 'r') as myfile:
            for row in myfile:
                if row.strip() == email:
                    found = True
        if found:
            print("Email Found In The File")
        else:
            print("Email Does Not Exist In The File")
