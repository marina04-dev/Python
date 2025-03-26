# Biggest of the 3 - list version
# This is a program that takes 3 numbers as inputs and appends the numbers if they are digits on the list
# Then it checks which number is bigger and prints the result
# exercise 7 (Lists)
a = input("Give the first number: ").strip()
b = input("Give the second number: ").strip()
c = input("Give the third number: ").strip()
new_list = []
if a.isdigit() and b.isdigit() and c.isdigit():
    new_a = float(a)
    new_list.append(new_a)
    new_b = float(b)
    new_list.append(new_b)
    new_c = float(c)
    new_list.append(new_c)
    if new_a>new_b and new_a>new_c:
        print("A: " + str(new_a) + " is the biggest")
    if new_b>new_a and new_b>new_c:
        print("B: " + str(new_b) + " is the biggest")
    if new_c>new_b and new_c>new_a:
        print("C: " + str(new_c) + " is the biggest")
    if new_c==new_b and new_c>new_a:
        print("C: " + str(new_c) + " and B: " + str(new_b) + " are equal and bigger than A: " + str(new_a))
    if new_c==new_a and new_c>new_b:
        print("C: " + str(new_c) + " and A: " + str(new_a) + " are equal and bigger than B: " + str(new_b))
    if new_b==new_a and new_b>new_c:
        print("A: " + str(new_a) + " and B: " + str(new_b) + " are equal and bigger than C: " + str(new_c))
    if new_b==new_a and new_a==new_c and new_c==new_b:
        print("All numbers are equal")
else:
    print("Wrong input! Please enter only digits!")
    
