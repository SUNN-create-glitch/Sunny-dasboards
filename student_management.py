import json
import os

DATA_FILE = "students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    roll = input("Enter roll number: ").strip()
    if any(s["roll"] == roll for s in students):
        print("A student with this roll number already exists.")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()
    year = input("Enter year: ").strip()

    students.append({
        "roll": roll,
        "name": name,
        "course": course,
        "year": year
    })
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(
            f'Roll: {student["roll"]} | '
            f'Name: {student["name"]} | '
            f'Course: {student["course"]} | '
            f'Year: {student["year"]}'
        )


def search_student(students):
    roll = input("Enter roll number to search: ").strip()
    for student in students:
        if student["roll"] == roll:
            print("\nStudent found:")
            print(f'Roll: {student["roll"]}')
            print(f'Name: {student["name"]}')
            print(f'Course: {student["course"]}')
            print(f'Year: {student["year"]}')
            return
    print("Student not found.")


def update_student(students):
    roll = input("Enter roll number to update: ").strip()
    for student in students:
        if student["roll"] == roll:
            name = input(f'Name [{student["name"]}]: ').strip()
            course = input(f'Course [{student["course"]}]: ').strip()
            year = input(f'Year [{student["year"]}]: ').strip()

            if name:
                student["name"] = name
            if course:
                student["course"] = course
            if year:
                student["year"] = year

            save_students(students)
            print("Student information updated successfully.")
            return
    print("Student not found.")


def delete_student(students):
    roll = input("Enter roll number to delete: ").strip()
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully.")
            return
    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using Student Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
