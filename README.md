# Learning Tracker App

A full-stack Learning Tracker application built using:

* Streamlit (Frontend)
* FastAPI (Backend)
* MySQL (Database)

This application helps users:

* Add skills
* View skills
* Update skills
* Track learning goals and completion dates

---

# Tech Stack

## Frontend

* Streamlit

## Backend

* FastAPI
* Uvicorn

## Database

* MySQL

## Other Libraries

* mysql-connector-python
* python-dotenv
* requests
* pandas

---

# Project Structure

```bash
learning_tracker/
│
├── backend/
│   ├── backend.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── welcome.py
│   └── pages/
│       ├── addskill.py
│       ├── skills.py
│       └── update.py
│
├── .gitignore
└── README.md
```

---

# Features

* Add new skills
* View all skills
* Update existing skills
* REST API integration
* MySQL database connectivity
* Environment variable security using `.env`

---

# Backend Setup

## 1. Navigate to Backend Folder

```bash
cd backend
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Create `.env` File

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=learning_tracker
```

## 6. Run Backend Server

```bash
uvicorn backend:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

Swagger API Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

## 1. Navigate to Frontend Folder

```bash
cd frontend
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run Streamlit App

```bash
streamlit run welcome.py
```

Frontend runs on:

```bash
http://localhost:8501
```

---

# API Endpoints

## Add Skill

```http
POST /skills
```

## View Skills

```http
GET /view_skills
```

## Update Skill

```http
PUT /update_skill/{skill_id}
```

---

# Database Table

```sql
CREATE TABLE skills (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,
    skill_name VARCHAR(255),
    topics TEXT,
    skill_level VARCHAR(100),
    goal TEXT,
    completion_date DATE
);
```

---

# Deployment

## Frontend Deployment

* Streamlit Community Cloud

## Backend Deployment

* Render

## Database Hosting

* Railway / Aiven / PlanetScale

---

# Security

* Sensitive credentials stored using `.env`
* `.env` added to `.gitignore`
* No hardcoded passwords

---

# Future Improvements

* Authentication system
* Delete skill feature
* Skill progress tracking
* Charts and analytics
* User dashboard
* Search and filtering

---

# Author

MEGHANA
