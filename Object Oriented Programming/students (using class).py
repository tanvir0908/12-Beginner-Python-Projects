class Student:
    def __init__(self, name, city, country):
        if not name:
            raise ValueError("Missing name")
        if city not in ["Dhaka", "London", "Toronto", "Delhi", "Tokyo"]:
            raise ValueError("Invalid city")
        self.name = name
        self.city = city
        self.country = country

    def getCountry(self):
        match self.country:
            case "Bangladesh":
                return "🍕"
            case "India":
                return "🍔"
            case "England":
                return "🌭"
            case _:
                return "🍿"

    def __str__(self):
        return f"{self.name} is from {self.city} which is a city of {self.country}"


def getStudent():
    name = input("Enter your name: ")
    city = input("Enter your hometown: ")
    country = input("Enter your country: ")
    return Student(name, city, country)


def main():
    student = getStudent()
    # print(f"{student.name} is from {student.city}")
    # print(student)
    print("Country emoji:", student.getCountry())


if __name__ == "__main__":
    main()
