# FastAPI User Management System

[![CI/CD](https://github.com/Ishita-Kulkarni/assignment10/workflows/FastAPI%20User%20Management%20CI/CD/badge.svg)](https://github.com/Ishita-Kulkarni/assignment10/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Coverage](https://img.shields.io/badge/coverage-75%25-yellowgreen.svg)](https://github.com/Ishita-Kulkarni/assignment10)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-Published-blue.svg)](https://hub.docker.com/r/ishitak0803/fastapi-user-management)

A production-ready FastAPI application featuring secure user management with SQLAlchemy, bcrypt password hashing, comprehensive testing (60 tests), and automated CI/CD pipeline with Docker Hub deployment.

## 🔗 Quick Links

- **GitHub Repository**: https://github.com/Ishita-Kulkarni/assignment10
- **Docker Hub Image**: https://hub.docker.com/r/ishitak0803/fastapi-user-management
- **CI/CD Pipeline**: https://github.com/Ishita-Kulkarni/assignment10/actions

## Features

👥 **User Management System**
- User registration with email validation
- Secure password hashing with bcrypt
- User login and authentication
- CRUD operations for user management
- Unique username and email constraints

🔧 **API Backend**
- RESTful API with FastAPI
- SQLAlchemy ORM with PostgreSQL
- Pydantic schemas for validation
- Interactive API documentation (Swagger UI)
- Comprehensive logging system

🔒 **Security**
- Bcrypt password hashing (bcrypt 4.0.1)
- Input validation with Pydantic
- SQL injection prevention via SQLAlchemy
- Environment variable configuration

🐳 **Docker & Database Integration**
- Docker Compose setup with FastAPI + PostgreSQL + pgAdmin
- PostgreSQL database for data persistence
- pgAdmin for database management
- Production-ready containerization

🚀 **CI/CD Pipeline**
- Automated testing on GitHub Actions
- Multi-version Python testing (3.9-3.12)
- Docker image builds and pushes to Docker Hub
- Code coverage reporting with Codecov
- Automated deployment on successful tests

## Quick Start with Docker

### Prerequisites
- Docker Desktop installed and running
- Git
- Docker Hub account (for pushing images)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Ishita-Kulkarni/assignment10.git
cd assignment10
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

3. Start all services with Docker Compose:
```bash
docker compose up --build
```

4. Access the services:
   - **API Documentation**: http://localhost:8000/docs
   - **pgAdmin**: http://localhost:5050
   - **PostgreSQL**: localhost:5432

### pgAdmin Login
- Email: `admin@example.com`
- Password: `admin`

### Database Connection (in pgAdmin)
- Host: `db` (or `postgres`)
- Port: `5432`
- Database: `calculator_db`
- Username: `calculator_user`
- Password: `calculator_pass`

### Pull from Docker Hub

Instead of building locally, you can pull the pre-built image:

```bash
# Pull the latest image from Docker Hub
docker pull ishitak0803/fastapi-user-management:latest

# Run the container
docker run -d -p 8000:8000 \
  -e DATABASE_URL=postgresql://calculator_user:calculator_pass@host.docker.internal:5432/calculator_db \
  --name fastapi-app \
  ishitak0803/fastapi-user-management:latest

# Check if it's running
docker ps

# View logs
docker logs fastapi-app

# Access API docs
open http://localhost:8000/docs
```

**Docker Hub Repository**: https://hub.docker.com/r/ishitak0803/fastapi-user-management

**Available Tags**:
- `latest` - Most recent build from main branch
- `main` - Latest main branch build
- `main-<commit-sha>` - Specific commit builds

## Running Tests Locally

### Quick Start

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt
pip install -r requirements-test.txt

# 3. Run all tests
pytest -v

# 4. Run with coverage report
pytest --cov=. --cov-report=html --cov-report=term-missing

# 5. View coverage report
open htmlcov/index.html  # On Linux: xdg-open htmlcov/index.html
```

### Test Categories

```bash
# Run user management tests only (60 tests)
pytest tests/test_auth.py tests/test_schemas.py tests/test_models.py tests/test_users.py -v

# Run authentication tests (12 tests)
pytest tests/test_auth.py -v

# Run schema validation tests (20 tests)
pytest tests/test_schemas.py -v

# Run model tests (10 tests)
pytest tests/test_models.py -v

# Run API integration tests (18 tests)
pytest tests/test_users.py -v

# Run specific test
pytest tests/test_users.py::test_register_user -v
```

### Expected Results

✅ **60 tests** should pass  
✅ **75% coverage** overall  
✅ **100% coverage** on `auth.py`, `schemas.py`, `models.py`  
✅ **93% coverage** on `users.py`  

### Test Output Example

```
tests/test_auth.py ✓✓✓✓✓✓✓✓✓✓✓✓                    [ 20%]
tests/test_schemas.py ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓         [ 53%]
tests/test_models.py ✓✓✓✓✓✓✓✓✓✓                    [ 70%]
tests/test_users.py ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓             [100%]

==================== 60 passed in 2.5s ====================
```

### Troubleshooting Tests

If tests fail:

```bash
# Ensure correct bcrypt version (CRITICAL)
pip install bcrypt==4.0.1

# Clear pytest cache
rm -rf .pytest_cache __pycache__

# Reinstall dependencies
pip install -r requirements.txt -r requirements-test.txt

# Run tests with verbose output
pytest -vv --tb=short
```

## SQL Database Setup

All SQL scripts are in the `sql/` directory:
- `01_create_tables.sql` - Create users and calculations tables
- `02_insert_records.sql` - Insert sample data
- `03_query_data.sql` - Query and join operations
- `04_update_record.sql` - Update records
- `05_delete_record.sql` - Delete records
- `complete_setup.sql` - Run all steps at once

See [sql/README.md](sql/README.md) for detailed SQL documentation.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic
- Docker & Docker Compose (for containerized setup)
- PostgreSQL 15 (via Docker)

## Installation (Local Development)

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server:
```bash
python main.py
```

Or use uvicorn directly:
```bash
uvicorn main:app --reload
```

The application will be available at: `http://localhost:8000`

## Using the Calculator

Once the server is running, visit:
- **Web Calculator**: `http://localhost:8000` - Interactive calculator interface
- **API Docs**: `http://localhost:8000/docs` - Swagger UI for API testing
- **Alternative Docs**: `http://localhost:8000/redoc` - ReDoc documentation
- **API Info**: `http://localhost:8000/api` - API information endpoint

### Web Interface
Simply open your browser and navigate to `http://localhost:8000`. You'll see a beautiful calculator interface where you can:
1. Enter two numbers
2. Select an operation (Add, Subtract, Multiply, Divide)
3. Click "Calculate" or press Enter
4. See the result displayed instantly

## API Endpoints

### User Management

#### POST /users/register
Register a new user with username, email, and password.

**Request Body:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securePassword123"
}
```

**Response:**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "created_at": "2024-01-15T10:30:00",
  "is_active": true
}
```

#### POST /users/login
Authenticate user with username and password.

**Request Body:**
```json
{
  "username": "johndoe",
  "password": "securePassword123"
}
```

**Response:**
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com"
  }
}
```

#### GET /users
Get all users (paginated).

**Query Parameters:**
- `skip`: Number of records to skip (default: 0)
- `limit`: Maximum number of records (default: 100)

#### GET /users/{user_id}
Get a specific user by ID.

#### PUT /users/{user_id}
Update user information.

**Request Body:**
```json
{
  "email": "newemail@example.com"
}
```

#### DELETE /users/{user_id}
Delete a user.

### Calculator Endpoints

#### POST /calculate
Performs arithmetic calculations.

**Request Body:**
```json
{
  "num1": 10,
  "num2": 5,
  "operation": "add"
}
```

**Supported Operations:**
- `add` - Addition
- `subtract` - Subtraction
- `multiply` - Multiplication
- `divide` - Division

**Response:**
```json
{
  "result": 15.0,
  "operation": "add",
  "num1": 10.0,
  "num2": 5.0
}
```

### Health Check

#### GET /health
Returns application health status.

## Example Usage

Using curl:

### User Registration
```bash
curl -X POST "http://localhost:8000/users/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securePassword123"
  }'
