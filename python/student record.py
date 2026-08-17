


def add_menu():
    choice=input("welcome! please enter 1 to view, 2 to add new student detail")
    if choice =="1":
        with open("student.txt", "r") as file:
            print(file.read())
    elif choice =="2":
        add_menu()
    else:
        print("wrong input!")

    add_students()

    con=input("do you want to enter another details enter Y or N").lower()
    if con== "y":
        add_students()
    elif con=="n":
        exit()
    else:
        print("WRONG INPUT!")




def add_students(*kwargs,):
    name= input("Enter the name of the student")
    department= input("Enter the department of the student")
    level= input("Enter the level of the student")
    with open("student.txt", "a") as file:
        file.write(name,department,level)
    




