class Employee:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("Age:", self.age)
        print("*" * 15)

employee1 = Employee("Anna", "Gurbanov", 33)
employee2 = Employee("Ata", "Geldiyev", 29)

employee1.show_info()
employee2.show_info()