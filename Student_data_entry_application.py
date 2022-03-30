print("Welcome to the student data entry application.")

number_of_grade = int(input("How many grades will be entered for each student? : "))

print("  Ok! Let's get started...")

is_entering_student = True

students_dic = dict()


index_students = 0

while is_entering_student:
    index_students += 1
    print(f"\nEntering data for student # {index_students}:")

    student_entry = {
        "name": str(input("Student's name: ")),
        "ID":   str(input("Student's ID number: "))
    }
    grades = []
    for grade_index in range(number_of_grade):
        grades.append(int(input(f"Enter grade #{grade_index+1}: ")))

    student_entry["Grades"] = list(grades)

    print(student_entry)

    students_dic["Student #"+str(index_students)] = student_entry.copy()
    
    another_one = input("Should we add another student? (y/n): ")

    if another_one == "n":
        is_entering_student = False


print("\n --- Input Completed --- \n")
print("Here is a review of the student data...")

for student_index in students_dic:
    print(f"\t{student_index}:")

    for info_index in students_dic[student_index]:
        print(f"\t\t{info_index}: {students_dic[student_index][info_index]}")
    
print("\n --- End Of Program --- \n")
