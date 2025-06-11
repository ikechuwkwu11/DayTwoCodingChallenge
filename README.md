Django REST Framework Custom Token Authentication API
A simple REST API for user registration, login, protected route access, and logout using a custom token-based authentication system built with Django and Django REST Framework.

Features
- Register a new user
- Login and receive a custom access token
- Access protected endpoints with the token
- Logout and invalidate the token
- Basic error handling for clean API responses

Tech Stack
- Python 
- Django
- Django REST Framework

File Overview
- views.py – Handles registration, login, logout, and protected route
- models.py – Contains User and AccessToken models
- serializer.py – Serializers for user and token data
- authentication.py – Custom authentication backend using the AccessToken
