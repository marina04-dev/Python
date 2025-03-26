"""Exercise 5: Check if the first and last numbers of a list are the same"""
"""Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False."""
def same(nums):
    if nums[0]==(nums[len(nums)-1]):
        return True
    else:
        return False
        
        
n = [1,2,3,4,5,6,7,1]
print(same(n))
