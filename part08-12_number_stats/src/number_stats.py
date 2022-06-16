# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0

    def add_number(self, number:int):
        self.numbers += 1
        self.sum += number

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return self.sum

    def average(self):
        if self.numbers > 0:
            return float(self.sum)/self.numbers
        return 0.0



holder = NumberStats()
odd_holder = NumberStats()
even_holder = NumberStats()

print("Please type in an integer")
while(True):
    value = int(input(""))
    if value == -1:
        break
    if value % 2 == 0:
        even_holder.add_number(value)
    else:
        odd_holder.add_number(value)

    holder.add_number(value)

print(f"Sum of numbers: {holder.get_sum()}")
print(f"Mean of numbers: {holder.average()}")
print(f"Sum of even numbers: {even_holder.get_sum()}")
print(f"Sum of odd numbers: {odd_holder.get_sum()}")
