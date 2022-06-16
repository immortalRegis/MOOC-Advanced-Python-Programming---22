# Write your solution here
import re

def is_dotw(my_string: str):
    rule =  'sun|mon|tue|wed|thu|fri|sat'
    if re.search(rule , my_string.lower()):
        return True
    return False

def all_vowels(my_string: str):
    rule = '^[aeiouy]*$'
    if re.search(rule, my_string.lower()):
        return True
    return False


def time_of_day(my_string: str):
    rule = '([01][0-9]|[2][0-3]):[0-5][0-9]:[0-5][0-9]'
    if re.match(rule, my_string):
        return True
    return False


