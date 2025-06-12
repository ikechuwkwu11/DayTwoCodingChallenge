# 🔐 Django REST Framework Custom Token Authentication API
A lightweight and secure REST API built with Django and Django REST Framework (DRF) that uses a custom token-based authentication system. It allows users to register, log in, access protected routes, and log out with token invalidation. Ideal for learning how to implement authentication manually, beyond built-in solutions like DRF’s TokenAuthentication or JWT.

## 🚀 Features
- User Registration (/register)
- Login with credentials to receive a custom access token (/login)
- Token-protected routes for authenticated access
- Logout functionality with token invalidation (/logout)
- Clean and structured error handling for API responses

## 🛠 Tech Stack
- Layer	Technology
- Language	Python
- Web Framework	Django
- API Framework	Django REST Framework
- Authentication	Custom Token System

## 📁 File Structure Overview
- views.py – Handles core logic: registration, login, logout, and protected views
- models.py – Defines the User and AccessToken models
- serializers.py – Serializes user credentials and token data
- authentication.py – Custom DRF authentication class using the AccessToken model

## 🔒 How It Works
- Register a user via the /register endpoint.
- Login via /login to receive a token.
- Include the token in request headers like so:

## 🧪 Testing the API
You can use tools like:
- Postman
- curl
- httpie

## 🧠 What You’ll Learn
- How to implement custom token authentication from scratch
- Using DRF authentication classes
- Handling secure login/logout flows
- Managing token lifecycle (creation, usage, invalidation)
