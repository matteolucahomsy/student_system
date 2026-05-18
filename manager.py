import sqlite3
from student import Student
import os 
print(os.path.abspath("students.db"))

class StudentManager:
    def add_student(self,student):
        conn=sqlite3.connect("students.db")
        cursor=conn.cursor()

        cursor.execute("""
        INSERT INTO students(id,name,age,grade)
        VALUES (?,?,?,?)
        """,(
            student.student_id,
            student.name,
            student.age,
            student.grade
        ))
        conn.commit()
        conn.close()

        print("Student added seccessfully!")
    def display_students(self):
        conn=sqlite3.connect("students.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM students")
        students= cursor.fetchall()

        for s in students:
            print(s)
        conn.close()
