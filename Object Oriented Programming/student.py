def getStudent():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return {"name": name, "house": house}


def main():
    student = getStudent()
    print(f"{student['name']} is from {student['house']}")


if __name__ == "__main__":
    main()
