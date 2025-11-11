# FastAPI Calculator with Docker & PostgreSQL

[![CI](https://github.com/Ishita-Kulkarni/assignment_8/workflows/FastAPI%20Calculator%20CI/badge.svg)](https://github.com/Ishita-Kulkarni/assignment_8/actions)
[![Code Quality](https://github.com/Ishita-Kulkarni/assignment_8/workflows/Code%20Quality%20&%20Security/badge.svg)](https://github.com/Ishita-Kulkarni/assignment_8/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://github.com/Ishita-Kulkarni/assignment_8)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)

A beautiful, interactive calculator web application built with FastAPI that performs basic arithmetic operations. Features a modern UI with real-time calculations, comprehensive API backend, and full Docker + PostgreSQL integration with pgAdmin.

## Features

🧮 **Web Calculator Interface**
- Beautiful, responsive web UI
- Real-time calculations
- Support for all arithmetic operations
- Keyboard support (Enter to calculate)
- Error handling with user-friendly messages

🔧 **API Backend**
- RESTful API for calculations
- Addition, Subtraction, Multiplication, Division
- Zero-division error handling
- Interactive API documentation (Swagger UI)
- Input validation with Pydantic
- Comprehensive logging

🐳 **Docker & Database Integration**
- Docker Compose setup with FastAPI + PostgreSQL + pgAdmin
- PostgreSQL database for data persistence
- pgAdmin for database management
- Pre-configured SQL scripts for database setup
- Multi-container orchestration

## Quick Start with Docker

### Prerequisites
- Docker Desktop installed and running
- Git

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Ishita-Kulkarni/assignment_8.git
cd assignment_8
```

2. Start all services with Docker Compose:
```bash
docker compose up --build
```

3. Access the services:
   - **FastAPI Calculator**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs
   - **pgAdmin**: http://localhost:5050
   - **PostgreSQL**: localhost:5432

### pgAdmin Login
- Email: `admin@calculator.com`
- Password: `admin`

### Database Connection (in pgAdmin)
- Host: `postgres`
- Port: `5432`
- Database: `calculator_db`
- Username: `calculator_user`
- Password: `calculator_pass`

For detailed Docker setup instructions, see [DOCKER_SETUP.md](DOCKER_SETUP.md)

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

### GET /
Returns a welcome message and available endpoints.

### POST /calculate
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

### GET /health
Health check endpoint.

## Example Usage

Using curl:
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

The project includes comprehensive tests:

### Test Categories
- **Unit Tests** (`tests/test_operations.py`): 37 tests for calculator functions
- **Integration Tests** (`tests/test_main.py`): 37 tests for API endpoints
- **End-to-End Tests** (`tests/test_e2e.py`): Playwright tests for user interactions

### Running Tests

Install test dependencies:
```bash
pip install -r requirements-test.txt
playwright install chromium
```

Run all tests:
```bash
./run_tests.sh
```

Or run specific test categories:
```bash
# Unit tests only
pytest tests/test_operations.py -v

# Integration tests only
pytest tests/test_main.py -v

# E2E tests (requires server running)
pytest tests/test_e2e.py -v

# All tests with coverage
pytest --cov=. --cov-report=html
```

### Test Coverage
The test suite achieves 100% code coverage on both `operations.py` and `main.py`.

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

## Continuous Integration

The project uses GitHub Actions for automated testing and quality checks.

### Workflows
- **CI Pipeline**: Runs tests on Python 3.9, 3.10, 3.11, and 3.12
- **Code Quality**: Linting, formatting, and security checks
- **Deployment**: Automated deployment on release

### What Gets Tested in CI
✅ Unit tests (37 tests)  
✅ Integration tests (37 tests)  
✅ Logging tests (26 tests)  
✅ Code coverage (100% on core modules)  
✅ Code linting and formatting  
✅ Security vulnerability scanning  

**Note**: E2E tests are available but run separately due to browser dependencies. Run locally with `pytest tests/test_e2e.py -v`  

### CI Status
Check the [Actions tab](https://github.com/Ishita-Kulkarni/assignment_8/actions) for workflow status and results.

For detailed CI/CD documentation, see [CI_CD.md](CI_CD.md)

## Project Structure

```
fastapi_calculator/
├── main.py                 # FastAPI application with endpoints
├── operations.py           # Calculator operation functions
├── logger_config.py        # Logging configuration
├── requirements.txt        # Production dependencies
├── requirements-test.txt   # Test dependencies
├── pyproject.toml         # Pytest configuration
├── run_tests.sh           # Test runner script
├── Dockerfile             # Docker container configuration
├── docker-compose.yml     # Multi-container orchestration
├── .env                   # Environment variables
├── .dockerignore          # Docker build exclusions
├── DOCKER_SETUP.md        # Docker setup guide
├── LOGGING.md             # Logging documentation
├── static/                # Static files (web interface)
│   └── index.html         # Calculator web UI
├── sql/                   # SQL scripts for database setup
│   ├── README.md          # SQL documentation
│   ├── 01_create_tables.sql    # Create database tables
│   ├── 02_insert_records.sql   # Insert sample data
│   ├── 03_query_data.sql       # Query examples
│   ├── 04_update_record.sql    # Update examples
│   ├── 05_delete_record.sql    # Delete examples
│   └── complete_setup.sql      # Complete setup script
├── logs/                  # Log files directory
│   ├── app.log            # Application logs
│   └── error.log          # Error logs
├── .github/               # GitHub Actions workflows
│   └── workflows/
│       ├── ci.yml         # CI pipeline
│       ├── code-quality.yml  # Code quality checks
│       ├── e2e-tests.yml  # E2E tests (optional)
│       └── deploy.yml     # Deployment workflow
├── tests/
│   ├── __init__.py
│   ├── test_operations.py # Unit tests
│   ├── test_main.py       # Integration tests
│   ├── test_e2e.py        # End-to-end tests
│   ├── test_logging.py    # Logging tests
│   └── README.md          # Test documentation
└── README.md              # This file
```
