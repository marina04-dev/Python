def get_integer():
    while True:
        try:
            integer = input("Enter an integer number: ").strip()
            if integer == "":
                raise ValueError("No Digits Entered")
            elif not integer.isdigit():
                raise ValueError("Wrong Input! Only Digits Please!")
            new_integer = int(integer)
        except ValueError as v:
            print(v)
        except Exception as e:
            print(e)
        else:
            print(f"The Input Integer  is: {new_integer}") 
            break 
            
get_integer()
        
