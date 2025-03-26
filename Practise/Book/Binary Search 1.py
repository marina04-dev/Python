# Binary Search Algorithm without found position
def binarySearch(array, key):
    first = 0
    last = len(array - 1)
    found = False
    while first <= last and not found:
        mid = (first + last)/2
        if array[mid] == key:
            found = True
        elif array[mid] < key:
            first = mid + 1 
        else:
            last = mid -1 
    return found
