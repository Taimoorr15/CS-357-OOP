from student import Student
from student_list import StudentList


def main():
    print("---- Department of Computer Science (DCS) Student Management ----\n")

    # 1) DCS office creates an empty list of students
    dcs = StudentList()
    print("Step 1: Empty student list created.\n")

    # 2) Admit 3 students into the department
    s1 = Student("Ahmed", 20, "ahmed@example.com", "S001", "CS", "1001", ["Python"])
    s2 = Student("Ayesha", 19, "ayesha@example.com", "S002", "CS", "1002", ["Math"])
    s3 = Student("Bilal", 21, "bilal@example.com", "S003", "CS", "1003", ["Java"])

    dcs.add_student(s1)
    dcs.add_student(s2)
    dcs.add_student(s3)

    print("Step 2: Admitted 3 students: Ahmed, Ayesha, Bilal.\n")
    dcs.display_students()

    # 3) A new student joins in the middle of semester
    s4 = Student("Sara", 22, "sara@example.com", "S004", "CS", "1004", ["Databases"])
    dcs.add_student(s4)
    print("\nStep 3: Sara joined in the middle of the semester.\n")
    dcs.display_students()

    # 4) DCS office searches for student
    print("\nStep 4: Searching for students.\n")

    print("Search by seat number (1002):")
    student_found = dcs.find_student("1002")
    print(student_found if student_found else "Student not found.")

    print("\nSearch by name (Bilal):")
    student_found = dcs.find_student("Bilal")
    print(student_found if student_found else "Student not found.")

    # 5) Student updates record (name correction & course correction)
    print("\nStep 5: Updating student record for Ahmed...\n")
    s1.name = "Ahmad"
    s1.courses = ["Python", "Data Science"]
    dcs.display_students()

    # 6) A student leaves the department
    print("\nStep 6: Bilal leaves the department.\n")
    dcs.remove_student("S003")
    dcs.display_students()

    # 7) DCS checks the student list after removal
    print("\nStep 7: Final student list after removal check.\n")
    dcs.display_students()


if __name__ == "__main__":
    main()
