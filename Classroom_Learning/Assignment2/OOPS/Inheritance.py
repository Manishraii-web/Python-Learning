class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee: {self.name}")
        print(f"Salary: Rs.{self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def total_salary(self):
        return self.salary + self.bonus


manager = Manager("Ram", 50000, 10000)

manager.show_details()
print("Total Salary:", manager.total_salary())