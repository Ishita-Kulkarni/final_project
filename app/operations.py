"""
Calculator operations module
Contains all arithmetic calculation functions
"""
from app.logger_config import get_logger

# Initialize logger
logger = get_logger(__name__)


class DivisionByZeroError(Exception):
    """Custom exception for division by zero"""
    pass


class InvalidOperationError(Exception):
    """Custom exception for invalid operations"""
    pass


def add(num1: float, num2: float) -> float:
    """
    Add two numbers
    
    Args:
        num1: First number
        num2: Second number
        
    Returns:
        Sum of num1 and num2
    """
    logger.debug(f"Addition: {num1} + {num2}")
    result = num1 + num2
    logger.debug(f"Addition result: {result}")
    return result


def subtract(num1: float, num2: float) -> float:
    """
    Subtract second number from first number
    
    Args:
        num1: First number
        num2: Second number
        
    Returns:
        Difference of num1 and num2
    """
    logger.debug(f"Subtraction: {num1} - {num2}")
    result = num1 - num2
    logger.debug(f"Subtraction result: {result}")
    return result


def multiply(num1: float, num2: float) -> float:
    """
    Multiply two numbers
    
    Args:
        num1: First number
        num2: Second number
        
    Returns:
        Product of num1 and num2
    """
    logger.debug(f"Multiplication: {num1} * {num2}")
    result = num1 * num2
    logger.debug(f"Multiplication result: {result}")
    return result


def divide(num1: float, num2: float) -> float:
    """
    Divide first number by second number
    
    Args:
        num1: Numerator
        num2: Denominator
        
    Returns:
        Quotient of num1 and num2
        
    Raises:
        DivisionByZeroError: If num2 is zero
    """
    logger.debug(f"Division: {num1} / {num2}")
    if num2 == 0:
        logger.error(f"Division by zero attempted: {num1} / {num2}")
        raise DivisionByZeroError("Cannot divide by zero")
    result = num1 / num2
    logger.debug(f"Division result: {result}")
    return result


def calculate(num1: float, num2: float, operation: str) -> float:
    """
    Perform a calculation based on the operation
    
    Args:
        num1: First number
        num2: Second number
        operation: Operation to perform (add, subtract, multiply, divide)
        
    Returns:
        Result of the calculation
        
    Raises:
        InvalidOperationError: If operation is not supported
        DivisionByZeroError: If dividing by zero
    """
    operation = operation.lower()
    logger.info(f"Calculate called: num1={num1}, num2={num2}, operation={operation}")
    
    operations_map = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    
    if operation not in operations_map:
        logger.error(f"Invalid operation requested: {operation}")
        raise InvalidOperationError(
            f"Invalid operation: {operation}. "
            f"Supported operations: {', '.join(operations_map.keys())}"
        )
    
    try:
        result = operations_map[operation](num1, num2)
        logger.info(f"Calculation successful: {num1} {operation} {num2} = {result}")
        return result
    except DivisionByZeroError as e:
        logger.error(f"Division by zero error: {num1} / {num2}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during calculation: {e}", exc_info=True)
        raise
