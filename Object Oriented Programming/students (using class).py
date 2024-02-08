class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"{self.name} is from {self.city}."

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
