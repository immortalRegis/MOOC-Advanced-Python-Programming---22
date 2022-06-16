# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date
def list_years(dates: list):
    new_dates = []
    # We add the for loop to copy a new list instead of making reference to the old ones
    for day in dates:
        new_dates.append(day.year)

    new_dates.sort()
    return new_dates