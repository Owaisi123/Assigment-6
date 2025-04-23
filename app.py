# 1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Owais", 90)
s1.display()


# 2. Using cls
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Objects created:", cls.count)

c1 = Counter()
c2 = Counter()
Counter.show_count()


# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand + " car started.")

car = Car("Honda")
print(car.brand)
car.start()


# 4. Class Variables and Methods
class Bank:
    bank_name = "Old Bank"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

Bank.change_bank_name("New Bank")
print(Bank.bank_name)


# 5. Static Variables and Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 3))


# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger created")

    def __del__(self):
        print("Logger destroyed")

log = Logger()
del log


# 7. Access Modifiers
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # public
        self._salary = salary   # protected
        self.__ssn = ssn        # private

emp = Employee("Owais", 50000, "123-45-6789")
print(emp.name)
print(emp._salary)
print(emp._Employee__ssn)  # Access private with name mangling


# 8. super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Owais", "Math")
print(t.name)
print(t.subject)


# 9. Abstract Classes
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r = Rectangle(5, 4)
print(r.area())


# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name + " is barking!")

dog1 = Dog("Rocky", "Bulldog")
dog1.bark()


# 11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def add_book(cls):
        cls.total_books += 1

Book.add_book()
Book.add_book()
print(Book.total_books)


# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def c_to_f(celsius):
        return (celsius * 9/5) + 32

print(TemperatureConverter.c_to_f(25))


# 13. Composition
class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

e = Engine()
my_car = Car(e)
my_car.start_car()


# 14. Aggregation
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

emp1 = Employee("Owais")
dept = Department("IT", emp1)
print(dept.employee.name)


# 15. MRO and Diamond Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()


# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()


# 17. Class Decorators
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Owais")
print(p.greet())


# 18. @property, @setter, @deleter
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

item = Product(100)
print(item.price)
item.price = 200
print(item.price)
del item.price


# 19. __call__()
class Multiplier:
    def __init__(self, number):
        self.number = number

    def __call__(self, value):
        return self.number * value

m = Multiplier(3)
print(callable(m))
print(m(10))


# 20. Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        print("Valid age.")

try:
    check_age(15)
except InvalidAgeError as e:
    print(e)


# 21. Custom Iterable
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        value = self.start
        self.start -= 1
        return value

for number in Countdown(5):
    print(number)
