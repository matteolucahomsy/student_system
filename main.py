from student import Student
from manager import StudentManager

manager=StudentManager()

while True:
    print("""
1. Add student 
2. Display students 
3. Exit
""")
    choice =input("Enter choice: ")
    if choice =="1":
        student_id=int(input("ID: "))
        name=input("Name: ")
        age=int(input("Age: "))
        grade=float(input("Grade: "))

        student= Student(student_id,name,age,grade)
        manager.add_student(student)
    elif choice=="2":
        manager.display_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
