with open("students.txt","r")as myfile:
    student = myfile.readlines()
with open("courses.txt","r")as myfile:
    courses = myfile.readlines()
with open("grades.txt","r")as myfile:
    grades = myfile.readlines()
student = [values.strip() for values in student[1:]]
courses = [values.strip() for values in courses[1:]]
grades = [values.strip() for values in grades[1:]]

total_courses = 0
average = 0
mo = 0
outfile = open('results.txt','w')
outfile.write('FullName-TotalCourses-Courses-Average \n') 
course = []
for row in student:
    student = row.split('-')
    student_id = student[0]
    student_name = student[1]
    student_surname = student[2]
    for grades_row in grades:
        grade = grades_row.split('-')
        if grade[0] == student_id:
            total_courses += 1
            average += float(grade[2])
            for course_row in courses:
                mathima = course_row.split('-')
                if grade[1] == mathima[0]:
                    course.append(mathima[1])
                    
                    
                    
    student_full_name = student_name + ' ' + student_surname
    import math
    mo = math.ceil(float(average) / float(total_courses))

    outfile.write(student_full_name + '-' + str(total_courses) + '-')
    for i in course:
        outfile.write(i + ' ')
    outfile.seek(outfile.tell()-1)
    outfile.write('-' + str(mo) + '\n')
    total_courses = 0
    average = 0
    course = []
    mo = 0
                 
outfile.close()
