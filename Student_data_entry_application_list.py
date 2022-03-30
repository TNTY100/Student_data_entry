print("Welcome to the student data entry application.")

number_of_grade = int(input("How many grades will be entered for each student? : "))

print("  Ok! Let's get started...")

is_entering_student = True

students_list = []


index_students = 0

while is_entering_student:
    index_students += 1
    print(f"\nEntering data for student # {index_students}:")

    student_entry = {
        "name": str(input("Student's name: ")),
        "ID":   int(input("Student's ID number: "))  # Maybe str ???
    }
    grades = []
    for grade_index in range(number_of_grade):
        grades.append(int(input(f"Enter grade #{grade_index+1}: ")))

    student_entry["Grades"] = list(grades)

    students_list.append(student_entry.copy())
    
    another_one = input("Should we add another student? (y/n): ")

    if another_one == "n":
        is_entering_student = False


print("\n --- Input Completed --- \n")
print("Here is a review of the student data...")

for student_index in range(len(students_list)):
    print(f"\tStudent #{student_index + 1}:")

    for info_index in students_list[student_index]:
        print(f"\t\t{info_index}: {students_list[student_index][info_index]}")
    
print("\n --- End Of Program --- \n")
