# 🎓 Smart Campus Helpdesk API

![Django](https://img.shields.io/badge/Django-Framework-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![DRF](https://img.shields.io/badge/DRF-API-red)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

A **Django REST Framework** based backend API for managing campus
helpdesk tickets.\
This system allows users to create, view, and manage support tickets
efficiently.

------------------------------------------------------------------------

## 🚀 Features

-   ✅ Create a new helpdesk ticket\
-   📋 View all tickets\
-   🔍 View ticket by ID\
-   🛠 Admin panel support\
-   📦 RESTful API structure\
-   🗂 Organized Django project structure

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python 3.x\
-   Django\
-   Django REST Framework\
-   SQLite (default database)

------------------------------------------------------------------------

## 📁 Project Structure

    Smart Campus Helpdesk API/
    │
    ├── helpdesk/        # Project settings folder
    ├── tickets/         # App containing ticket logic
    ├── manage.py
    ├── requirements.txt
    └── .gitignore

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

    git clone https://github.com/reddi8055/smart-campus-helpdesk.git
    cd smart-campus-helpdesk

### 2️⃣ Create Virtual Environment

    python -m venv env

Activate:

**Windows**

    env\Scripts\activate

**Mac/Linux**

    source env/bin/activate

### 3️⃣ Install Dependencies

    pip install -r requirements.txt

### 4️⃣ Apply Migrations

    python manage.py migrate

### 5️⃣ Run Server

    python manage.py runserver

Server will start at:

http://127.0.0.1:8000/

------------------------------------------------------------------------

## 📡 API Endpoints

  Method   Endpoint           Description
  -------- ------------------ --------------------
  GET      `/tickets/`        Get all tickets
  GET      `/tickets/<id>/`   Get ticket by ID
  POST     `/tickets/`        Create new ticket
  GET      `/admin/`          Django Admin Panel

------------------------------------------------------------------------

## 🔐 Admin Access

Create superuser:

    python manage.py createsuperuser

Login at:

http://127.0.0.1:8000/admin/

------------------------------------------------------------------------

## 📌 Future Improvements

-   Authentication & Authorization\
-   Pagination\
-   Filtering & Search\
-   Deployment on Cloud (Render / Railway)\
-   JWT Token Authentication

------------------------------------------------------------------------

## 👨‍💻 Author

**Adith Reddy**

------------------------------------------------------------------------

## 📜 License

This project is for educational purposes.
