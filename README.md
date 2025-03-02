Task: Develop a REST API for User Management
Project Overview
Develop a simple REST API for managing users. The API should allow clients to create, retrieve, and delete users while ensuring proper authentication and input validation.

Milestones
1. Project Setup
Set up a Python project using Flask or FastAPI.
Install necessary dependencies (Flask-SQLAlchemy, FastAPI, pydantic, etc.).
2. Database and Models
Use SQLAlchemy with SQLite as the database.
Create a User model with the following fields:
id (Primary Key, Auto-incremented Integer)
name (String, Required)
email (Unique String, Required)
Implement database migrations.
3. API Endpoints (Without Authentication)
GET /users/{user_id} – Retrieve user details.
DELETE /users/{user_id} – Delete a user.
POST /users – Create a new user (validate input).
GET /users – Retrieve all users.
4. Authentication (Basic Auth or JWT)
Secure the API with Basic Authentication or JWT.
Ensure unauthorized users cannot access the API.
5. Error Handling & Input Validation
Validate input using Pydantic (FastAPI) or Marshmallow (Flask).
Handle missing users with 404 Not Found.
Return proper HTTP status codes (400, 401, 500).
6. API Documentation (Swagger/OpenAPI)
If using FastAPI, Swagger UI is built-in.
If using Flask, use flasgger or Flask-RESTx.
Git Workflow & Contribution Process
1. Use Feature Branches
Work on new features in separate branches.
git checkout -b feature/user-model
2. Submit Pull Requests (PRs)
PRs should be merged into main.
Include a clear description of changes.
3. Code Review
Code must be reviewed before merging.
Address all feedback before finalizing PRs.
Repository High Level Structure
/project-root
 ├── README.md         # Setup and API usage guide
 ├── requirements.txt  # Dependencies
 ├── src/              # Application source code
 │   ├── main.py       # Entry point
 │   ├── models.py     # Database models
 │   ├── routes.py     # API routes
 │   ├── auth.py       # Authentication
 ├── tests/            # Unit and integration tests
Commit Message Guidelines
✅ Added user model and database setup ✅ Implemented user creation endpoint ✅ Added authentication using JWT

Expected Outcome
✔ A structured GitHub repository ✔ Working API with proper authentication and database integration ✔ Clear API documentation (Swagger/OpenAPI) ✔ Error handling & validation implemented ✔ Meaningful commits and PRs