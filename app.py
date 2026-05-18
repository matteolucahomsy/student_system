from flask import Flask, render_template, request , redirect
from manager import StudentManager
from student import Student

app=Flask(__name__)
manager = StudentManager()

@app.route("/")
def home():
    students=manager.get_all_students()
    return render_template("index.html", students=students)
if __name__ == "__main__":
    app.run(debug=True)