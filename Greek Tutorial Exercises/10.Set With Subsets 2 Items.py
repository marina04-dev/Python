# Set with All Subsets With 2 Items of {1,2,...N}
# Lesson 10: Exercise 1
subsets = set()
N = 4
for i in range(1,N+1):
    for j in range(i+1,N+1):
        subsets.add(frozenset({i,j}))
    
print(subsets)


# Set With all Subsets of {1,2,...N}
# Lesson 10: Exercise 2
N = 10

subsets = set()
subsets.add(frozenset())

for i in range(1,N+1):
    new_subsets = set()
    for subset in subsets:
        nonfz = set(subset)
        nonfz.add(i)
        fz = frozenset(nonfz)
        new_subsets.add(fz)
    subsets.update(new_subsets)

print(subsets)
print(len(subsets))
