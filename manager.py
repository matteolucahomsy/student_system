import csv 
import matplotlib.pyplot as plt
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
    def class_average(self):
        conn=sqlite3.connect("students.db")
        cursor=conn.cursor()
        cursor.execute("SELECT AVG(grade) FROM students")
        avg=cursor.fetchone()[0]
        conn.close()
        print("Class average: ",avg)
    def best_student(self):
        conn=sqlite3.connect("students.db")
        cursor=conn.cursor()
        cursor.execute("SELECT MAX(grade) FROM students")
        max_grade=cursor.fetchone()[0]
        cursor.execute("SELECT * FROM students WHERE grade = ?", (max_grade,))
        students=cursor.fetchall()
        conn.close()
        print("Best students: ")
        for s in students:
            print(s)
    def ranking(self):
        conn=sqlite3.connect("students.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM students  ORDER BY grade DESC")
        data=cursor.fetchall()
        conn.close()
        last_grade=Nonerank=0
        real_rank=0
        for s in data:
            real_rank+=1
            if s[3]!= last_grade:
                rank= real_rank
                last_grade=s[3]
            print(f"{rank}. {s}")

    def export_csv(self):
        conn=sqlite3.connect("students.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM students")
        data=cursor.fetchall()
        conn.close()
        with open("students.csv","w",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(["ID","Name","Age", "grade"])
            writer.writerows(data)
        print("Export done!")
    def plot_grades(self):
        conn=sqlite3.connect("students.db")
        cursor=conn.cursor()
        cursor.execute("SELECT name, grade FROM students")
        data=cursor.fetchall()
        conn.close()
        if not data:
            print("No students found")
            return
        names=[x[0] for x in data]
        grades=[x[1] for x in data]
        plt.bar(names, grades)
        plt.title("Student Grades")
        plt.show()
    def display_students(self):
        conn=sqlite3.connect("students.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM students")
        students= cursor.fetchall()
        for s in students:
            print(s)
        conn.close()
