from person import Person

class Teacher(Person):
    def __init__(self, name: str, age: int, email: str, teacher_id: str, department: str, courses: list):
        super().__init__(name, age, email)
        self._teacher_id = teacher_id
        self._department = department
        self._courses = courses  # list of course names or Course objects

    def is_teaching(self):
        if self._courses:
            return f"{self._name} is teaching: {', '.join(self._courses)}"
        return f"{self._name} is currently not assigned any courses."

    def __str__(self):
        return (f"{self._name}, age {self._age}, email: {self._email}, "
                f"Teacher ID: {self._teacher_id}, Department: {self._department}, "
                f"Courses: {', '.join(self._courses)}")