```

### User Login
```bash
curl -X POST "http://localhost:8000/users/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securePassword123"
  }'
```

### Get All Users
```bash
curl -X GET "http://localhost:8000/users?skip=0&limit=10"
```

### Calculator Operations
```bash
# Addition
curl -X POST "http://localhost:8000/calculate" \
  -H "Content-Type: application/json" \
  -d '{"num1": 10, "num2": 5, "operation": "add"}'

# Division
curl -X POST "http://localhost:8000/calculate" \
  -H "Content-Type: application/json" \
  -d '{"num1": 20, "num2": 4, "operation": "divide"}'
```

## Error Handling

The API handles common errors:
- Division by zero returns a 400 error
- Invalid operations return a 400 error with supported operations list
- Invalid input types are caught by Pydantic validation

## Testing

The project includes comprehensive tests covering 60 test cases:

### Test Categories
- **Authentication Tests** (`tests/test_auth.py`): 12 tests for password hashing
- **Schema Tests** (`tests/test_schemas.py`): 20 tests for Pydantic validation
- **Model Tests** (`tests/test_models.py`): 10 tests for SQLAlchemy User model
- **Integration Tests** (`tests/test_users.py`): 18 tests for API endpoints
- **Calculator Tests** (`tests/test_operations.py`): 37 tests for calculator functions
- **API Tests** (`tests/test_main.py`): 37 tests for calculator API endpoints
- **Logging Tests** (`tests/test_logging.py`): 26 tests for logging system

### Running Tests

Install test dependencies:
```bash
pip install -r requirements-test.txt
```

Run all tests:
```bash
pytest -v
```

Run with coverage:
```bash
pytest --cov=. --cov-report=html --cov-report=term-missing
```

Run specific test categories:
```bash
# User management tests
pytest tests/test_auth.py tests/test_schemas.py tests/test_models.py tests/test_users.py -v

