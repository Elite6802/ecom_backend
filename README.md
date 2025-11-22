E-Commerce Backend – ProDev BE

A fully functional e-commerce backend built using Django, designed to simulate real-world backend engineering workflows. The project emphasizes clean architecture, scalability, secure authentication, query optimization, and API documentation.

🚀 Overview

This project implements a robust backend system to support an e-commerce product catalog. It provides APIs for managing products, categories, and user accounts while enabling efficient product discovery through filtering, sorting, and pagination.

This case study mirrors real-world backend engineering expectations, focusing on:

Designing relational database schemas

Implementing backend business logic

Creating production-ready API documentation

Optimizing query performance

🎯 Project Goals
1. CRUD APIs

Full CRUD for Products

CRUD for Categories

User registration & login using JWT authentication

2. Filtering, Sorting & Pagination

Filter products by category

Sort by fields such as price

Paginated responses for scalable browsing

3. Database Optimization

Efficient Django ORM queries

Indexing and query optimization where needed

🛠️ Technologies Used
Technology	Purpose
Django	Backend framework
SQLite / Django default database	Relational DB for development (Django database used instead of PostgreSQL)
Django REST Framework	API building
JWT Authentication	Secure login & access control
drf-spectacular / Swagger	Auto-generated API documentation
Python 3.12.2	Programming language
🔑 Key Features
1. CRUD Operations

Create, read, update, and delete products & categories

User management and authentication with JWT

2. Advanced API Features

Filter products by category

Sort products by price or other fields

Paginate large product lists efficiently

3. API Documentation

OpenAPI/Swagger documentation using drf-spectacular

Fully interactive API explorer for frontend teams

🧱 Implementation Process
Example Git Commit Workflow
feat: set up Django project structure
feat: configure JWT authentication
feat: add product and category CRUD APIs
feat: implement filtering, sorting, and pagination
feat: integrate Swagger API documentation
perf: optimize ORM queries and add indexing
docs: update README and API usage instructions

▶️ How to Run the Project
1. Clone the Repository
git clone https://github.com/Elite6802/ecom_backend.git
cd ecom-backend

1. Install Dependencies
pip install -r requirements.txt

1. Run Migrations
python manage.py migrate

1. Start Server
python manage.py runserver

1. Access API Documentation

Visit:

http://127.0.0.1:8000/api/schema/swagger-ui/