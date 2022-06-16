from unicodedata import name


class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"


def accepted(attempts: list):
    return list(filter(lambda cs: cs.grade >= 1, attempts))

def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda cs: cs.grade == grade, attempts))

def passed_students(attempts: list, course: str):
    holder = list(filter(lambda cs: cs.course_name == course and cs.grade > 0, attempts))
    return sorted(list(map(lambda cs: cs.student_name, holder)))


