# ----------------- Unit 5: Classic Algorithms ------ #
# ---------------- Activity 5: Exercise Book ----------------- #
# write a program which will read students grades until negative 
# number is given and then it will show the three biggest grades it read

# Solution: First we read the grades and we store them in a list.
# Then, after we find the max grade, we place -1 in it's place so that 
# in the next loop, we find the second largest etc.
grade = int(input("Enter grade: "))
gradeList = []
while grade >= 0:
    gradeList.append(grade)
    grade = int(input("Enter grade: "))

maximum = [-1, -1, -1]
pos = -1 
for i in range(len(maximum)):
    for j in range(len(gradeList)):
        if gradeList[j] > maximum[i]:
            maximum[i] = gradeList[j]
            pos = j 
            
# Delete the value of maximum grade 
gradeList[pos] = -1 

print(maximum[0], maximum[1], maximum[2])
