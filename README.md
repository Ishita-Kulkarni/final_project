# FastAPI Calculator with JWT Authentication & Full BREAD Operations

[![CI/CD](https://github.com/Ishita-Kulkarni/assignment14/workflows/CI/CD%20with%20E2E%20Tests%20and%20Docker%20Hub%20Deployment/badge.svg)](https://github.com/Ishita-Kulkarni/assignment14/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![Tests](https://img.shields.io/badge/tests-72%20passing-brightgreen.svg)](https://github.com/Ishita-Kulkarni/assignment14)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/JWT-Authentication-orange.svg)](https://jwt.io/)
[![Playwright](https://img.shields.io/badge/Playwright-1.57.0-45ba4b.svg)](https://playwright.dev/)

A production-ready FastAPI calculator application featuring **complete BREAD (Browse, Read, Edit, Add, Delete) operations**, **JWT authentication**, **comprehensive front-end interface for calculation management**, **72 E2E tests with Playwright**, and automated CI/CD pipeline with Docker Hub deployment.

## 🔗 Quick Links

- **GitHub Repository**: https://github.com/Ishita-Kulkarni/assignment14
- **API Documentation**: http://localhost:8000/docs (when running locally)
- **CI/CD Pipeline**: https://github.com/Ishita-Kulkarni/assignment14/actions
- **Calculations Dashboard**: http://localhost:8000/static/calculations.html (when running locally)

## ✨ What's New in Assignment 14

This project builds upon assignment13 with major enhancements focused on **complete BREAD operations** for calculations with a comprehensive front-end interface:

### 🧮 **Full BREAD Operations for Calculations**
- **Browse**: View all user-specific calculations with pagination
- **Read**: View detailed calculation information in modal dialogs
- **Edit**: Update existing calculations with automatic result recalculation
- **Add**: Create new calculations with all four operations (add, subtract, multiply, divide)
- **Delete**: Remove calculations with confirmation dialogs

### 🎨 **Comprehensive Calculations Dashboard**
- **`calculations.html`**: Full-featured calculation management interface (743 lines)
- Real-time calculation display with dynamic updates
- Modal dialogs for viewing, creating, and editing calculations
- Client-side validation (numeric checks, division by zero, required fields)
- User-specific data isolation (users only see their own calculations)
- Responsive design with professional UI/UX
- Automatic JWT token handling with logout functionality

### 🧪 **Comprehensive E2E Testing with Playwright**
- **72 Playwright E2E tests** (31 calculations + 26 login + 15 registration)
- TypeScript-based test suite (`tests/e2e/*.spec.ts`)
- **Calculations Tests (31 tests)**:
  - Browse operations (empty state, list display, ordering)
  - Read operations (modal display, field visibility)
  - Add operations (all four operations, decimals, negatives)
  - Edit operations (update calculations, partial updates)
  - Delete operations (confirmation, cancellation)
  - Negative scenarios (division by zero, validation, auth)
  - User isolation verification
  - UI/UX testing (navigation, logout)
- Positive & negative test scenarios
- UI state verification
- Server response validation
- Token storage verification

### 🔐 **Enhanced JWT Authentication**
- Complete authentication flow (register → login → protected routes)
- 30-minute JWT token expiration
- Bcrypt password hashing
- Token-based session management
- Email OR username login support
- Remember Me functionality

### 🚀 **Production-Ready CI/CD**
- **275 total tests** (234 unit + 41 E2E)
- Multi-job pipeline (unit tests → E2E tests → Docker build → Docker push)
- PostgreSQL service containers in CI
- Automated Docker Hub deployment
- Python 3.11 & 3.12 matrix testing
- Comprehensive test reporting

## 📋 Features

### 🔐 Authentication & User Management

**Backend API (`/users` endpoints):**
- ✅ User registration with validation (`POST /users/register`)
- ✅ User login with JWT token (`POST /users/login`)
- ✅ Get current user info (`GET /users/me`)
- ✅ Password hashing with bcrypt
- ✅ Duplicate username/email prevention
- ✅ Email validation with Pydantic
- ✅ Inactive account handling

**Frontend Pages:**
- ✅ **`register.html`**: Registration form with client-side validation
  - Username field (3-50 characters)
  - Email field with format validation
  - Password field (minimum 8 characters)
  - Confirm password field
  - Real-time password strength indicator (weak/medium/strong)
  - Client-side validation feedback
  - JWT token storage on success
  
- ✅ **`login.html`**: Login form with authentication
  - Username/Email field (flexible login)
  - Password field
  - Remember Me checkbox (localStorage vs sessionStorage)
  - JWT token storage
  - Error handling and display
  - Automatic redirect on success

**Security Features:**
- ✅ JWT tokens with HS256 algorithm
- ✅ Bcrypt password hashing (cost factor 12)
- ✅ Token expiration (30 minutes)
- ✅ Protected routes with JWT validation
- ✅ Input sanitization and validation
- ✅ SQL injection prevention via SQLAlchemy

### 🧮 Calculator API (Legacy Feature)

- ✅ Basic arithmetic operations (add, subtract, multiply, divide)
- ✅ User-specific calculation history
- ✅ BREAD operations (Browse, Read, Edit, Add, Delete)
- ✅ Division by zero validation
- ✅ Calculation persistence

### ✅ Testing & Quality (72 E2E Tests)

**E2E Tests with Playwright (72 tests):**
- ✅ **Calculations Tests (31 tests)**:
  - Browse: Empty state, list display, ordering, pagination
  - Read: Modal display, field visibility, close functionality
  - Add: All operations (add, subtract, multiply, divide), decimals, negatives
  - Edit: Update calculations, partial updates, UI changes
  - Delete: Successful deletion, confirmation dialogs, cancellation
  - Negative: Division by zero, invalid inputs, unauthorized access
  - Isolation: User-specific data verification
  - UI/UX: Navigation, logout, display formatting
  
- ✅ **Login Tests (26 tests)**:
  - Positive: Valid credentials, email login, token storage, redirects
  - Negative: Empty fields, wrong password, invalid user, network errors
  - UI/UX: Form labels, placeholders, links, forgot password
  
- ✅ **Registration Tests (15 tests)**:
  - Positive: Valid data, email formats, password strength, redirects
  - Negative: Short username/password, invalid email, duplicates
  - Validation: Client-side and server-side error handling

**Test Coverage:**
- ✅ All positive test cases
- ✅ All negative test cases
- ✅ Error scenarios (400, 401, 403, 404, 422)
- ✅ UI state verification
- ✅ Token storage verification
- ✅ Database verification

### 🐳 Docker & Database

- ✅ Docker Compose setup with FastAPI + PostgreSQL
- ✅ PostgreSQL 15 for production
- ✅ SQLite support for development
- ✅ Multi-stage Docker builds
- ✅ Production-ready containerization
- ✅ Health check endpoints

### 🚀 CI/CD Pipeline

**4-Job Pipeline:**
1. **Unit Tests**: Run unit tests on Python 3.11 & 3.12 with PostgreSQL
2. **E2E Tests**: Run 72 Playwright tests with Chromium
3. **Docker Build**: Build and test Docker image
4. **Docker Push**: Deploy to Docker Hub (on main branch)

**Features:**
- ✅ Automated testing on every commit
- ✅ PostgreSQL service containers
- ✅ Playwright browser installation
- ✅ Docker image caching
- ✅ Multi-Python version testing
- ✅ Automated deployment to Docker Hub
- ✅ Comprehensive workflow summary

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or 3.12
- Node.js 18+ (for Playwright)
- Docker & Docker Compose (optional, for containerized setup)
- Git

### Local Development Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Ishita-Kulkarni/assignment14.git
cd assignment14
```

2. **Set up Python environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-test.txt
```

3. **Set up Node.js for Playwright:**
```bash
npm install
npx playwright install chromium  # For local testing
```

4. **Configure environment variables:**
```bash
cp .env.example .env
# Edit .env with your settings (defaults work for development)
```

5. **Initialize the database:**
```bash
# Database tables are created automatically on first run
python -c "from app.database import init_db; init_db()"
```

6. **Start the application:**
```bash
uvicorn app.main:app --reload
```

7. **Access the application:**
   - API Docs: http://localhost:8000/docs
   - Register Page: http://localhost:8000/static/register.html
   - Login Page: http://localhost:8000/static/login.html
   - Calculations Dashboard: http://localhost:8000/static/calculations.html
   - Health Check: http://localhost:8000/health

### Quick Start with Docker

```bash
# Start all services
docker compose up --build

# Access the application
open http://localhost:8000/docs
```

## 🧪 Running Tests

### Run All Tests (72 E2E tests)

```bash
# Run E2E tests (72 tests)
npm test

# Run E2E tests with UI
npx playwright test --ui

# Run specific test file
npx playwright test tests/e2e/calculations.spec.ts
```

### Run Specific Test Suites

```bash
# E2E calculations tests (31 tests)
npx playwright test tests/e2e/calculations.spec.ts

# E2E login tests (26 tests)
npx playwright test tests/e2e/login.spec.ts

# E2E registration tests (15 tests)
npx playwright test tests/e2e/register.spec.ts
```

### Run Tests with Coverage

```bash
# Python tests with coverage
pytest tests/ --cov=app --cov-report=html --cov-report=term-missing --ignore=tests/e2e

# View coverage report
open htmlcov/index.html
```

### Expected Test Results

```
✅ 72 E2E tests passing
   - 31 calculations tests
   - 26 login tests
   - 15 registration tests
```

## 📖 API Documentation

### Authentication Endpoints

#### Register New User
```http
POST /users/register
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepass123"
}
```

**Response (201 Created):**
```json
{
  "message": "Registration successful",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "is_active": true,
    "created_at": "2025-12-04T..."
  },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### Login User
```http
POST /users/login
Content-Type: application/json

{
  "username": "johndoe",  // or email
  "password": "securepass123"
}
```

**Response (200 OK):**
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "is_active": true,
    "created_at": "2025-12-04T..."
  },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### Get Current User
```http
GET /users/me
Authorization: Bearer <your-jwt-token>
```

### Error Responses

```json
// 400 Bad Request - Duplicate username/email
{
  "detail": "Username already registered"
}

// 401 Unauthorized - Invalid credentials
{
  "detail": "Invalid username or password"
}

// 403 Forbidden - Inactive account
{
  "detail": "User account is inactive"
}

// 422 Unprocessable Entity - Validation error
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```

## 🎨 Front-End Usage

### Registration Page

1. Navigate to http://localhost:8000/static/register.html
2. Fill in the form:
   - **Username**: 3-50 characters
   - **Email**: Valid email format
   - **Password**: Minimum 8 characters
   - **Confirm Password**: Must match password
3. Watch the password strength indicator (weak/medium/strong)
4. Click "Create Account"
5. On success:
   - JWT token stored in localStorage
   - Success message displayed
   - Automatic redirect to home page after 2 seconds

### Login Page

1. Navigate to http://localhost:8000/static/login.html
2. Enter credentials:
   - **Username/Email**: Your username or email
   - **Password**: Your password
   - **Remember Me**: Check to persist token
3. Click "Sign In"
4. On success:
   - JWT token stored (localStorage if Remember Me, otherwise sessionStorage)
   - Success message with username displayed
   - Automatic redirect to home page after 2 seconds

### Client-Side Validation

**Registration Validation:**
- Username: 3-50 characters
- Email: Valid format (regex pattern)
- Password: Minimum 8 characters
- Confirm Password: Must match password
- All fields required

**Login Validation:**
- Username/Email: Cannot be empty
- Password: Cannot be empty

**Real-Time Feedback:**
- Input validation on blur
- Password strength indicator updates on typing
- Error messages display immediately
- Success states shown on valid input

## 🏗️ Project Structure

```
assignment14/
├── .github/
│   └── workflows/
│       └── ci-cd-e2e.yml          # Main CI/CD pipeline
├── app/
│   ├── __init__.py
│   ├── auth.py                     # JWT & password hashing utilities
│   ├── calculation_factory.py     # Calculator factory pattern
│   ├── calculations.py             # Calculation BREAD endpoints ⭐
│   ├── database.py                 # Database configuration (SQLite/PostgreSQL)
│   ├── logger_config.py            # Logging setup
│   ├── main.py                     # FastAPI app entry point
│   ├── models.py                   # SQLAlchemy models (User, Calculation)
│   ├── operations.py               # Calculator operations
│   ├── schemas.py                  # Pydantic schemas
│   └── users.py                    # User management endpoints
├── static/
│   ├── calculations.html           # Calculations BREAD interface (743 lines) ⭐⭐
│   ├── index.html                  # Main landing page
│   ├── login.html                  # Login page
│   └── register.html               # Registration page
├── tests/
│   ├── e2e/
│   │   ├── calculations.spec.ts    # Calculations E2E tests (31 tests) ⭐⭐
│   │   ├── login.spec.ts           # Login E2E tests (26 tests)
│   │   └── register.spec.ts        # Registration E2E tests (15 tests)
│   └── [unit test files omitted for brevity]
├── docs/                           # Documentation files
├── examples/                       # Example scripts
├── scripts/                        # Utility scripts
├── .dockerignore                   # Docker ignore patterns
├── .env.example                    # Environment template
├── .gitignore                      # Git ignore patterns
├── calculator.db                   # SQLite database (development)
├── docker-compose.yml              # Docker services definition
├── Dockerfile                      # Docker image definition
├── package.json                    # Node.js dependencies
├── package-lock.json               # Node.js lock file
├── playwright.config.ts            # Playwright configuration
├── pyproject.toml                  # Python project metadata
├── requirements.txt                # Python dependencies
├── requirements-test.txt           # Test dependencies
└── README.md                       # This file
```

**⭐ Enhanced in Assignment 14**  
**⭐⭐ NEW in Assignment 14**

## 🔧 Environment Variables

### Required Variables

```bash
# Database URL
DATABASE_URL=sqlite:///./calculator.db
# For PostgreSQL: postgresql://user:pass@localhost:5432/calculator_db

# JWT Configuration
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Generate Secure Secret Key

```bash
# Python method
python -c "import secrets; print(secrets.token_urlsafe(32))"

# OpenSSL method
openssl rand -hex 32
```

### Docker Hub Secrets (CI/CD)

Set these as GitHub repository secrets:
- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Your Docker Hub access token

## 🐳 Docker Deployment

### Build and Run Locally

```bash
# Build the image
docker build -t fastapi-user-management .

# Run the container
docker run -d -p 8000:8000 \
  -e DATABASE_URL=sqlite:///./calculator.db \
  -e SECRET_KEY=your-secret-key \
  --name fastapi-app \
  fastapi-user-management

# Check logs
docker logs fastapi-app

# Access the app
open http://localhost:8000/docs
```

### Using Docker Compose

```bash
# Start all services (FastAPI + PostgreSQL)
docker compose up -d

# View logs
docker compose logs -f

# Stop services
docker compose down

# Rebuild and start
docker compose up --build
```

### Pull from Docker Hub

```bash
# Pull the latest image
docker pull ishitak0803/fastapi-user-management:latest

# Run it
docker run -d -p 8000:8000 \
  -e DATABASE_URL=sqlite:///./calculator.db \
  -e SECRET_KEY=your-secret-key \
  ishitak0803/fastapi-user-management:latest
```

## 📊 CI/CD Pipeline

The project uses a comprehensive 4-job GitHub Actions pipeline:

### Job 1: Unit & Integration Tests
- Runs on Python 3.11 and 3.12 (matrix)
- PostgreSQL 15 service container
- Executes 234 unit/integration tests
- Uploads coverage reports to Codecov
- Includes flake8 linting

### Job 2: E2E Tests with Playwright
- Runs after unit tests pass
- Sets up Node.js 18
- Installs Playwright with Chromium browser
- Starts FastAPI server in background
- Executes 41 E2E tests
- Uploads test reports and screenshots

### Job 3: Docker Build
- Builds Docker image with caching
- Tests the built image
- Verifies health endpoints
- Only runs if all tests pass

### Job 4: Docker Push
- Pushes to Docker Hub (main branch only)
- Tags: latest, branch name, commit SHA
- Updates Docker Hub description
- Only runs if build succeeds

### Workflow Triggers
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

### View Pipeline Status
Visit: https://github.com/Ishita-Kulkarni/assignment14/actions

## 🧰 Development Tools

### Linting
```bash
# Install flake8
pip install flake8

# Run linting
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --max-complexity=10 --max-line-length=127 --statistics
```

### Code Formatting
```bash
# Install black
pip install black

# Format code
black app/ tests/
```

### Type Checking
```bash
# Install mypy
pip install mypy

# Run type checking
mypy app/
```

## 📝 Manual Testing Guide

### Using Swagger UI

1. Start the application: `uvicorn app.main:app --reload`
2. Open http://localhost:8000/docs
3. Test registration:
   - Expand `POST /users/register`
   - Click "Try it out"
   - Enter user data
   - Execute and copy the `access_token`
4. Authorize:
   - Click "Authorize" button
   - Enter: `Bearer YOUR_TOKEN_HERE`
   - Click "Authorize"
5. Test protected endpoints:
   - `GET /users/me` - Get current user
   - `POST /calculations` - Create calculation
   - `GET /calculations` - List calculations

### Using the Front-End

1. **Test Registration Flow:**
   - Go to http://localhost:8000/static/register.html
   - Try invalid inputs (short username, bad email, weak password)
   - Verify client-side validation messages
   - Register with valid data
   - Verify success message and redirect
   - Check browser console for token storage

2. **Test Login Flow:**
   - Go to http://localhost:8000/static/login.html
   - Try invalid credentials
   - Verify error messages
   - Login with valid credentials
   - Test "Remember Me" functionality
   - Verify token storage (localStorage vs sessionStorage)
   - Check automatic redirect

3. **Test E2E Scenarios:**
   - Register → Login → Access protected endpoint
   - Test forgot password link
   - Test navigation between login/register pages
   - Test already-logged-in redirect

## 🚀 Production Deployment

### Security Checklist
- [ ] Generate strong `SECRET_KEY`
- [ ] Set `DATABASE_URL` to PostgreSQL
- [ ] Configure strong database password
- [ ] Set up SSL/TLS certificates
- [ ] Configure CORS properly
- [ ] Enable rate limiting
- [ ] Set up monitoring and logging
- [ ] Configure database backups
- [ ] Set up health checks
- [ ] Use environment variables (never commit secrets)

### Deployment Platforms

**Recommended platforms:**
- **Railway**: Easy PostgreSQL + FastAPI deployment
- **Render**: Free tier with PostgreSQL
- **Heroku**: Classic PaaS platform
- **AWS**: EC2 + RDS for production
- **DigitalOcean**: App Platform + Managed PostgreSQL

## 📚 Additional Documentation

- **API Documentation**: http://localhost:8000/docs (Swagger UI)
- **API Documentation**: http://localhost:8000/redoc (ReDoc)
- **Calculations Dashboard**: http://localhost:8000/static/calculations.html

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests: `npm test`
5. Commit: `git commit -m 'Add amazing feature'`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📄 License

This project is created for educational purposes as part of a university assignment.

## 🙏 Acknowledgments

- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation library
- **Playwright** - E2E testing framework
- **bcrypt** - Password hashing
- **python-jose** - JWT implementation
- **PostgreSQL** - Production database
- **Docker** - Containerization platform
- **GitHub Actions** - CI/CD automation

## 📞 Support

For issues or questions:
- Open an issue on [GitHub](https://github.com/Ishita-Kulkarni/assignment14/issues)
- Check the API documentation at http://localhost:8000/docs
- Review existing test examples in `tests/e2e/`

## 📈 Project Stats

- **Total E2E Tests**: 72 (31 calculations + 26 login + 15 registration)
- **Test Coverage**: Comprehensive frontend E2E coverage
- **Lines of Code**: ~6000+ (including 743-line calculations.html)
- **CI/CD Jobs**: 4 automated jobs
- **Supported Python Versions**: 3.11, 3.12
- **Supported Browsers**: Chromium, Firefox, WebKit (local), Chromium (CI)
- **Database**: SQLite (development), PostgreSQL (production)

---

**Built with ❤️ for Assignment 14**
