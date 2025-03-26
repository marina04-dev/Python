"""Exercise 3: Print characters present at an even index number"""
"""Write a Python code to accept a string from the user and display characters present at an even index number."""
st = input("Enter a string: ")
print(f"Original String is {st}")
print("Printing only even index chars")
for letter in range(1,len(st),2):
    print(st[letter])
