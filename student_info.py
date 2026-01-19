def student_info():
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    school = input("Enter your school name:")

    subjects = []
    subjects.append(input("Enter your first subject:"))
    subjects.append(input("Enter your second subject:"))
    subjects.append(input("Enter your third subject:"))

    print("------student info------")
    print("Name:" , name)
    print("Age:" , age)
    print("School:", school)
    print("Subjects:", ",".join(subjects))

    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")

student_info()
