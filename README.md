# Healthcare Backend System - Django REST Framework

## Overview

This project is a backend system for a healthcare application built with Django and Django REST Framework (DRF). It provides secure APIs for managing patients, doctors, and their relationships using JWT authentication and PostgreSQL database.

## Features

- **User Authentication**: Secure JWT-based registration and login
- **Patient Management**: CRUD operations for patient records
- **Doctor Management**: CRUD operations for doctor records
- **Patient-Doctor Mapping**: Assign doctors to patients and manage relationships
- **RESTful API**: Clean, well-structured endpoints following REST conventions
- **PostgreSQL Database**: Relational database for data persistence
- **Environment Configuration**: Secure handling of sensitive settings

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Log in and get JWT tokens
- `POST /api/auth/token/refresh/` - Refresh access token

### Patient Management
- `POST /api/patients/` - Create a new patient
- `GET /api/patients/` - List all patients for current user
- `GET /api/patients/<id>/` - Retrieve specific patient
- `PUT /api/patients/<id>/` - Update patient
- `DELETE /api/patients/<id>/` - Delete patient

### Doctor Management
- `POST /api/doctors/` - Create a new doctor
- `GET /api/doctors/` - List all doctors
- `GET /api/doctors/<id>/` - Retrieve specific doctor
- `PUT /api/doctors/<id>/` - Update doctor
- `DELETE /api/doctors/<id>/` - Delete doctor

### Patient-Doctor Mapping
- `POST /api/mappings/` - Assign doctor to patient
- `GET /api/mappings/` - List all mappings
- `GET /api/mappings/<patient_id>/` - Get doctors for a patient
- `DELETE /api/mappings/<id>/` - Remove mapping

## Technologies Used

- Python 3.x
- Django 4.x
- Django REST Framework
- PostgreSQL
- JWT Authentication (djangorestframework-simplejwt)
- python-dotenv (for environment variables)

## Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/healthcare-backend.git
   cd healthcare-backend
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL:
   - Create a database and user
   - Update the `.env` file with your credentials (use `.env.example` as template)

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## Testing

To run tests:
```bash
python manage.py test
```

For API testing, import the Postman collection provided in the `postman` directory.

## Project Structure

```
healthcare/
├── accounts/            # User authentication app
├── doctors/            # Doctor management app
├── patients/           # Patient management app
├── mappings/           # Patient-doctor mapping app
├── healthcare/         # Main project settings
├── .env                # Environment variables
├── .env.example        # Environment variables template
├── requirements.txt    # Dependencies
└── README.md           # This file
```

## Environment Variables

Create a `.env` file based on `.env.example` with these variables:

```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
```

## Postman Testing

1. Import the Postman collection from `postman/Healthcare_API.postman_collection.json`
2. Set up environment variables in Postman:
   - `base_url`: `http://localhost:8000`
   - `access_token`: (will be set after login)
   - `refresh_token`: (will be set after login)

## API Documentation

For detailed API documentation, after running the server:
- Visit `http://localhost:8000/swagger/` for Swagger UI
- Visit `http://localhost:8000/redoc/` for ReDoc documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django REST Framework team
- SimpleJWT package maintainers
- PostgreSQL community
