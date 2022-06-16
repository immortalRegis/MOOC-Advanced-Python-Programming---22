# Write your solution here:
class Person:
    def __init__(self, name: str):
        self.name = name
        

    def return_first_name(self):
        split_name = self.name.split()
        return split_name[0]
    

    def return_last_name(self):
        split_name = self.name.split()
        return split_name[1]
        












