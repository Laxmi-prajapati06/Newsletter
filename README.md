📧 Django Consultation & Newsletter System  
A robust web application built with Django and Tailwind CSS. This system allows users to sign up for newsletters and book free in-center consultations, while providing administrators with a powerful, automated dashboard to manage leads.

🌟 Key Features  
Tailwind-Powered Frontend: A modern, mobile-responsive "In-Center Consultation" booking section.

Automated Admin Panel: Leveraging Django’s built-in /admin to manage subscribers and leads with zero extra frontend code.

Database Integration: Securely stores consultation requests and email subscriptions in a relational database.

🛠 Tech Stack  
Backend: Django 5.x (Python)

Frontend: Tailwind CSS 

Database: SQLite 

Styling: Tailwind CSS

🚀 Getting Started
1. Prerequisites
Python 3.10+
Pip (Python package manager)

2. Installation

# Clone the repository
git clone https://github.com/Laxmi-prajapati06/Newsletter/
cd django-newsletter

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Django
pip install django

3. Database Setup & Admin Creation
# Run migrations to create database tables
python manage.py migrate

# Create your Admin account
python manage.py createsuperuser
4. Running the App
python manage.py runserver
Frontend: View the site at http://127.0.0.1:8000/

Admin Panel: Access the dashboard at http://127.0.0.1:8000/admin/







