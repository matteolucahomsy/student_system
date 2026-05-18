# 🎓 Student Management System

A full-stack Python project using Flask, SQLite and Matplotlib.

---

## 🚀 Features

### Terminal version (Level 3)
- Add student
- Delete student
- Update grade
- Search student
- Display students
- Ranking system
- Class average
- Export CSV
- Data visualization (Matplotlib)

---

### Web version (Level 4)
- Flask web server
- Add student via web form
- Display students in browser
- SQLite database integration
- Dynamic routing

---

## 🛠️ Tech Stack

- Python
- Flask
- SQLite
- Matplotlib
- CSV module
- HTML/CSS

---

## ▶️ How to run

### Terminal version:
```bash
python main.py
```

---
### Web version:
```bash
python app.py

THEN open:
http://127.0.0.1:5000
```



📁 Project Structure

student_system/
│
├── app.py              # Flask web application
├── main.py             # Terminal version (CLI)
├── manager.py          # Database logic (CRUD operations)
├── student.py          # Student class model
├── students.db        # SQLite database
│
├── templates/         # HTML pages (Flask)
│   ├── index.html     # Student list page
│   └── add.html       # Add student form
│
└── static/            # Static files (CSS/JS optional)
    └── style.css