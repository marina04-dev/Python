# ---------------- UNIT 5: Classic Algorithms ---------------------- #
# ---------------- Activity 2 ---------------------- #
# selection sort ascending
def find_min_position(start, end, iterable):
    position = start
    for i in range(start, end):
        if iterable[i] > iterable[position]:
            position = i
    return position

def selection_sort_ascending(iterable):
    position = None
    n = len(iterable)
    for i in range(0,n):
        position = find_min_position(i,n,iterable)
        iterable[i], iterable[position] = iterable[position], iterable[i]
    return iterable