# Calculator tests
pytest tests/test_operations.py tests/test_main.py -v

# All tests with coverage
pytest -v --cov=. --cov-report=xml --cov-report=term-missing
```

### Test Coverage
Current test coverage: **75%**
- `auth.py`: 100%
- `schemas.py`: 100%
- `models.py`: 100%
- `users.py`: 93%
- `operations.py`: 100%
- `main.py`: 100%

## Logging

The application includes comprehensive logging to track operations and errors.

### Log Files
- `logs/app.log` - All application logs (DEBUG, INFO, WARNING, ERROR)
- `logs/error.log` - Error logs only (ERROR, CRITICAL)

### What Gets Logged
- ✓ All HTTP requests and responses with duration
- ✓ Calculator operations (inputs and results)
- ✓ Errors and exceptions with full stack traces
- ✓ Application startup and shutdown events

### Log Rotation
- Max file size: 10 MB
- Backup count: 5 files
- Automatic rotation when size limit is reached

### Viewing Logs
```bash
# View all logs
cat logs/app.log

# View errors only
cat logs/error.log

# Follow logs in real-time
tail -f logs/app.log
```

For detailed logging documentation, see [LOGGING.md](LOGGING.md)

## CI/CD Pipeline

The project features a comprehensive CI/CD pipeline with GitHub Actions that automatically tests and deploys your application.

### Pipeline Overview

```mermaid
graph LR
    A[Push to Main] --> B[Run Tests]
    B --> C{Tests Pass?}
    C -->|Yes| D[Build Docker Image]
    C -->|No| E[Pipeline Fails]
    D --> F[Push to Docker Hub]
    F --> G[Deployment Ready]
