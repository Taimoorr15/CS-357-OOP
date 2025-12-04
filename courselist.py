from course import Course

class CourseList:
    def __init__(self):
        self._courses = []

    def add_course(self, course: Course):
        self._courses += [course]

    def remove_course(self, course_code: str):
        self._courses = [c for c in self._courses if c._course_code != course_code]

    def find_course(self, course_code: str):
        for course in self._courses:
            if course._course_code == course_code:
                return course
        return None

    def display_courses(self):
        if not self._courses:
            print("No courses available.")
        else:
            for course in self._courses:
                print(course)

    def __len__(self):
        return len(self._courses)
