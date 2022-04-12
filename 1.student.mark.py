#input number of student in class
NumberOfStudent = int(input("number of student in the class is: \n"))
#input student information : id,name,DoB
student_list = list()
for i in range (0,NumberOfStudent):
    student = {}
    S_id = input(f"Id of student {i+1} is :\n")
    S_name = input(f"Name of student {i+1} is :\n")
    S_DoB = input(f"Student DoB {i+1} is :\n")
    student["id"] = S_id
    student["name"] = S_name
    student["DoB"] = S_DoB
    student_list.append(student)
print(student_list)
#input number of courses
NumberOfCourses = int(input("number of courses is: \n"))
#input courses information : id, name
courses_list = list()
for i in range (0,NumberOfCourses):
    course = {}
    C_id = input(f"id of the course {i+1} is :\n")
    C_name = input(f"name of the course {i+1} is :\n")
    course["id"] = C_id
    course["name"] = C_name
    courses_list.append(course)
print(courses_list)
#Show student marks for a given course
for i in range (0,NumberOfCourses):
	for j in range (0,NumberOfStudent):
		mark = input(f"mark of student {j + 1} in course {i +1} is:\n")
		student_list[j][f"mark{i+1}"] = mark
print(student_list) 