# 👨‍💼 Employee Management System – Django API Integration

## 🚀 Project Overview

The **Employee Management System** is a web-based application developed using **Django** that allows organizations to efficiently manage employee records with authentication support and API-based data handling.

This project demonstrates:

* Employee data management
* User Authentication (Login & Registration)
* CRUD Operations
* Django Backend Integration
* API-based system architecture

The system enables authenticated users to securely manage employee information through an organized dashboard.

---

## 🛠️ Technologies Used

* Python 3.x
* Django Framework
* Django Templates
* SQLite Database
* HTML, CSS
* Django Authentication System
* REST/API Integration Concepts

---

## 📂 Full Project Structure

```
Employee-Management-System-API-Integration-Django/
│
├── Employee_Details-Using-Django/
│   │
│   ├── Employee_Details/          # Main Project Configuration
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── authentication/            # Authentication App
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── templates/
│   │   │   └── authentication/
│   │   │       ├── login.html
│   │   │       └── register.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   │
│   ├── employee/                  # Employee Management App
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── templates/
│   │   │   └── employee/
│   │   │       ├── employee_list.html
│   │   │       ├── add_employee.html
│   │   │       ├── update_employee.html
│   │   │       └── delete_employee.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   │
│   ├── db.sqlite3                 # Database File
│   ├── manage.py                  # Django Management Script
│   │
│   └── static/                    # Static Files (CSS / JS / Images)
│       ├── css/
│       ├── js/
│       └── images/
│
├── venv/                          # Virtual Environment (Ignored)
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ✨ Features

- ✅ User Registration 
- ✅ Secure Login & Logout 
- ✅ Employee Record Management 
- ✅ Add Employee 
- ✅ Update Employee Details 
- ✅ Delete Employee 
- ✅ View Employee List 
- ✅ Authentication-Based Access 
- ✅ Clean MVC Architecture 

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Shivamdhole99/Employee-Management-System-API-Integration-Django.git
cd Employee-Management-System-API-Integration-Django
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install django
```

---

### 4️⃣ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run Development Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication Module

The project includes an authentication system:

* User Registration
* Login System
* Logout Functionality
* Protected Employee Pages

Only authenticated users can manage employee records.

---

## 👨‍💻 Employee Module

Employees can be managed with full CRUD operations:

| Operation | Description             |
| --------- | ----------------------- |
| Create    | Add new employee        |
| Read      | View employee list      |
| Update    | Modify employee details |
| Delete    | Remove employee         |

---

## 🧪 Application Usage Flow

1. Register a new user account
2. Login using credentials
3. Access Employee Dashboard
4. Perform CRUD operations

---

## 📸 Key Learning Outcomes

* Django Project Structure
* Authentication Implementation
* Model–View–Template Architecture
* Database Handling
* API Integration Concepts
* Backend Development Best Practices

---

## 👨‍🎓 Author

**Shivam Dhole**

B.Tech. Artificial Intelligence & Machine Learning

Aspiring Backend & Python Developer

🔗 GitHub: https://github.com/Shivamdhole99 

🔗 LinkedIn: https://www.linkedin.com/in/shivam-dhole-468a232b5/

---

## 📄 License

This project is developed for **educational and learning purposes**.

---

⭐ If you like this project, consider giving it a star on GitHub!
