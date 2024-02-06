class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Natore", "Dhaka"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def getStudent():
    name = input("Enter your name: ")
    house = input("Enter your hometown: ")
    return Student(name, house)


def main():
    student = getStudent()
    print(f"{student.name} is from {student.house}")


if __name__ == "__main__":
    main()
