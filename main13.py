# Обработка данных о студентах

def students_count():
    num_students = int(input("Enter number of students: "))
    students = []
    for i in range(num_students):
        name = input("Enter student name: ")
        grade = int(input("Enter student grade: "))
        students.append({"name": name, "grade": grade})

    for student in students:
        print(student["name"], student["grade"])
    return students


def students_grades(students):
    if not students:
        print("No students")
        return

    total_grade = sum(student["grade"] for student in students)
    average = total_grade / len(students)
    max_grade = max(student["grade"] for student in students)
    top_student = [student["name"] for student in students if student["grade"] == max_grade]

    print(f"Average grade: {average}")
    print(f"Max grade student: {top_student} - {max_grade}")


students = students_count()  # Получаем список студентов
students_grades(students)    # Анализируем их оценки








