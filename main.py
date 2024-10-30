#1
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew {amount}. New balance: {self.balance}")

account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
#2
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"[{self.year}] {self.make} {self.model}"

car = Car("Tesla", "Cibertrack", 2021)
print(car.get_info())
#3
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary}"

employee = Employee("Ольга", "Менеджер", 50000)
print(employee.get_salary_info())
#4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 10)
print("Площа:", rectangle.calculate_area())
print("Периметр:", rectangle.calculate_perimeter())
#5
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Назва товару: {self.name}")
        print(f"Ціна за одиницю: {self.price}")
        print(f"Кількість: {self.quantity}")
        print(f"Загальна вартість: {self.calculate_total_price()}")

product = Product("PlayStation 5", 45000, 100)
product.display_info()
