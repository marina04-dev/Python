# ----------------- Unit 5: Classic Algorithms ------ #
# ---------------- Activity 8: Exercise Book ----------------- #
# write a program which will read students grades and their surnames
# and then it will return the students in descending order based on their 
# grades 

N = int(input("Enter the number of students: "))
gradeList = []
surnameList = []

for i in range(N):
    surname = input("Enter student's surname: ")
    grade = int(input("Enter student's grade: "))
    surnameList.append(surname)
    gradeList.append(grade)
    
for i in range(N):
    for j in range(N-1, i, -1):
        if gradeList[j] > gradeList[j-1]:
            gradeList[j], gradeList[j-1] = gradeList[j-1], gradeList[j]
            surnameList[j], surnameList[j-1] = surnameList[j-1], surnameList[j]
    
for i in range(N):
    print(surnameList[i])
    

