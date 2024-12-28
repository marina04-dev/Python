# Data Project: CRUD - Create
pupils = [
    {
        "id": 1001,
        "name": "John",
        "surname": "Doe",
        "fathers_name": "Michael",
        "age": 11,
        "class": 1,
        "id_number": "AN123949"
    },
    {
        "id": 1002,
        "name": "Mary",
        "surname": "Poppins",
        "fathers_name": "Chris",
        "age": 10,
        "class": 3,
        "id_number": "AE123981"
    },
    {
        "id": 1003,
        "name": "John",
        "surname": "Wick",
        "fathers_name": "Chiwetel",
        "age": 7,
        "class": 6,
    }
]
while True:
    print("""1.Registration Creation\n2.Printing\n3.Registration Update\n4.Registration Cancelation\n5.Exit""")
    choice = int(input("Please press a number between 1 and 5 to make a choice: "))
    if (choice==1):
        print("New registration")
        print("===========================")
        name = input("Student's name: ")
        surname = input("Student's surname: ")
        father_name = input("Student's father name: ")
        check = [name,surname,father_name]
        
        stop=False
        for p in pupils:
            if name==p["name"] and surname==p["surname"] and father_name==p["father_name"]:
                print("The pupil you entered already exists!")
                ch input("Would you like to continue? If yes press y,if no press n: ")
                if (ch=="n") {
                    stop = True
                    break
                }
        if stop:
            continue
        
        age = int(input("Student's age: "))
        pupil_classs = int(input("Student's class: "))
        id_card = input("Does the student already have an id-card?: (Press:y for yes and n for no) ")
        if id_card=="y":
            id_number = input("Enter the id card number: ")
            
        pupil = {}
        pupil["name"]=name
        pupil["surname"]=surname
        pupil["father_name"]=father_name
        pupil["age"]=age
        pupil["class"]=pupil_class
        if id_card=="y":
            pupil["id_number"]=id_number
            
        ids = []
        for p in pupils:
            ids.append(p["id"])
        pupil["id"] = max(ids) + 1
        
        pupils.append(pupil)
        
        print("New Registration")
        print(f"Student's name: {pupil['name']}")
        print(f"Student's surname: {pupil['surname']}")
        print(f"Student's father name: {pupil['father_name']}")
        print(f"Student's age: {pupil['age']}")
        print(f"Student's class: {pupil['class']}")
        if (pupil["id_number"]):
            print(f"ID card number: {pupil['id_number']}")
            
    elif choice==2:
        pass
    elif choice==3:
        pass
    elif choice==4:
        pass
    elif choice==5:
        print("Exit of the programm!")
        break
        
        
    
