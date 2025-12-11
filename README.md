# FastAPI Advanced Calculator with JWT Authentication & 8 Operations

[![CI/CD](https://github.com/Ishita-Kulkarni/final_project/workflows/CI/CD%20with%20E2E%20Tests%20and%20Docker%20Hub%20Deployment/badge.svg)](https://github.com/Ishita-Kulkarni/final_project/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-2.0.0-green.svg)](https://fastapi.tiangolo.com/)
[![Tests](https://img.shields.io/badge/tests-300%20passing-brightgreen.svg)](https://github.com/Ishita-Kulkarni/final_project)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/JWT-Authentication-orange.svg)](https://jwt.io/)
[![Playwright](https://img.shields.io/badge/Playwright-E2E%20Tests-45ba4b.svg)](https://playwright.dev/)

A production-ready FastAPI calculator application featuring **8 advanced mathematical operations** (including power, modulus, square root, nth root), **complete BREAD (Browse, Read, Edit, Add, Delete) operations**, **JWT authentication**, **comprehensive front-end interfaces**, **300+ tests**, and automated CI/CD pipeline with Docker Hub deployment.

## 🔗 Quick Links

- **GitHub Repository**: https://github.com/Ishita-Kulkarni/final_project
- **API Documentation**: http://localhost:8000/docs (when running locally)
- **Calculator Interface**: http://localhost:8000/calculator (when running locally)
- **Calculations Dashboard**: http://localhost:8000/static/calculations.html (when running locally)
- **CI/CD Pipeline**: https://github.com/Ishita-Kulkarni/final_project/actions

## ✨ New Features - Advanced Calculator Operations

This project implements **4 additional advanced mathematical operations** beyond basic arithmetic:

### 🔢 **Advanced Mathematical Operations**
1. **Power (Exponentiation)**: `a^b` - Raise a number to a power
   - Supports negative exponents: `2^-1 = 0.5`
   - Handles zero exponents: `10^0 = 1`
   - Overflow protection for large results
   
2. **Modulus (Remainder)**: `a % b` - Find remainder after division
   - Handles decimal operands
   - Prevents modulus by zero
   
3. **Square Root**: `√a` - Calculate square root
   - Single operand operation
   - Prevents negative number inputs
   - Returns precise decimal results
   
4. **Nth Root**: `ⁿ√a` - Calculate nth root of a number
   - Cube root: `³√27 = 3`
   - Fourth root: `⁴√16 = 2`
   - Supports odd roots of negative numbers: `³√-8 = -2`
   - Prevents even roots of negative numbers
   - Validates root degree (n ≠ 0)

### 🧮 **Complete Calculator Features**
- **8 Total Operations**: add, subtract, multiply, divide, power, modulus, square_root, nth_root
- **Smart UI**: Dynamic input fields (num2 disabled for square_root)
- **Helper Text**: Operation-specific guidance
- **Mathematical Notation**: Special symbols (√, ⁿ√, ^, %)
- **Error Handling**: Comprehensive validation for all edge cases
### 🧮 **Complete BREAD Operations for Calculations**
- **Browse**: View all user-specific calculations with pagination
- **Read**: View detailed calculation information in modal dialogs
- **Edit**: Update existing calculations with automatic result recalculation (all 8 operations)
- **Add**: Create new calculations with all 8 operations
- **Delete**: Remove calculations with confirmation dialogs

### 🎨 **Comprehensive Front-End Interfaces**
- **`index.html`**: Interactive calculator with 8 operations (425 lines)
  - Real-time calculation with all operations
  - Smart form controls (conditional num2 field)
  - Operation-specific helper text
  - Mathematical notation display
  - Client-side validation
  
- **`calculations.html`**: Full-featured calculation management dashboard (743 lines)
  - Real-time calculation display with dynamic updates
  - Modal dialogs for viewing, creating, and editing
  - Client-side validation (numeric checks, division by zero, required fields)
  - User-specific data isolation
  - Responsive design with professional UI/UX
  - Automatic JWT token handling with logout functionality

### 🧪 **Comprehensive Testing Suite**
- **300 total tests** (75 unit + 103 integration + 122 E2E)
- **Unit Tests** (`tests/test_*.py`):
  - Operations testing (all 8 operations with edge cases)
  - Schema validation (Pydantic models)
  - Authentication (bcrypt, JWT)
  - Factory pattern implementation
  
- **Integration Tests** (`tests/test_*_api.py`):
  - API endpoint testing
  - Database operations
  - User authentication flows
  
- **E2E Tests** (`tests/e2e/*.spec.ts` - TypeScript/Playwright):
  - **Calculator Tests (37 tests)**: All 8 operations, input validation, UI state
  - **Calculations CRUD Tests (31 tests)**: Browse, Read, Edit, Add, Delete operations
  - **Login Tests (26 tests)**: Authentication flow, token storage, validation
  - **Registration Tests (15 tests)**: User signup, validation, password strength

### 🔐 **Enhanced JWT Authentication**
- Complete authentication flow (register → login → protected routes)
- 30-minute JWT token expiration
- Bcrypt password hashing
- Token-based session management
- Email OR username login support
- Remember Me functionality

### 🚀 **Production-Ready CI/CD**
- **300 total tests** (75 unit + 103 integration + 122 E2E)
- **4-stage pipeline**: unit tests → E2E tests → Docker build → Docker push
- PostgreSQL service containers in CI
- Automated Docker Hub deployment on main branch
- Python 3.11 & 3.12 matrix testing
- Comprehensive test reporting with coverage
- E2E tests with Playwright in headless mode

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

### 🧮 Calculator Features

**8 Mathematical Operations:**
- ✅ **Basic**: Add, Subtract, Multiply, Divide
- ✅ **Power**: Exponentiation with negative/zero exponent support
- ✅ **Modulus**: Remainder after division
- ✅ **Square Root**: Single operand, negative number validation
- ✅ **Nth Root**: Cube root, fourth root, odd/even root handling

**Calculation Management (BREAD):**
- ✅ Browse: View all user-specific calculations with pagination
- ✅ Read: Detailed calculation view in modal dialogs
- ✅ Edit: Update calculations with automatic result recalculation
- ✅ Add: Create calculations with all 8 operations
- ✅ Delete: Remove calculations with confirmation
- ✅ User-specific data isolation
- ✅ Calculation persistence in database

### ✅ Testing & Quality (300+ Tests)

**Unit Tests (75 tests):**
- ✅ All 8 operations with edge cases
- ✅ Pydantic schema validation
- ✅ Authentication (bcrypt, JWT)
- ✅ Factory pattern implementation
- ✅ Custom exception handling

**Integration Tests (103 tests):**
- ✅ API endpoint testing (BREAD operations)
- ✅ Database operations and transactions
- ✅ User authentication flows
- ✅ Error handling and validation

**E2E Tests with Playwright (122 tests):**
- ✅ **Calculator Tests (37 tests)**: 
  - All 8 operations (power, modulus, square_root, nth_root)
  - Input validation and error handling
  - UI state management and helper text
  
- ✅ **Calculations CRUD Tests (31 tests)**:
  - Browse, Read, Edit, Add, Delete operations
  - User isolation and authorization
  - Modal interactions and UI feedback
  
- ✅ **Login Tests (26 tests)**:
  - Valid/invalid credentials, token storage, redirects
  
- ✅ **Registration Tests (15 tests)**:
  - Validation, password strength, duplicate handling

**Test Coverage:**
- ✅ 86% code coverage on app module
- ✅ All positive and negative test cases
- ✅ Error scenarios (400, 401, 403, 404, 422)
- ✅ UI state verification
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

## 📁 Project Structure

```
final_project/
├── app/                              # Main application package
│   ├── __init__.py
│   ├── main.py                       # FastAPI application & routes
│   ├── database.py                   # Database configuration
│   ├── models.py                     # SQLAlchemy models (User, Calculation)
│   ├── schemas.py                    # Pydantic schemas & validation
│   ├── auth.py                       # JWT authentication utilities
│   ├── users.py                      # User management router
│   ├── calculations.py               # Calculations BREAD router
│   ├── operations.py                 # 8 mathematical operations
│   ├── calculation_factory.py        # Factory pattern implementation
│   └── logger_config.py              # Logging configuration
│
├── static/                           # Frontend HTML pages
│   ├── index.html                    # Interactive calculator (425 lines)
│   ├── calculations.html             # CRUD dashboard (743 lines)
│   ├── login.html                    # Login page
│   └── register.html                 # Registration page
│
├── tests/                            # Test suite (300+ tests)
│   ├── test_auth.py                  # Authentication unit tests
│   ├── test_operations.py            # Operations unit tests (8 ops)
│   ├── test_schemas.py               # Schema validation tests
│   ├── test_models.py                # Database model tests
│   ├── test_calculations.py          # Calculation logic tests
│   ├── test_calculations_api.py      # Calculations API integration tests
│   ├── test_users.py                 # User API integration tests
│   ├── test_main.py                  # Main endpoint tests
│   ├── test_logging.py               # Logging tests
│   ├── e2e/                          # End-to-end tests (Playwright)
│   │   ├── calculator.spec.ts        # Calculator UI tests (37 tests)
│   │   ├── calculations.spec.ts      # CRUD operations tests (31 tests)
│   │   ├── login.spec.ts             # Login flow tests (26 tests)
│   │   └── register.spec.ts          # Registration tests (15 tests)
│   ├── E2E_TESTING.md               # E2E testing documentation
│   └── README.md                     # Testing guide
│
├── scripts/                          # Utility scripts
│   ├── ci_check.sh                   # CI validation script
│   ├── run_tests.sh                  # Test runner
│   └── setup-tests.sh                # Test environment setup
│
├── docs/                             # Documentation
│   ├── JWT_AUTHENTICATION.md         # JWT implementation guide
│   ├── FRONTEND_AUTHENTICATION.md    # Frontend auth flows
│   ├── LOGGING.md                    # Logging documentation
│   ├── CI_CD_PIPELINE.md             # Pipeline documentation
│   ├── CI_CD_SETUP.md                # CI/CD setup guide
│   ├── QUICK_REFERENCE.md            # Quick reference
│   └── SETUP_CHECKLIST.md            # Setup checklist
│
├── examples/                         # Example scripts
│   ├── demo_user_endpoints.py        # User API demo
│   ├── calculations_api.py           # Calculations API demo
│   ├── test_jwt_token.py             # JWT testing demo
│   ├── factory_usage_examples.py     # Factory pattern examples
│   └── test_api_manual.py            # Manual API testing
│
├── .github/workflows/                # GitHub Actions CI/CD
│   └── ci-cd-e2e.yml                 # 4-stage pipeline
│
├── logs/                             # Application logs
│   ├── app.log                       # General application logs
│   └── error.log                     # Error logs
│
├── Dockerfile                        # Multi-stage Docker build
├── docker-compose.yml                # Docker services (FastAPI + PostgreSQL)
├── pyproject.toml                    # Python project config & pytest
├── playwright.config.ts              # Playwright E2E config
├── package.json                      # Node.js dependencies (Playwright)
├── requirements.txt                  # Python dependencies
├── requirements-test.txt             # Test dependencies
├── .env.example                      # Environment variables template
├── .gitignore                        # Git ignore patterns
└── README.md                         # This file
```

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
   - **Calculator**: http://localhost:8000/calculator
   - **API Docs**: http://localhost:8000/docs
   - **Login Page**: http://localhost:8000 (root redirects to login)
   - **Register Page**: http://localhost:8000/static/register.html
   - **Calculations Dashboard**: http://localhost:8000/static/calculations.html (requires auth)
   - **Health Check**: http://localhost:8000/health

### Quick Start with Docker

```bash
# Start all services
docker compose up --build

# Access the application
open http://localhost:8000/docs
```

## 🧪 Running Tests

### Run All Tests (300+ tests)

```bash
# Run Python unit & integration tests (178 tests)
pytest tests/ --ignore=tests/e2e -v

# Run E2E tests (122 tests)
npm test

# Run all tests
pytest tests/ --ignore=tests/e2e && npm test
```

### Run Specific Test Suites

```bash
# Unit tests only
pytest tests/test_operations.py -v  # 8 operations tests
pytest tests/test_auth.py -v        # Authentication tests
pytest tests/test_schemas.py -v     # Schema validation tests

# Integration tests
pytest tests/test_calculations_api.py -v  # Calculations API
pytest tests/test_users.py -v             # User API

# E2E calculator tests (37 tests - all 8 operations)
npx playwright test tests/e2e/calculator.spec.ts

# E2E calculations CRUD tests (31 tests)
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

### Run Tests with Playwright UI

```bash
# Run E2E tests with interactive UI
npx playwright test --ui

# Run specific test file with UI
npx playwright test tests/e2e/calculator.spec.ts --ui
```

### Expected Test Results

```
✅ 300 total tests passing:
   - 75 unit tests (operations, auth, schemas, models, etc.)
   - 103 integration tests (API endpoints, database)
   - 122 E2E tests (calculator, calculations CRUD, login, registration)
   
✅ 86% code coverage on app module
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
- Open an issue on [GitHub](https://github.com/Ishita-Kulkarni/final_project/issues)
- Check the API documentation at http://localhost:8000/docs
- Review existing test examples in `tests/e2e/`
- Read the documentation in `docs/` folder

## 📈 Project Stats

- **Total Tests**: 300+ (75 unit + 103 integration + 122 E2E)
- **Test Coverage**: 86% on app module
- **Mathematical Operations**: 8 (add, subtract, multiply, divide, power, modulus, square_root, nth_root)
- **Lines of Code**: ~7500+ (including test suite)
- **CI/CD Jobs**: 4 automated stages
- **Supported Python Versions**: 3.11, 3.12
- **Supported Browsers**: Chromium (CI), Chromium/Firefox/WebKit (local)
- **Database**: SQLite (development), PostgreSQL 15 (production)
- **Front-End Pages**: 4 (calculator, calculations dashboard, login, register)

---

**Built with ❤️ for Advanced Calculator Project**
