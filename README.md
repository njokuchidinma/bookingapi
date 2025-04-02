# Music Booking API

A Django-based RESTful API for booking music events, supporting role-based access for artists, event organizers, and promoters. It features JWT authentication, artist and event management, booking with background payment processing via Celery and Redis, and full Docker support for development and deployment.

---

## Features

- **User Roles**: Artist, Event Organizer, Event Promoter
- **JWT Authentication**: via `djangorestframework-simplejwt`
- **Artist Profiles**: Stage name, genre, bio, discography
- **Event Management**: Organizers create events, assign artists and promoters
- **Bookings**: Users can book tickets for events
- **Payments**: Background task using Celery + Redis
- **Change Password Endpoint**: Users can change their password securely
- **Booking & Profile Management**: Edit and delete user accounts, artist profiles, events, and bookings
- **Dockerized**: Complete setup for local development with Docker

---

## Technologies

- Django & Django REST Framework
- PostgreSQL
- Redis
- Celery
- Gunicorn
- Docker & Docker Compose

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/music-booking-api.git
cd music-booking-api
```

### 2. Create a `.env` File
```dotenv
DDATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
SECRET_KEY=your_django_secret_key
DEBUG=True
```
> Note: Do not commit your `.env` file or expose sensitive database credentials publicly.

### 3. Build & Run with Docker Compose
```bash
docker-compose up --build
```

### 4. Apply Migrations and Create Superuser
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 5. Collect Static Files (Optional for Admin Panel)
```bash
docker-compose exec web python manage.py collectstatic --noinput
```

---

## API Endpoints

### Authentication
- `POST /api/accounts/register/`
- `POST /api/accounts/login/`
- `POST /api/accounts/change-password/`


### Artist Profiles
- `POST /api/artists/profiles/`
- `GET /api/artists/profiles/`
- `PUT /api/artists/profiles/<id>/`
- `DELETE /api/artists/profiles/<id>/`

### Events
- `POST /api/events/event/`
- `GET /api/events/event/`
- `PUT /api/events/event/<id>/`
- `DELETE /api/events/event/<id>/`

### Bookings
- `POST /api/bookings/`
- `GET /api/bookings/`
- `PUT /api/bookings/<id>/`
- `DELETE /api/bookings/<id>/`

---

## Running Celery Worker
```bash
docker-compose exec celery celery -A bookingapi worker --loglevel=info
```

---

## Postman Collection
You can find the full list of endpoints in the shared Postman collection:
https://interstellar-satellite-896143.postman.co/workspace/Personal-Workspace~8d066e17-daac-4c30-8a20-f52dbc49d22f/collection/36599644-19fb42ec-6d65-41af-88ba-10e7553961ac?action=share&creator=36599644

---

## Notes
- Redis is required for Celery to function properly
- Use valid JWT tokens for protected routes
- Roles (artist, promoter, organizer) determine API access
- Make sure to set `DEBUG=False` and secure environment variables in production

---

## Author
Chidinma Njoku

