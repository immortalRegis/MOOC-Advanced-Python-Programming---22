# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    holder = [person1, person2, person3]
    least_average = float(person1['result1'] + person1['result2'] + person1['result3'])/3
    least_person = person1
    for person in holder:
        current_average = (float(person['result1'] + person['result2'] + person['result3'])/3)
        if current_average < least_average:
            least_average = current_average
            least_person = person
    
    return least_person