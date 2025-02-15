# Cram School Cloud

## The Pain Point
Many local schools have all their data spread out over many systems. Sharing information is difficult. 
Tracking task completion is difficult. Ensuring consistency and quality is difficult. There's no way to see everything
that happens at your school at a glance.

## The Solution
An all-in-one solution to organizing a school's data. Manage students, teachers, classes, schedules, reports,
and in-class activities from a single interface.

## Installation
This repo is the application server. It can be configured to directly deliver HTML content to the client.
Or it can deliver JSON responses to SPA and mobile clients.

```
cd projects (wherever you keep your projects)
mkdir school-mgmt
git clone https://github.com/markoco14/student-mgmt.git server .
cd server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cd server
cp .env.example .env
fill in your database info

python manage.py migrate
python manage.py createsuperuser # this gives you access to the django admin section
choose an email: admin1@adminmail.com
choose a password: admin1234
python manage.py runserver
```

Visit localhost:8000 and you should see the Django Rest Framework screen
Visit localhost:8000/admin and you should see the admin login screen