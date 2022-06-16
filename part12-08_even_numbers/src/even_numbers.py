# Write your solution here
def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1
    current_even_number = beginning
    while current_even_number <= maximum:
        yield current_even_number
        current_even_number += 2