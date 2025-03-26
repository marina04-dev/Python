# Dynamic tuple constructing
# Lesson 6: Exercise 1
my_list = []
n=0
while (n<5):
    num = input("Enter an integer number between 10 and 20: ").strip()
    if num.isdigit():
        number = int(num)
        if (number<10 or number>20):
            print("Wrong input!")
            continue
        elif (number>=10 and number<=20):
            my_list.append(number)
            n+=1 
    else:
        print("Enter only digits please!")
        continue
        
        
        
my_tuple = tuple(my_list)
print(my_list)
print(my_tuple)
my_new_list = []
for i in range(len(my_list)):
    x = (my_list[i])**2 
    my_new_list.append(x)
    
my_new_tuple = tuple(my_new_list)
print(my_new_list)
print(my_new_tuple)
        
