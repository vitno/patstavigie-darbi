class Student:

    def __init__(self, name):
        self.name = name


names = ("Alex", "Carl", "Hannah")

students = [Student(name) for name in names]