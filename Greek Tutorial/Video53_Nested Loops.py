#1_first_way
my_set = set()
for i in range(2):
    for j in range(3):
        my_set.add((i,j))
        
#1_another_way
my_set1 = {(i,j) for i in range(2) for j in range(3)}


#2_first_way
my_set2 = set()
for i in range(6):
    if i%2==0:
        for j in range(6,10):
            if j%2==1:
                my_set2.add((i,j))

#2_another_way
my_set3 = {(i,j) for i in range(6) if i%2==0 for j in range(6,10) if j%2==1}
