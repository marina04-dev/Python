# String Validation - Formatted Output(Lesson 9: Exercise 6)
while True:
    name = input("Enter you name: ").strip()
    if name.isalpha():
        new_name = name.capitalize()
        print(f"Name Entered: {new_name}")
        break
    else:
        print("Enter Only Characters Please!")
        
        
while True:
    surname = input("Enter you surname: ").strip()
    if surname.isalpha():
        new_surname = surname.capitalize()
        print(f"Surname Entered: {new_surname}")
        break
    else:
        print("Enter Only Characters Please!")
        
print(f"+{28*'-'}+")
print(f"|{(name+ ' ' + surname).center(28)}|")
print(f"+{28*'-'}+")
