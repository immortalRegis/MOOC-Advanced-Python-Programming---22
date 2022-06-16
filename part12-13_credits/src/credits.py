from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(courses: list):

    def credit_sum_helper(total_credits, course):
        return total_credits + course.credits
    
    return reduce(credit_sum_helper, courses, 0)

def sum_of_passed_credits(courses: list):
    def credit_sum_helper(total_credits, course):
        return total_credits + course.credits
    
    passed_list = list(filter(lambda cs: cs.grade > 0, courses))
    return reduce(credit_sum_helper, passed_list, 0)


def average(courses: list):
    def credit_sum_helper(total_credits, course):
        return total_credits + course.grade
    
    passed_list = list(filter(lambda cs: cs.grade > 0, courses))
    return (float)(reduce(credit_sum_helper, passed_list, 0)/len(passed_list))