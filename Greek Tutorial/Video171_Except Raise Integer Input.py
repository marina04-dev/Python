def get_integer():
    while True:
        try:
            user_input = input("Enter an integer number: ").strip()
            if user_input[0] == "-":
                st = user_input[1:]
                if st == "":
                    raise ValueError("No Digits Entered")
                elif not st.isdigit():
                    raise ValueError("Wrong Input! Only Digits Please!")
                x = -int(st)
            else:
                st = user_input
                if st == "":
                    raise ValueError("No Digits Entered")
                elif not st.isdigit():
                    raise ValueError("Wrong Input! Only Digits Please!")
                x = int(st)
        except ValueError as v:
            print(v)
        except Exception as e:
            print(e)
        else:
            print(f"The Input Integer  is: {x}") 
            break 
            
get_integer()
        
