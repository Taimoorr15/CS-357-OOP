from student import Student

class StudentList:
    def __init__(self):
        self._students = []  # holds multiple Student objects

    def add_student(self, student: Student):
        # Instead of append, we can do list concatenation
        self._students = self._students + [student]

    def remove_student(self, student_id: str):
        # Create a new list without the matching student
        self._students = [s for s in self._students if s.student_id != student_id]

    def find_student(self, student_id: str):
        for student in self._students:
            if student.student_id == student_id:
                return student
        return None  # if not found

    def display_students(self):
        if not self._students:
            print("No students in the list.")
        else:
            for student in self._students:
                print(student)

    def __str__(self):
        return f"Total students: {len(self._students)}"
