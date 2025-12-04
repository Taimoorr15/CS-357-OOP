from student_list import StudentList
from student import Student

class Course:
    def __init__(self, course_code: str, course_name: str, course_teacher: str, enrolled_students: StudentList):
        self._course_code = course_code
        self._course_name = course_name
        self._course_teacher = course_teacher
        self._enrolled_students = enrolled_students  
  

    def enroll_student(self, student: Student):
        self._enrolled_students.add_student(student)

    def remove_student(self, student_id: str):
        self._enrolled_students.remove_student(student_id)

    def find_student(self, student_id: str):
        return self._enrolled_students.find_student(student_id)

    def display_students(self):
        self._enrolled_students.display_students()

    def __str__(self):
        return (f"Course: {self._course_name} ({self._course_code}), "
                f"Taught by: {self._course_teacher}, "
                f"Enrolled Students: {len(self._enrolled_students._students)}")