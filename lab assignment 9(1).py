class Employee:
    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def show_data(self):
        print(self.name, self.age, self.salary, self.address)


class Manager(Employee):
    pass


managers = []

for i in range(10):
    m = Manager()
    m.get_data()
    managers.append(m)

for m in managers:
    m.show_data()
