from student import Student
from manager import StudentManager

manager=StudentManager()

while True:
    print("""
=========================
Student Management System
=========================
1. Add student 
2. Delete student
3. Search student
4. Update grade
5. Display students 
6. Class average
7. Best student
8. Ranking
9. Export CSV
10. Show graph
11. Exit
""")
    choice =input("Enter choice: ")
    if choice =="1":
        try:
            student_id=int(input("ID: "))
            name=input("Name: ")
            age=int(input("Age: "))
            grade=float(input("Grade: "))
        except ValueError:
            print("Invalid input!")
            continue
        student= Student(student_id,name,age,grade)
        manager.add_student(student)
    elif choice == "2":
        try:
            student_id =int(input("ID to delete: "))
        except ValueError:
            print("Invalid ID")
            continue
        manager.delete_student(student_id)
    elif choice == "3":
        try:
            student_id=int(input("ID: "))
        except ValueError:
            print("Invalid ID!")
            continue
        manager.search_student(student_id)
    elif choice == "4":
        try:
            student_id=int(input("ID: "))
            new_grade=float(input("New grade: "))
        except ValueError:
            print("Invalid Input!")
            continue
        manager.update_grade(student_id,new_grade)
    elif choice=="5":
        manager.display_students()
    elif choice == "6":
        manager.class_average()
    elif choice == "7":
        manager.best_student()
    elif choice == "8":
        manager.ranking()
    elif choice == "9":
        manager.export_csv()
    elif choice == "10":
        manager.plot_grades()
    elif choice == "11":
        print("BYE")
        break
    else:
        print("Invalid choice")
