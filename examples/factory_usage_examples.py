"""
Example usage of the Calculation Factory Pattern

This file demonstrates how to use and extend the CalculationFactory.
"""

from app.calculation_factory import (
    CalculationFactory,
    CalculationStrategy,
    PowerStrategy,
    ModuloStrategy
)
from app.logger_config import get_logger

logger = get_logger(__name__)


# ============================================================================
# Example 1: Basic Usage with Built-in Operations
# ============================================================================

def basic_calculations():
    """Demonstrate basic calculator operations using the factory."""
    
    # Addition
    result = CalculationFactory.calculate(10, 5, "add")
    print(f"10 + 5 = {result}")  # 15.0
    
    # Subtraction
    result = CalculationFactory.calculate(10, 5, "subtract")
    print(f"10 - 5 = {result}")  # 5.0
    
    # Multiplication
    result = CalculationFactory.calculate(10, 5, "multiply")
    print(f"10 * 5 = {result}")  # 50.0
    
    # Division
    result = CalculationFactory.calculate(10, 5, "divide")
    print(f"10 / 5 = {result}")  # 2.0


# ============================================================================
# Example 2: Error Handling
# ============================================================================

def error_handling():
    """Demonstrate error handling in calculations."""
    from app.operations import DivisionByZeroError
    
    try:
        result = CalculationFactory.calculate(10, 0, "divide")
    except DivisionByZeroError as e:
        print(f"Error: {e}")
    
    try:
        result = CalculationFactory.calculate(10, 5, "invalid_op")
    except ValueError as e:
        print(f"Error: {e}")


# ============================================================================
# Example 3: Extending with New Operations
# ============================================================================

def register_power_operation():
    """Register and use the power operation."""
    
    # Register the power strategy
    CalculationFactory.register_strategy("power", PowerStrategy)
    
    # Use it
    result = CalculationFactory.calculate(2, 3, "power")
    print(f"2 ^ 3 = {result}")  # 8.0


def register_modulo_operation():
    """Register and use the modulo operation."""
    
    # Register the modulo strategy
    CalculationFactory.register_strategy("modulo", ModuloStrategy)
    
    # Use it
    result = CalculationFactory.calculate(10, 3, "modulo")
    print(f"10 % 3 = {result}")  # 1.0


# ============================================================================
# Example 4: Creating Custom Operations
# ============================================================================

class SquareRootStrategy(CalculationStrategy):
    """Custom strategy for square root (uses only first operand)."""
    
    def execute(self, a: float, b: float) -> float:
        """Calculate square root of a (b is ignored)."""
        import math
        logger.debug(f"Square root: √{a}")
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        result = math.sqrt(a)
        logger.debug(f"Square root result: {result}")
        return result
    
    def get_operation_name(self) -> str:
        return "sqrt"


class MaxStrategy(CalculationStrategy):
    """Custom strategy for finding maximum of two numbers."""
    
    def execute(self, a: float, b: float) -> float:
        """Return the maximum of a and b."""
        logger.debug(f"Max: max({a}, {b})")
        result = max(a, b)
        logger.debug(f"Max result: {result}")
        return result
    
    def get_operation_name(self) -> str:
        return "max"


class MinStrategy(CalculationStrategy):
    """Custom strategy for finding minimum of two numbers."""
    
    def execute(self, a: float, b: float) -> float:
        """Return the minimum of a and b."""
        logger.debug(f"Min: min({a}, {b})")
        result = min(a, b)
        logger.debug(f"Min result: {result}")
        return result
    
    def get_operation_name(self) -> str:
        return "min"


def custom_operations():
    """Demonstrate custom operation registration and usage."""
    
    # Register custom operations
    CalculationFactory.register_strategy("sqrt", SquareRootStrategy)
    CalculationFactory.register_strategy("max", MaxStrategy)
    CalculationFactory.register_strategy("min", MinStrategy)
    
    # Use them
    result = CalculationFactory.calculate(16, 0, "sqrt")
    print(f"√16 = {result}")  # 4.0
    
    result = CalculationFactory.calculate(10, 20, "max")
    print(f"max(10, 20) = {result}")  # 20.0
    
    result = CalculationFactory.calculate(10, 20, "min")
    print(f"min(10, 20) = {result}")  # 10.0


# ============================================================================
# Example 5: Querying Available Operations
# ============================================================================

def list_operations():
    """List all registered operations."""
    operations = CalculationFactory.get_supported_operations()
    print("Supported operations:")
    for op in operations:
        print(f"  - {op}")


# ============================================================================
# Example 6: Using Strategies Directly
# ============================================================================

def direct_strategy_usage():
    """Use strategies directly without the factory."""
    from app.calculation_factory import AdditionStrategy
    
    strategy = AdditionStrategy()
    result = strategy.execute(10, 5)
    print(f"Direct strategy result: {result}")
    print(f"Operation name: {strategy.get_operation_name()}")


# ============================================================================
# Example 7: Integration with Calculation Model
# ============================================================================

def save_calculation_to_database(db, user_id: int, a: float, b: float, operation: str):
    """
    Calculate and save to database.
    
    This demonstrates how to use the factory with the Calculation model.
    """
    from app.models import Calculation
    
    # Calculate using factory
    result = CalculationFactory.calculate(a, b, operation)
    
    # Create model instance
    calculation = Calculation(
        user_id=user_id,
        a=a,
        b=b,
        type=operation,
        result=result
    )
    
    # Save to database
    db.add(calculation)
    db.commit()
    db.refresh(calculation)
    
    return calculation


# ============================================================================
# Example 8: Validation with Pydantic
# ============================================================================

def validated_calculation():
    """Use Pydantic schema for validation before calculation."""
    from app.schemas import CalculationCreate
    from pydantic import ValidationError
    
    # Valid calculation
    try:
        calc_data = CalculationCreate(a=10.0, b=5.0, type="add")
        result = CalculationFactory.calculate(
            calc_data.a, 
            calc_data.b, 
            calc_data.type
        )
        print(f"Result: {result}")
    except ValidationError as e:
        print(f"Validation error: {e}")
    
    # Invalid calculation (division by zero)
    try:
        calc_data = CalculationCreate(a=10.0, b=0.0, type="divide")
    except ValidationError as e:
        print(f"Caught validation error: Division by zero prevented!")


# ============================================================================
# Main execution
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Calculation Factory Examples")
    print("=" * 60)
    
    print("\n1. Basic Calculations:")
    print("-" * 60)
    basic_calculations()
    
    print("\n2. Error Handling:")
    print("-" * 60)
    error_handling()
    
    print("\n3. Extended Operations (Power):")
    print("-" * 60)
    register_power_operation()
    
    print("\n4. Extended Operations (Modulo):")
    print("-" * 60)
    register_modulo_operation()
    
    print("\n5. Custom Operations:")
    print("-" * 60)
    custom_operations()
    
    print("\n6. List All Operations:")
    print("-" * 60)
    list_operations()
    
    print("\n7. Direct Strategy Usage:")
    print("-" * 60)
    direct_strategy_usage()
    
    print("\n8. Validated Calculation:")
    print("-" * 60)
    validated_calculation()
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
