def safe_divide():
    try:
        nom = int(input("Enter the nominator: "))
        denom = int(input("Enter the denominator: "))
        res = nom/denom
    except ZeroDivisionError:
        print("Error! Denominator is 0")
    except Exception as e:
        print("Something Went Really Wrong: " + str(e))
    else:
        return res 
    finally:
        return None 
        
print(safe_divide())
