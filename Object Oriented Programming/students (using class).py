class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"{self.name} is from {self.city}."

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if city not in ["Dhaka", "London", "Toronto", "Delhi", "Tokyo"]:
            raise ValueError("Invalid city")
        self._city = city


def getStudent():
    name = input("Enter your name: ").title()
    city = input("Enter your hometown: ").title()
    return Student(name, city)


def main():
    student = getStudent()
    # print(f"{student.name} is from {student.city}")
    print(student)


if __name__ == "__main__":
    main()
