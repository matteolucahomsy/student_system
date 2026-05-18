from student import Student
from manager import StudentManager

manager=StudentManager()

while True:
    print("""
1. Add student 
2. Delete student
3. Search student
4. Update grade
5. Display students 
6. Exit
""")
    choice =input("Enter choice: ")
    if choice =="1":
        student_id=int(input("ID: "))
        name=input("Name: ")
        age=int(input("Age: "))
        grade=float(input("Grade: "))

        student= Student(student_id,name,age,grade)
        manager.add_student(student)
    elif choice == "2":
        student_id =int(input("ID to delte: "))
        manager.delete_student(student_id)
    elif choice == "3":
        student_id=int(input("ID: "))
        manager.search_student(student_id)
    elif choice == "4":
        student_id=int(input("ID: "))
        new_grade=float(input("New grade: "))
        manager.update_grade(student_id,new_grade)
    elif choice=="5":
        manager.display_students()
    elif choice == "6":
        break
    else:
        print("Invalid choice")
