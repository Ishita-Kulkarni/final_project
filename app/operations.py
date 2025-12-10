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


class NegativeRootError(Exception):
    """Custom exception for square root of negative numbers"""
    pass


class InvalidExponentError(Exception):
    """Custom exception for invalid exponent operations"""
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


def power(num1: float, num2: float) -> float:
    """
    Raise first number to the power of second number
    
    Args:
        num1: Base number
        num2: Exponent
        
    Returns:
        num1 raised to the power of num2
        
    Raises:
        InvalidExponentError: If result would be too large or invalid
    """
    logger.debug(f"Power: {num1} ** {num2}")
    try:
        # Check for potential overflow
        if abs(num1) > 1 and num2 > 1000:
            logger.error(f"Exponent too large: {num1} ** {num2}")
            raise InvalidExponentError("Exponent too large, result would overflow")
        
        result = num1 ** num2
        
        # Check if result is infinity or NaN
        if not (-float('inf') < result < float('inf')):
            logger.error(f"Power operation resulted in infinity: {num1} ** {num2}")
            raise InvalidExponentError("Result is too large (overflow)")
        
        logger.debug(f"Power result: {result}")
        return result
    except OverflowError:
        logger.error(f"Overflow error in power operation: {num1} ** {num2}")
        raise InvalidExponentError("Result is too large (overflow)")
    except Exception as e:
        logger.error(f"Error in power operation: {e}")
        raise


def modulus(num1: float, num2: float) -> float:
    """
    Calculate modulus (remainder) of num1 divided by num2
    
    Args:
        num1: Dividend
        num2: Divisor
        
    Returns:
        Remainder of num1 / num2
        
    Raises:
        DivisionByZeroError: If num2 is zero
    """
    logger.debug(f"Modulus: {num1} % {num2}")
    if num2 == 0:
        logger.error(f"Modulus by zero attempted: {num1} % {num2}")
        raise DivisionByZeroError("Cannot calculate modulus with zero divisor")
    result = num1 % num2
    logger.debug(f"Modulus result: {result}")
    return result


def square_root(num1: float, num2: float = 0) -> float:
    """
    Calculate square root of num1 (num2 is ignored for compatibility)
    
    Args:
        num1: Number to find square root of
        num2: Ignored (kept for API compatibility)
        
    Returns:
        Square root of num1
        
    Raises:
        NegativeRootError: If num1 is negative
    """
    logger.debug(f"Square root: √{num1}")
    if num1 < 0:
        logger.error(f"Square root of negative number attempted: √{num1}")
        raise NegativeRootError("Cannot calculate square root of negative number")
    result = num1 ** 0.5
    logger.debug(f"Square root result: {result}")
    return result


def nth_root(num1: float, num2: float) -> float:
    """
    Calculate nth root of num1 where n is num2
    
    Args:
        num1: Number to find root of
        num2: Root degree (n)
        
    Returns:
        nth root of num1
        
    Raises:
        DivisionByZeroError: If num2 is zero
        NegativeRootError: If num1 is negative and num2 is even
        InvalidExponentError: If operation is invalid
    """
    logger.debug(f"Nth root: {num1} ^ (1/{num2})")
    
    if num2 == 0:
        logger.error(f"Zeroth root attempted: {num1} ^ (1/0)")
        raise DivisionByZeroError("Cannot calculate zeroth root (division by zero)")
    
    # Check for negative number with even root
    if num1 < 0 and num2 % 2 == 0:
        logger.error(f"Even root of negative number attempted: {num1} ^ (1/{num2})")
        raise NegativeRootError(f"Cannot calculate even root of negative number")
    
    try:
        # For negative numbers with odd roots, use special handling
        if num1 < 0:
            result = -(abs(num1) ** (1 / num2))
        else:
            result = num1 ** (1 / num2)
        
        logger.debug(f"Nth root result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in nth root operation: {e}")
        raise InvalidExponentError(f"Invalid nth root operation: {e}")


def calculate(num1: float, num2: float, operation: str) -> float:
    """
    Perform a calculation based on the operation
    
    Args:
        num1: First number
        num2: Second number
        operation: Operation to perform (add, subtract, multiply, divide, power, modulus, square_root, nth_root)
        
    Returns:
        Result of the calculation
        
    Raises:
        InvalidOperationError: If operation is not supported
        DivisionByZeroError: If dividing by zero or modulus by zero
        NegativeRootError: If taking square root of negative number
        InvalidExponentError: If power operation is invalid
    """
    operation = operation.lower()
    logger.info(f"Calculate called: num1={num1}, num2={num2}, operation={operation}")
    
    operations_map = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "power": power,
        "modulus": modulus,
        "square_root": square_root,
        "nth_root": nth_root
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
    except (DivisionByZeroError, NegativeRootError, InvalidExponentError) as e:
        logger.error(f"Operation error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during calculation: {e}", exc_info=True)
        raise
