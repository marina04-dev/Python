"""Exercise 10: Merge two lists using the following condition"""
"""Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list"""
def merge_con(list1, list2):
    new_list = []
    for i in range(0,len(list1)-1):
        if list1[i]%2==0:
            new_list.append(list1[i])
        else:
            continue
    
    for i in range(0,len(list2)-1):
        if list2[i]%2!=0:
            new_list.append(list2[i])
        else:
            continue
        
    return new_list
    
my_list = [2,4,6,8,7,5,4,3,2,12,23]
my_new_list = [32,33,45,65,78,65,31]
print(f"1st list: {my_list}")
print(f"\n2nd list: {my_new_list}\n")
print(merge_con(my_list,my_new_list))
    
