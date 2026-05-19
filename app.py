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
        try:
            student_id =int (request.form.get("id"))
            name=request.form.get("name")
            age=int(request.form.get("age"))
            if age <=0:
                return "Age must be positive"
            grade=float(request.form.get("grade"))
            if grade<0 or grade>20:
                return "Grade must be between 0 and 20"
            student=Student(student_id,name,age,grade)
            manager.add_student(student)
            return redirect("/")
        except ValueError:
            return "Invalid input"
    return render_template("add.html")
@app.route("/delete/<int:student_id>")
def delete_student(student_id):
    manager.delete_student(student_id)
    return redirect("/")
@app.route("/update/<int:student_id>",methods=["GET", "POST"])
def update_student(student_id):
    if request.method=="POST":
        new_grade=float(request.form.get("grade"))
        if new_grade<0 or new_grade>20:
            return "New grade must be between 0 and 20"
        manager.update_grade(student_id, new_grade)
        return redirect("/")
    return render_template("update.html", student_id=student_id)



if __name__ == "__main__":
    app.run(debug=True)

