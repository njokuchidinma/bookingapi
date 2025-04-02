# Music Booking API

Welcome to the Music Booking API! This API allows you to manage artist profiles, event listings, and booking transactions. It uses **Django REST Framework** for API management, **PostgreSQL** for database management, **Redis** for caching and task management, and **Celery** for background processing.

## 🚀 Features
- User registration and authentication using JWT
- Artist profile management
- Event creation and management
- Booking system with payment simulation
- Background tasks using Celery for payment confirmation
- API documentation using Swagger

---

## 🧑‍💻 Prerequisites
Make sure you have the following installed:
- Python 3.11+
- PostgreSQL
- Redis
- Docker (optional, for containerization)

---

## 🛠 Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository_url>
cd bookingapi
```

### 2. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate    # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add:
```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=music_booking
DATABASE_USER=music_user
DATABASE_PASSWORD=password123
DATABASE_HOST=localhost
DATABASE_PORT=5432
REDIS_URL=redis://localhost:6379/0
```

### 5. Set Up PostgreSQL
```sql
CREATE DATABASE music_booking;
CREATE USER music_user WITH ENCRYPTED PASSWORD 'password123';
GRANT ALL PRIVILEGES ON DATABASE music_booking TO music_user;
```

### 6. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser
```bash
python manage.py createsuperuser
```

### 8. Start Redis
Make sure Redis is running:
```bash
redis-server
```

### 9. Start Celery Worker
```bash
celery -A bookingapi worker --loglevel=info
```

### 10. Start the Application
```bash
python manage.py runserver
```

---

## 🌐 API Endpoints

### Authentication
- **POST** `/api/accounts/register/` - Register a new user
- **POST** `/api/accounts/login/` - Log in and obtain JWT tokens

### Artists
- **POST** `/api/artists/profiles/` - Create artist profile
- **GET** `/api/artists/profiles/` - View all artist profiles
- **GET** `/api/artists/profiles/{id}/` - View a specific artist profile

### Events
- **POST** `/api/events/events/` - Create an event (Event Organizer only)
- **GET** `/api/events/events/` - View all events
- **PATCH** `/api/events/events/{id}/` - Update an event
- **DELETE** `/api/events/events/{id}/` - Delete an event

### Bookings
- **POST** `/api/bookings/bookings/` - Book an event
- **GET** `/api/bookings/bookings/` - View all bookings
- **DELETE** `/api/bookings/bookings/{id}/` - Cancel a booking

---


## 🧪 Postman Collection
A Postman collection is available for testing. Import it into Postman using the `.json` file located in the `postman/` folder:
- `postman/MusicBookingAPI.postman_collection.json`

---

## ⚙️ Background Tasks
- Payments are simulated using Celery.
- Ensure the Celery worker is running before creating bookings to trigger payment processing.
```bash
celery -A bookingapi worker --loglevel=info
```

---

## 🚀 Running with Docker (Optional)
You can run the entire app using Docker and Docker Compose.
```bash
docker-compose up --build
```
This will start:
- Web server on port `8000`
- Redis on port `6379`
- Celery worker for background tasks

---

## 🛎 Support
For any issues, contact: **support@musicbookingapp.com**

Happy Booking! 🎵