```

### What Happens on Push

1. **Testing Phase** (runs on every push/PR)
   - Tests run on Python 3.9, 3.10, 3.11, and 3.12
   - PostgreSQL service spins up for integration tests
   - All 60+ tests execute with coverage reporting
   - Code linting with flake8
   - Coverage report uploaded to Codecov
   - Test results archived as artifacts

2. **Build & Push Phase** (only on main branch)
   - Docker image built with multi-stage build
   - Image tagged with branch name, commit SHA, and `latest`
   - Image pushed to Docker Hub
   - Build cache optimized for faster builds

3. **Verification Phase**
   - Confirms successful deployment
   - Logs image digest for tracking

### Setting Up CI/CD

#### 1. GitHub Secrets Configuration

Add these secrets to your GitHub repository (`Settings > Secrets and variables > Actions`):

- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Docker Hub access token (not password!)

**Creating a Docker Hub Access Token:**
1. Log in to [Docker Hub](https://hub.docker.com/)
2. Go to Account Settings > Security
3. Click "New Access Token"
4. Name it (e.g., "GitHub Actions")
5. Copy the token immediately (you won't see it again!)
6. Add it as `DOCKERHUB_TOKEN` secret in GitHub

#### 2. Update Workflow File

Edit `.github/workflows/ci.yml` and replace image references:
```yaml
images: YOUR_DOCKERHUB_USERNAME/fastapi-user-management
```

#### 3. Enable GitHub Actions

Ensure GitHub Actions are enabled for your repository:
- Go to repository Settings > Actions > General
- Select "Allow all actions and reusable workflows"

### CI/CD Features

✅ **Multi-Python Version Testing**
- Tests run on Python 3.9, 3.10, 3.11, and 3.12
- Ensures compatibility across versions

✅ **Database Integration**
- PostgreSQL service container for realistic testing
- Separate test database for isolation

✅ **Code Quality**
- Flake8 linting for syntax and style
- Coverage reporting with Codecov integration

✅ **Automated Docker Deployment**
- Only deploys on successful tests
- Only runs on main branch pushes
- Supports multiple tags (latest, SHA, branch)

✅ **Build Optimization**
- Docker layer caching for faster builds
- Multi-stage builds for smaller images

### Workflow Jobs

#### `test` Job
Runs comprehensive test suite across multiple Python versions:
```yaml
- Lint with flake8
- Run unit tests (auth, schemas, models, operations)
- Run integration tests (users, calculator API)
- Run logging tests
- Generate coverage reports
- Upload to Codecov
- Archive test results and logs
```

#### `build-and-push` Job
Builds and publishes Docker image:
```yaml
- Checkout code
- Set up Docker Buildx
- Log in to Docker Hub
- Extract metadata (tags, labels)
- Build and push image
- Cache layers for optimization
```

#### `verify-deployment` Job
Confirms successful deployment:
```yaml
- Verify image pushed
- Display image digest
- Confirm pipeline completion
```

### Viewing CI/CD Results

1. **GitHub Actions Tab**: See workflow runs, logs, and status
2. **Commit Status**: Green checkmark or red X on commits
3. **Pull Requests**: Automatic status checks before merge
4. **Docker Hub**: View published images with tags

### Triggering Workflows

Workflows trigger automatically on:
- Push to `main` branch (full pipeline with Docker push)
- Push to `develop` branch (tests only)
- Pull requests to `main` or `develop` (tests only)

Manual trigger:
```bash
# Go to Actions tab > Select workflow > Run workflow
```

### Docker Image Tags

Images are tagged with:
- `latest`: Most recent build from main branch
- `main-<sha>`: Specific commit on main branch
- `main`: Latest main branch build

Example:
```bash
docker pull YOUR_USERNAME/fastapi-user-management:latest
docker pull YOUR_USERNAME/fastapi-user-management:main-a1b2c3d
```

### Troubleshooting CI/CD

**Tests failing in CI but passing locally?**
- Check Python version compatibility
- Verify environment variables are set
- Review PostgreSQL connection settings

**Docker push failing?**
- Verify `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` secrets
- Check Docker Hub token hasn't expired
- Ensure repository name matches Docker Hub repository

**Build taking too long?**
- Build cache should speed up subsequent builds
- First build may take 5-10 minutes
- Later builds typically 2-3 minutes

### Local Testing Before Push

Test locally before pushing:
```bash
# Run tests
pytest -v --cov=.

# Build Docker image
docker build -t fastapi-user-management:test .

# Test Docker image
docker run -p 8000:8000 fastapi-user-management:test
```

### Continuous Deployment

To add automatic deployment to a hosting platform:
1. Add deployment job to workflow
2. Configure platform credentials as secrets
3. Add deployment step after successful Docker push

Example platforms:
- AWS ECS/Fargate
- Google Cloud Run
- Azure Container Instances
- DigitalOcean App Platform
- Heroku Container Registry

## Project Structure

```
assignment10/
├── app/                        # Application package
│   ├── __init__.py             # Package initializer
│   ├── main.py                 # FastAPI application entry point
│   ├── database.py             # SQLAlchemy database configuration
│   ├── models.py               # User SQLAlchemy model
│   ├── schemas.py              # Pydantic validation schemas
│   ├── auth.py                 # Password hashing utilities
│   ├── users.py                # User management router
│   ├── operations.py           # Calculator operation functions
│   └── logger_config.py        # Logging configuration
├── tests/                      # Test suite
│   ├── __init__.py
│   ├── README.md               # Test documentation
│   ├── test_auth.py            # Password hashing tests (12 tests)
│   ├── test_schemas.py         # Pydantic schema tests (20 tests)
│   ├── test_models.py          # SQLAlchemy model tests (10 tests)
│   ├── test_users.py           # User API integration tests (18 tests)
│   ├── test_operations.py      # Calculator tests (37 tests)
│   ├── test_main.py            # Calculator API tests (37 tests)
│   ├── test_logging.py         # Logging tests (26 tests)
│   └── test_e2e.py             # End-to-end tests (Playwright)
├── docs/                       # Documentation
│   ├── CI_CD_SETUP.md          # CI/CD setup guide
│   ├── QUICK_REFERENCE.md      # Quick command reference
│   ├── SETUP_CHECKLIST.md      # Setup checklist
│   └── LOGGING.md              # Logging documentation
├── scripts/                    # Utility scripts
│   ├── run_tests.sh            # Test runner script
│   └── ci_check.sh             # CI validation script
├── static/                     # Static files
│   └── index.html              # Calculator web UI (legacy)
├── logs/                       # Log files directory
│   ├── app.log                 # Application logs
│   └── error.log               # Error logs
├── .github/
│   └── workflows/
│       └── ci.yml              # CI/CD pipeline configuration
├── requirements.txt            # Production dependencies
├── requirements-test.txt       # Test dependencies
├── pyproject.toml              # Pytest configuration
├── Dockerfile                  # Docker container configuration
├── docker-compose.yml          # Multi-container orchestration
├── .env.example                # Environment variables template
├── .dockerignore               # Docker build exclusions
├── .gitignore                  # Git exclusions
└── README.md                   # This file
```

## Environment Variables

The application uses environment variables for configuration. Copy `.env.example` to `.env` and configure:

### Required Variables

```bash
# Database Configuration
DATABASE_URL=postgresql://calculator_user:calculator_pass@db:5432/calculator_db

