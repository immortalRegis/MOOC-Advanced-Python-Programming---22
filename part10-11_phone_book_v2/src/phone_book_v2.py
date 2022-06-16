
# Tee ratkaisusi tähän:
class Person:
    def __init__(self, name: str):
        self.__name = name
        self.numbers = None
        self.address = None

    def name(self):
        return self.__name
    
    def numbers(self):
        return self.numbers
    
    def address(self):
        return self.address
    
    def add_number(self, number: str):
        self.numbers = number

    def add_address(self, address: str):
        self.address = address
    
    def __str__(self):
        return f"{self.__name}\n{self.address}\n{self.numbers}"
        

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons.keys():
            new_person = Person(name)
            self.__persons[name] = new_person
        self.__persons[name].add_number(number)
    
    def add_address(self, name: str, address: str):
        if not name in self.__persons.keys():
            new_person = Person(name)
            self.__persons[name] = new_person
        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        return self.__persons[name]


    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 add address")
    
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        searched_for = self.__phonebook.get_entry(name)
        
        print(searched_for)

          

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()



# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
