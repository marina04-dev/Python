filename = "file.txt"
try:
    with open("file.txt") as f:
        st = f.read()
except FileNotFoundError:
    print(f"The File {filename} Does Not Exist")
    choice = input("Would you like to create the file? (Yes/No): ").lower()
    if choice == "yes":
        with open(filename, "w") as f:
            pass
    else:
        print("Exit")
        break 