# PostgreSQL Configuration
POSTGRES_USER=calculator_user
POSTGRES_PASSWORD=calculator_pass
POSTGRES_DB=calculator_db
```

### Optional Variables

```bash
# Application Configuration
APP_NAME=FastAPI User Management
APP_VERSION=1.0.0
DEBUG=False

# Security (for future JWT implementation)
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS Configuration
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
```

### Docker Hub Variables (CI/CD only)

Set these as **GitHub Secrets**, not in `.env`:
```bash
DOCKERHUB_USERNAME=your-dockerhub-username
DOCKERHUB_TOKEN=your-dockerhub-access-token
```

## Security Best Practices

### Password Security
✅ **Bcrypt Hashing**
- All passwords hashed with bcrypt (cost factor 12)
- Never store plain text passwords
- Password verification uses constant-time comparison

✅ **Version Compatibility**
- Use bcrypt 4.0.1 (not 5.0.0) for passlib compatibility
- Tested across Python 3.9-3.12

### Database Security
✅ **SQLAlchemy ORM**
- Prevents SQL injection via parameterized queries
- Input validation through Pydantic schemas

✅ **Unique Constraints**
- Usernames and emails must be unique
- Database-level constraint enforcement

### API Security
✅ **Input Validation**
- Email format validation
- Username/password requirements
- Type checking with Pydantic

✅ **Error Handling**
- No sensitive information in error messages
- Proper HTTP status codes

### Docker Security
✅ **Non-root User**
- Container runs as non-root user
- Minimal attack surface

✅ **Environment Variables**
- Sensitive data via environment variables
- `.env` file gitignored

### CI/CD Security
✅ **Secrets Management**
- Docker Hub credentials in GitHub Secrets
- Never commit secrets to repository

✅ **Dependency Scanning**
- Automated dependency updates
- Regular security audits

## Deployment

### Using Docker Hub Image

Pull and run the pre-built image:
```bash
# Pull latest image
docker pull YOUR_USERNAME/fastapi-user-management:latest

# Run with environment variables
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:pass@host:5432/db \
  YOUR_USERNAME/fastapi-user-management:latest
```

### Production Deployment Checklist

- [ ] Set strong `POSTGRES_PASSWORD`
- [ ] Configure `SECRET_KEY` for JWT (future feature)
- [ ] Set `DEBUG=False`
- [ ] Configure CORS for your domain
- [ ] Set up SSL/TLS certificates
- [ ] Configure database backups
- [ ] Set up monitoring and logging
- [ ] Configure rate limiting
- [ ] Set up health checks

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest -v`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- FastAPI framework by Sebastián Ramírez
- SQLAlchemy ORM
- Pydantic validation library
- bcrypt password hashing
- PostgreSQL database
- Docker containerization
- GitHub Actions CI/CD

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review test examples

## Changelog

### Version 1.0.0 (Current)
- ✅ User management system with SQLAlchemy
- ✅ Secure password hashing with bcrypt
- ✅ Comprehensive test suite (60+ tests)
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Docker Hub automated deployment
- ✅ PostgreSQL database integration
- ✅ Calculator API (legacy feature)
- ✅ 75% test coverage

### Future Enhancements
- [ ] JWT authentication
- [ ] User roles and permissions
- [ ] Password reset functionality
- [ ] Email verification
- [ ] Rate limiting
- [ ] API versioning
- [ ] Swagger UI customization
- [ ] Monitoring and metrics
