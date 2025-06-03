# Написать программу для управления списком студентов, позволяющую добавлять, удалять и выводить список студентов.
students = []


def add_student():
    name = input("Add student: ")
    grade = input("Add grade: ")
    students.append({"name": name, "grade": grade})
    print(f"Student {name} added")


def remove_student():
    name = input("Enter student's name to remove: ")
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print(f"Student {name} removed")
            return
    print(f"Student not found.")


def show_students():
    if not students:
        print("No students added yet.")
    else:
        print("\nList of students: ")
        for student in students:
            print(f"Name: {student['name']}, Grade: {student['grade']}")


while True:
    print("\nMenu:")
    print("1. Add student")
    print("2. Remove student")
    print("3. Show students")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        remove_student()
    elif choice == 3:
        show_students()
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")