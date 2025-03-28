data={}
backwards=[]
Nbackwards=[]
while True:
    value = input("Give me a word bigger than 3 letter or 'stop' to exit: ")
    if value == "stop":
        print("Words given that can be read the same backwards: ")
        for key,price in data.items():
            if price == 'Yes':
                backwards.append(key)
                backwards.sort()
        for word in backwards:
            print (word)
        print("Words given that cannot be read the same backwards: ")
        for key,price in data.items():
            if price == "No":
                Nbackwards.append(key)
                Nbackwards.sort()
        for word in Nbackwards:
            print (word)
        break

    if len(value) > 3 :
        value = value.upper()
        forImport = {value:"Yes"} if value == value[::-1] else {value:"No"}
        data.update(forImport)
    else:
        print("You must give a word bigger than 3 letters...")
        continue
    
