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
    def delete_student(self,student_id):
        conn=sqlite3.connect("students.db")
        cursor=conn.cursor()

        cursor.execute("DELETE FROM students WHERE id = ?",(student_id,))
        
        conn.commit()
        conn.close()

        print("Student deleted!")
    def update_grade(self,student_id,new_grade):
        conn=sqlite3.connect("students.db")
        cursor=conn.cursor()

        cursor.execute("""
        UPDATE  students
        SET grade = ?
        WHERE id = ?
        """,(new_grade,student_id))
        conn.commit()
        conn.close()

        print("Grade updated!")
    def search_student(self,student_id):
        conn=sqlite3.connect("students.db")
        cursor=conn.cursor()

        cursor.execute("SELECT * FROM students WHERE id = ?",(student_id,))
        student=cursor.fetchone()
        conn.close()

        print(student)
    def display_students(self):
        conn=sqlite3.connect("students.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM students")
        students= cursor.fetchall()

        for s in students:
            print(s)
        conn.close()
