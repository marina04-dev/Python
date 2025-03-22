def print_name(first_name, first_surname, details=False, second_name="", second_surname=""):
    if details:
        if second_name != "":
            print("Name: " + first_name + "-" + second_name)
        else:
            print("Name: " + first_name)
        if second_surname != "":
            print("Surname: " + first_surname + " " + second_surname)
        else:
            print("Surrname: " + first_surname)
    else:
        if second_name != "":
            print(f"{first_name}-{second_name} {first_surname} {second_surname}")
        else:
            print(f"{first_name} {first_surname} {second_surname}")
            
            
print_name("Charles", "Kane", second_name="Bob")
print_name("Kim", "Jet", second_name="Yo", second_surname="Kennedy")
