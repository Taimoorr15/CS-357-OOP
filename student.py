from person import Person

class Student(Person):
    def __init__(self, name: str, age: int, email: str, student_id: str, major: str, seat_number: str, courses: list):
        super().__init__(name, age, email)
        self._student_id = student_id
        self._major = major
        self._seat_number = seat_number
        self._courses = courses  # list of course names or Course objects

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, other: str):
        self._student_id = other

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, other: str):  
        self._major = other

    @property
    def seat_number(self):
        return self._seat_number

    @seat_number.setter
    def seat_number(self, other: str):
        self._seat_number = other

    @property
    def courses(self):
        return self._courses  

    @courses.setter
    def courses(self, other: list):  # expects a list
        self._courses = other  

    def __str__(self):
        courses_str = ", ".join(self._courses) if self._courses else "No courses enrolled"
        return (f"{self._name} (Student ID: {self._student_id}, Seat No: {self._seat_number}) "
                f"is majoring in {self._major}. Email: {self._email}. "
                f"Enrolled in courses: {courses_str}")
