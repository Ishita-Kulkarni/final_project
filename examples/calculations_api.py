"""
Example API endpoints for the Calculation model.

This file shows how to integrate the Calculation model with FastAPI endpoints.
You can add these to app/main.py or create a separate calculations router.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Calculation, User
from app.schemas import CalculationCreate, CalculationResponse, CalculationUpdate
from app.calculation_factory import CalculationFactory
from app.operations import DivisionByZeroError
from app.logger_config import get_logger

logger = get_logger(__name__)

# Create router
router = APIRouter(
    prefix="/calculations",
    tags=["calculations"]
)


# ============================================================================
# Helper function to get current user (placeholder - implement with auth)
# ============================================================================

def get_current_user(db: Session = Depends(get_db)) -> User:
    """
    Get the current authenticated user.
    Replace this with actual authentication logic.
    """
    # This is a placeholder - in production, use JWT tokens or sessions
    # For now, return the first user in the database
    user = db.query(User).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No authenticated user found"
        )
    return user


# ============================================================================
# CREATE - Add a new calculation
# ============================================================================

@router.post("/", response_model=CalculationResponse, status_code=status.HTTP_201_CREATED)
def create_calculation(
    calculation: CalculationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create a new calculation and save it to the database.
    
    - **a**: First operand
    - **b**: Second operand
    - **type**: Operation type (add, subtract, multiply, divide)
    
    Returns the calculation with computed result.
    """
    logger.info(f"User {current_user.id} creating calculation: {calculation.a} {calculation.type} {calculation.b}")
    
    try:
        # Calculate result using factory
        result = CalculationFactory.calculate(
            calculation.a,
            calculation.b,
            calculation.type
        )
        
        # Create database record
        db_calculation = Calculation(
            user_id=current_user.id,
            a=calculation.a,
            b=calculation.b,
            type=calculation.type,
            result=result
        )
        
        db.add(db_calculation)
        db.commit()
        db.refresh(db_calculation)
        
        logger.info(f"Calculation created successfully: ID {db_calculation.id}, Result: {result}")
        return db_calculation
        
    except DivisionByZeroError:
        logger.error(f"Division by zero attempted by user {current_user.id}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Division by zero is not allowed"
        )
    except ValueError as e:
        logger.error(f"Invalid operation: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Unexpected error creating calculation: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your calculation"
        )


# ============================================================================
# READ - Get all calculations for current user
# ============================================================================

@router.get("/", response_model=List[CalculationResponse])
def get_calculations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retrieve all calculations for the current user.
    
    - **skip**: Number of records to skip (for pagination)
    - **limit**: Maximum number of records to return
    """
    logger.info(f"User {current_user.id} retrieving calculations (skip={skip}, limit={limit})")
    
    calculations = db.query(Calculation)\
        .filter(Calculation.user_id == current_user.id)\
        .order_by(Calculation.created_at.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()
    
    logger.info(f"Retrieved {len(calculations)} calculations for user {current_user.id}")
    return calculations


# ============================================================================
# READ - Get a specific calculation
# ============================================================================

@router.get("/{calculation_id}", response_model=CalculationResponse)
def get_calculation(
    calculation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retrieve a specific calculation by ID.
    
    Only returns calculations belonging to the current user.
    """
    logger.info(f"User {current_user.id} retrieving calculation {calculation_id}")
    
    calculation = db.query(Calculation)\
        .filter(
            Calculation.id == calculation_id,
            Calculation.user_id == current_user.id
        )\
        .first()
    
    if not calculation:
        logger.warning(f"Calculation {calculation_id} not found for user {current_user.id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Calculation with ID {calculation_id} not found"
        )
    
    return calculation


# ============================================================================
# UPDATE - Modify an existing calculation
# ============================================================================

