"""Exercise 6: Display numbers divisible by 5"""
"""Write a Python code to display numbers from a list divisible by 5"""
def divFive(nums):
    new_list = []
    for num in range(len(nums)):
        if (nums[num])%5==0:
            new_list.append(nums[num])
        else:
            continue
    return new_list
        
        
n = [20,30,40,35,55,34]
print(divFive(n))
        
