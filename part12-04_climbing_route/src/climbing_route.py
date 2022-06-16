class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:
def sort_by_length(routes: list):
    def order_by_length(route):
        return route.length

    new_list = routes.copy()
    return sorted(new_list, key=order_by_length, reverse=True)



def sort_by_difficulty(routes: list):
    def order_by_difficulty(route):
        return route.grade
    
    
    new_list = sort_by_length(routes)
    new_list.sort(key=order_by_difficulty, reverse=True)
    return new_list
        

