# Calculation Model Examples

This directory contains example code demonstrating how to use the Calculation model, factory pattern, and API endpoints.

## Files

### 1. `factory_usage_examples.py`
Complete examples of using the CalculationFactory pattern.

**What it demonstrates:**
- Basic calculator operations (add, subtract, multiply, divide)
- Error handling for division by zero and invalid operations
- Extending the factory with new operations (power, modulo)
- Creating custom operations (square root, max, min)
- Querying available operations
- Direct strategy usage
- Integration with Calculation model
- Pydantic validation

**How to run:**
```bash
cd /home/ishit/calculation_model
python examples/factory_usage_examples.py
```

**Expected output:**
```
============================================================
Calculation Factory Examples
============================================================

1. Basic Calculations:
------------------------------------------------------------
10 + 5 = 15.0
10 - 5 = 5.0
10 * 5 = 50.0
10 / 5 = 2.0

2. Error Handling:
------------------------------------------------------------
Error: Cannot divide by zero
Error: Unsupported operation type: invalid_op

[... more examples ...]
```

### 2. `calculations_api.py`
Example REST API endpoints for the Calculation model.

**What it demonstrates:**
- CRUD operations for calculations
- RESTful API design
- Authentication integration
- Error handling in API endpoints
- Pagination
- Statistics endpoint
- Proper HTTP status codes
- Request/response validation

**Endpoints provided:**
- `POST /calculations/` - Create new calculation
- `GET /calculations/` - List user's calculations
- `GET /calculations/{id}` - Get specific calculation
- `PUT /calculations/{id}` - Update calculation
- `DELETE /calculations/{id}` - Delete calculation
- `GET /calculations/stats/summary` - Get statistics

**How to integrate:**
1. Copy the router to your app
2. Add to `app/main.py`:
   ```python
   from examples.calculations_api import router as calculations_router
   app.include_router(calculations_router)
   ```
3. Run your FastAPI app:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Visit http://localhost:8000/docs to see interactive API documentation

**Example API calls:**

Create a calculation:
```bash
curl -X POST "http://localhost:8000/calculations/" \
  -H "Content-Type: application/json" \
  -d '{"a": 10.5, "b": 5.2, "type": "add"}'
```

Get all calculations:
```bash
curl "http://localhost:8000/calculations/"
```

Get statistics:
```bash
curl "http://localhost:8000/calculations/stats/summary"
```

## Quick Start Guide

### 1. Basic Usage

```python
from app.calculation_factory import CalculationFactory

# Simple calculation
result = CalculationFactory.calculate(10, 5, "add")
print(f"Result: {result}")  # 15.0
```

### 2. With Database

```python
from app.models import Calculation
from app.calculation_factory import CalculationFactory
from app.database import SessionLocal

db = SessionLocal()
user_id = 1  # Your user ID

# Calculate and save
result = CalculationFactory.calculate(10, 5, "multiply")
calculation = Calculation(
    user_id=user_id,
    a=10,
    b=5,
    type="multiply",
    result=result
)
db.add(calculation)
db.commit()
```

### 3. With Validation

```python
from app.schemas import CalculationCreate
from pydantic import ValidationError

try:
    # This will validate inputs
    calc = CalculationCreate(a=10, b=0, type="divide")
except ValidationError as e:
    print(f"Validation failed: {e}")
```

### 4. Extending with New Operations

```python
from app.calculation_factory import CalculationFactory, CalculationStrategy

class PowerStrategy(CalculationStrategy):
    def execute(self, a: float, b: float) -> float:
        return a ** b
    
    def get_operation_name(self) -> str:
        return "power"

# Register it
CalculationFactory.register_strategy("power", PowerStrategy)

# Use it
result = CalculationFactory.calculate(2, 3, "power")  # 8.0
```

## Testing

All examples are tested in the test suite:

```bash
# Run calculation tests
pytest tests/test_calculations.py -v

# Run with coverage
pytest tests/test_calculations.py -v --cov=app.calculation_factory --cov=app.models --cov=app.schemas
```

## Common Use Cases

### Use Case 1: Calculator History
Store all user calculations for history/audit trail:
```python
# User performs calculation
result = CalculationFactory.calculate(a, b, operation)

# Save to database
calc = Calculation(user_id=user_id, a=a, b=b, type=operation, result=result)
db.add(calc)
db.commit()

# Later: retrieve history
history = db.query(Calculation).filter(Calculation.user_id == user_id).all()
```

### Use Case 2: Calculation as a Service
Expose calculations via REST API:
```python
@app.post("/calculate/")
def calculate_endpoint(calc: CalculationCreate, current_user: User):
    result = CalculationFactory.calculate(calc.a, calc.b, calc.type)
    return {"result": result}
```

### Use Case 3: Bulk Calculations
Process multiple calculations:
```python
calculations = [
    {"a": 10, "b": 5, "type": "add"},
    {"a": 20, "b": 4, "type": "multiply"},
    {"a": 100, "b": 10, "type": "divide"}
]

results = []
for calc_data in calculations:
    result = CalculationFactory.calculate(**calc_data)
    results.append(result)
```

### Use Case 4: Custom Operations
Add domain-specific operations:
```python
class PercentageStrategy(CalculationStrategy):
    def execute(self, a: float, b: float) -> float:
        """Calculate a% of b"""
        return (a / 100) * b
    
    def get_operation_name(self) -> str:
        return "percentage"

CalculationFactory.register_strategy("percentage", PercentageStrategy)
result = CalculationFactory.calculate(15, 200, "percentage")  # 30.0
```

## Best Practices

1. **Always use Pydantic validation** before creating calculations
2. **Handle errors gracefully** - catch DivisionByZeroError and ValueError
3. **Log operations** - use the logger for audit trail
4. **Store results** - don't recalculate, store for performance
5. **Use transactions** - wrap database operations in try/except with rollback
6. **Validate user ownership** - ensure users can only access their calculations
7. **Use the factory** - don't call operation functions directly
8. **Test new strategies** - write tests for any custom operations

## Troubleshooting

### Division by Zero Error
```python
try:
    result = CalculationFactory.calculate(10, 0, "divide")
except DivisionByZeroError:
    # Handle error
    print("Cannot divide by zero")
```

### Invalid Operation
```python
try:
    result = CalculationFactory.calculate(10, 5, "invalid")
except ValueError as e:
    # Handle error
    print(f"Invalid operation: {e}")
```

### Validation Error
```python
from pydantic import ValidationError

try:
    calc = CalculationCreate(a=10, b=0, type="divide")
except ValidationError as e:
    # Handle validation error
    print(f"Validation failed: {e}")
```

## Further Reading

- See `IMPLEMENTATION_SUMMARY.md` for detailed implementation notes
- See `tests/test_calculations.py` for comprehensive test examples
- See FastAPI documentation: https://fastapi.tiangolo.com/
- See Pydantic documentation: https://docs.pydantic.dev/
- See SQLAlchemy documentation: https://docs.sqlalchemy.org/
