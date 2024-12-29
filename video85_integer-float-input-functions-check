#exercise_3 : integer-input check
def input_integer():
    while True:
        data = input("Please enter an integer number: ").strip()
        if data.isdigit():
            return int(data)
        else:
            print("Only digits please!")
            
print(input_integer())
        
        
#exercise_4 : float-input check
def input_float():
    while True:
        data = input("Please enter a float number: ").strip()
        if "." in data:
            parts = data.split(".")
            if len(parts)>2:
                print("Please enter only one dot please!")
            elif parts[0].isdigit() and parts[1].isdigit():
                return float(data)
            else:
                print("Only digits please!")
        else:
            if data.isdigit():
                return float(data)
            else:
                print("Only digits please!")
            
print(input_float())
