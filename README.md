# Silver Pine State University - Student Portal
# TO SEE A VIDEO DEMO OF THIS PROJECT PLEASE VISIT: https://www.youtube.com/watch?v=s98uzzpjrAc 

An elite Ivy League university student management system featuring course registration, grade tracking, financial aid management, and academic calendar.

## Spin this up
- open terminal and type cd silverpine_university
- Now, open your virtual environment by typing source venv/Scripts/activate inside the terminal
- Now, type this in the terminal python manage.py runserver
- Now, open it in another browser with  http://127.0.0.1:8000/

## Features

- **Student Authentication** - Simple name-based login
- **Course Catalog** - Browse 80+ courses with detailed information
- **Course Registration** - Real-time seat availability, conflict detection, shopping cart system
- **Grade Portal** - View transcripts, GPA calculations, and academic history
- **Schedule Viewer** - Interactive weekly calendar
- **Financial Aid** - Track aid packages, tuition payments, and account balance
- **Academic Calendar** - Important dates and deadlines

## Technology Stack

- **Backend:** Django 5.0
- **Frontend:** HTML5, CSS3, JavaScript
- **3D Graphics:** Three.js
- **Database:** SQLite
- **Design:** Glassmorphism, responsive design

## School Colors

- Dark Green: #1a4d2e
- Silver: #c0c0c0
- Black: #000000

## Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## Project Structure
```
silverpine_university/
├── apps/
│   ├── students/
│   ├── courses/
│   ├── grades/
│   ├── financial_aid/
│   └── calendar/
├── config/
├── static/
├── templates/
└── media/
```

---

**Silver Pine State University - Excellence in Education Since 1865**
**Ranked #1 in the Nation**