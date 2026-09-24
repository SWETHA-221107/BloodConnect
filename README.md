# BloodConnect 🩸

BloodConnect is a Django-based web application that helps connect people who need blood with registered blood donors.

The application allows users to register as blood donors, search for donors based on blood group, and submit blood requests. An admin can manage donor and blood request information through the Django Admin Panel.

## Features

- 🩸 Donor registration
- 🔎 Find donors by blood group
- ❤️ Submit blood requests
- 👤 Store donor details such as name, blood group, phone number and city
- 🏥 Store blood request details such as requester name, blood group, hospital and phone number
- ✅ Request submission confirmation page
- 🛠️ Django Admin Panel for managing donors and blood requests
- 📱 Simple and responsive user interface

## Users

### Blood Donor
A donor can register by providing:
- Name
- Blood group
- Phone number
- City

### Blood Requester
A requester can submit:
- Name
- Required blood group
- Hospital
- Phone number

### Admin
The administrator can manage:
- Donors
- Blood requests

## Technology Stack

- **Frontend:** HTML, CSS
- **Backend:** Python, Django
- **Database:** SQLite
- **Admin:** Django Admin

## Project Structure

```text
BloodDonor/
│
├── BloodDonor/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── donor/
│   ├── migrations/
│   ├── static/
│   │   └── donor/
│   │       └── style.css
│   ├── templates/
│   │   ├── home.html
│   │   ├── find_donors.html
│   │   ├── register_donor.html
│   │   ├── blood_request.html
│   │   └── success.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── .gitignore
└── README.md
