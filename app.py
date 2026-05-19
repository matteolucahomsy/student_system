from flask import Flask, render_template, request , redirect
from manager import StudentManager
from student import Student

app=Flask(__name__)
manager = StudentManager()

@app.route("/")
def home():
    students=manager.get_all_students()
    return render_template("index.html", students=students)
@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        student_id =int (request.form.get("id"))
        name=request.form.get("name")
        age=int(request.form.get("age"))
        grade=float(request.form.get("grade"))

        student=Student(student_id,name,age,grade)
        manager.add_student(student)
        return redirect("/")
    return render_template("add.html")
@app.route("/delete/<int:student_id>")
def delete_student(student_id):
    manager.delete_student(student_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