@router.put("/{calculation_id}", response_model=CalculationResponse)
def update_calculation(
    calculation_id: int,
    calculation_update: CalculationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update an existing calculation.
    
    Recalculates the result based on updated values.
    """
    logger.info(f"User {current_user.id} updating calculation {calculation_id}")
    
    # Get existing calculation
    db_calculation = db.query(Calculation)\
        .filter(
            Calculation.id == calculation_id,
            Calculation.user_id == current_user.id
        )\
        .first()
    
    if not db_calculation:
        logger.warning(f"Calculation {calculation_id} not found for user {current_user.id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Calculation with ID {calculation_id} not found"
        )
    
    # Update fields
    update_data = calculation_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_calculation, field, value)
    
    try:
        # Recalculate result
        result = CalculationFactory.calculate(
            db_calculation.a,
            db_calculation.b,
            db_calculation.type
        )
        db_calculation.result = result
        
        db.commit()
        db.refresh(db_calculation)
        
        logger.info(f"Calculation {calculation_id} updated successfully")
        return db_calculation
        
    except DivisionByZeroError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Division by zero is not allowed"
        )
    except ValueError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# ============================================================================
# DELETE - Remove a calculation
# ============================================================================

@router.delete("/{calculation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_calculation(
    calculation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Delete a calculation.
    
    Only allows deletion of calculations belonging to the current user.
    """
    logger.info(f"User {current_user.id} deleting calculation {calculation_id}")
    
    db_calculation = db.query(Calculation)\
        .filter(
            Calculation.id == calculation_id,
            Calculation.user_id == current_user.id
        )\
        .first()
    
    if not db_calculation:
        logger.warning(f"Calculation {calculation_id} not found for user {current_user.id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Calculation with ID {calculation_id} not found"
        )
    
    db.delete(db_calculation)
    db.commit()
    
    logger.info(f"Calculation {calculation_id} deleted successfully")
    return None


# ============================================================================
# STATISTICS - Get calculation statistics for user
# ============================================================================

@router.get("/stats/summary")
def get_calculation_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get statistics about user's calculations.
    
    Returns count by operation type and other useful metrics.
    """
    from sqlalchemy import func
    
    logger.info(f"User {current_user.id} retrieving calculation statistics")
    
    # Count by operation type
    stats = db.query(
        Calculation.type,
        func.count(Calculation.id).label('count'),
        func.avg(Calculation.result).label('average_result'),
        func.min(Calculation.result).label('min_result'),
        func.max(Calculation.result).label('max_result')
    ).filter(
        Calculation.user_id == current_user.id
    ).group_by(
        Calculation.type
    ).all()
    
    # Total calculations
    total = db.query(func.count(Calculation.id))\
        .filter(Calculation.user_id == current_user.id)\
        .scalar()
    
    return {
        "total_calculations": total,
        "by_operation": [
            {
                "operation": stat.type,
                "count": stat.count,
                "average_result": float(stat.average_result) if stat.average_result else None,
                "min_result": float(stat.min_result) if stat.min_result else None,
                "max_result": float(stat.max_result) if stat.max_result else None,
            }
            for stat in stats
        ]
    }


# ============================================================================
# How to integrate this router into main.py:
# ============================================================================

"""
In app/main.py, add:

from app.calculations_api import router as calculations_router

app.include_router(calculations_router)

Then your API will have these endpoints:

POST   /calculations/              - Create calculation
GET    /calculations/              - List user's calculations
GET    /calculations/{id}          - Get specific calculation
PUT    /calculations/{id}          - Update calculation
DELETE /calculations/{id}          - Delete calculation
GET    /calculations/stats/summary - Get statistics

Example API calls:

# Create calculation
curl -X POST "http://localhost:8000/calculations/" \
  -H "Content-Type: application/json" \
  -d '{"a": 10.5, "b": 5.2, "type": "add"}'

# Get all calculations
curl "http://localhost:8000/calculations/"

# Get specific calculation
curl "http://localhost:8000/calculations/1"

# Update calculation
curl -X PUT "http://localhost:8000/calculations/1" \
  -H "Content-Type: application/json" \
  -d '{"a": 20.0, "b": 10.0, "type": "multiply"}'

# Delete calculation
curl -X DELETE "http://localhost:8000/calculations/1"

# Get statistics
curl "http://localhost:8000/calculations/stats/summary"
"""
