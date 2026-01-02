# Django CRM Project

## Overview
This is a Customer Relationship Management (CRM) system built using Django. It allows users to manage customer records, including adding, viewing, updating, and deleting customer information. The application includes user authentication features such as login, registration, and logout.

## Features
- **User Authentication**: Login, register, and logout functionality.
- **Record Management**: 
  - View all customer records in a table.
  - Add new customer records.
  - Update existing records.
  - Delete records.
  - View individual record details.
- **Responsive UI**: Built with Bootstrap for a clean, responsive interface.

## Project Structure
```
CRM_project/
├── requirements.txt          # Python dependencies
├── .gitignore               # Files to ignore in Git
├── .vscode/                 # VS Code settings
├── dcrm/                    # Main Django project directory
│   ├── manage.py            # Django management script
│   ├── mydb.py              # Custom database script (if any)
│   ├── db.sqlite3           # SQLite database (ignored in Git)
│   ├── dcrm/                # Django project settings
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py      # Project settings
│   │   ├── urls.py          # Main URL configuration
│   │   ├── wsgi.py
│   │   └── __pycache__/
│   └── website/             # Main Django app
│       ├── __init__.py
│       ├── apps.py
│       ├── models.py        # Record model
│       ├── views.py         # View functions
│       ├── forms.py         # Forms for records and signup
│       ├── urls.py          # App URL configuration
│       ├── __pycache__/
│       ├── migrations/      # Database migrations
│       │   ├── __init__.py
│       │   └── 0001_initial.py
│       └── templates/       # HTML templates
│           ├── base.html    # Base template
│           ├── home.html    # Home page with login/table
│           ├── navbar.html  # Navigation bar
│           ├── record.html  # Individual record view
│           ├── register.html # Registration form
│           ├── add_record.html # Add record form
│           └── update_record.html # Update record form
```

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Virtual environment (recommended)

### Steps
1. **Clone the repository** (if applicable) or navigate to the project directory.

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   cd dcrm
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user.

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Login with your created user or register a new account.

## Usage
- **Home Page**: Displays login form for unauthenticated users or a table of records for logged-in users.
- **Register**: Create a new user account.
- **Add Record**: Add a new customer record.
- **View/Update/Delete Records**: Click on record IDs to view details, edit, or delete.
- **Logout**: Log out from the application.

## Technologies Used
- **Backend**: Django 5.1
- **Database**: SQLite (default; can be changed to MySQL via settings)
- **Frontend**: HTML, CSS (Bootstrap), Django Templates
- **Authentication**: Django's built-in auth system

## Contributing
1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test thoroughly.
5. Submit a pull request.

## License
This project is for educational purposes. Feel free to modify and use as needed.

## Contact
For questions or issues, please reach out to the project maintainer.