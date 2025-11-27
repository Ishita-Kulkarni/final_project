"""
Factory pattern for calculation operations.
Provides extensibility for adding new calculation types.
"""
from abc import ABC, abstractmethod
from typing import Dict, Type
from app.operations import add, subtract, multiply, divide, DivisionByZeroError
from app.logger_config import get_logger

logger = get_logger(__name__)


class CalculationStrategy(ABC):
    """Abstract base class for calculation strategies."""
    
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """
        Execute the calculation.
        
        Args:
            a: First operand
            b: Second operand
            
        Returns:
            Result of the calculation
        """
        pass
    
    @abstractmethod
    def get_operation_name(self) -> str:
        """Return the name of the operation."""
        pass


class AdditionStrategy(CalculationStrategy):
    """Strategy for addition operations."""
    
    def execute(self, a: float, b: float) -> float:
        """Perform addition."""
        return add(a, b)
    
    def get_operation_name(self) -> str:
        return "add"


class SubtractionStrategy(CalculationStrategy):
    """Strategy for subtraction operations."""
    
    def execute(self, a: float, b: float) -> float:
        """Perform subtraction."""
        return subtract(a, b)
    
    def get_operation_name(self) -> str:
        return "subtract"


class MultiplicationStrategy(CalculationStrategy):
    """Strategy for multiplication operations."""
    
    def execute(self, a: float, b: float) -> float:
        """Perform multiplication."""
        return multiply(a, b)
    
    def get_operation_name(self) -> str:
        return "multiply"


class DivisionStrategy(CalculationStrategy):
    """Strategy for division operations."""
    
    def execute(self, a: float, b: float) -> float:
        """Perform division."""
        return divide(a, b)
    
    def get_operation_name(self) -> str:
        return "divide"


class CalculationFactory:
    """
    Factory class for creating calculation strategies.
    Implements the Factory pattern for extensibility.
    """
    
    _strategies: Dict[str, Type[CalculationStrategy]] = {
        "add": AdditionStrategy,
        "subtract": SubtractionStrategy,
        "multiply": MultiplicationStrategy,
        "divide": DivisionStrategy,
    }
    
    @classmethod
    def register_strategy(cls, operation_type: str, strategy_class: Type[CalculationStrategy]) -> None:
        """
        Register a new calculation strategy.
        Allows extending the factory with new operation types.
        
        Args:
            operation_type: Name of the operation (e.g., 'power', 'modulo')
            strategy_class: Strategy class to handle the operation
        """
        logger.info(f"Registering new calculation strategy: {operation_type}")
        cls._strategies[operation_type] = strategy_class
    
    @classmethod
    def get_strategy(cls, operation_type: str) -> CalculationStrategy:
        """
        Get a calculation strategy instance based on operation type.
        
        Args:
            operation_type: Type of operation (add, subtract, multiply, divide)
            
        Returns:
            Instance of the appropriate calculation strategy
            
        Raises:
            ValueError: If operation type is not supported
        """
        strategy_class = cls._strategies.get(operation_type)
        if not strategy_class:
            logger.error(f"Unsupported operation type: {operation_type}")
            raise ValueError(f"Unsupported operation type: {operation_type}")
        
        logger.debug(f"Creating strategy for operation: {operation_type}")
        return strategy_class()
    
    @classmethod
    def calculate(cls, a: float, b: float, operation_type: str) -> float:
        """
        Perform a calculation using the factory pattern.
        
        Args:
            a: First operand
            b: Second operand
            operation_type: Type of operation
            
        Returns:
            Result of the calculation
            
        Raises:
            ValueError: If operation type is not supported
            DivisionByZeroError: If attempting to divide by zero
        """
        strategy = cls.get_strategy(operation_type)
        logger.info(f"Executing {operation_type} operation: {a} and {b}")
        
        try:
            result = strategy.execute(a, b)
            logger.info(f"Calculation result: {result}")
            return result
        except DivisionByZeroError as e:
            logger.error(f"Division by zero error: {e}")
            raise
        except Exception as e:
            logger.error(f"Calculation error: {e}")
            raise
    
    @classmethod
    def get_supported_operations(cls) -> list[str]:
        """
        Get list of all supported operation types.
        
        Returns:
            List of operation type names
        """
        return list(cls._strategies.keys())


# Example of extending the factory with a new operation
class PowerStrategy(CalculationStrategy):
    """Strategy for power/exponentiation operations."""
    
    def execute(self, a: float, b: float) -> float:
        """Perform exponentiation: a^b"""
        logger.debug(f"Power: {a} ^ {b}")
        result = a ** b
        logger.debug(f"Power result: {result}")
        return result
    
    def get_operation_name(self) -> str:
        return "power"


class ModuloStrategy(CalculationStrategy):
    """Strategy for modulo operations."""
    
    def execute(self, a: float, b: float) -> float:
        """Perform modulo: a % b"""
        if b == 0:
            logger.error(f"Modulo by zero attempted: {a} % {b}")
            raise DivisionByZeroError("Cannot perform modulo with zero")
        logger.debug(f"Modulo: {a} % {b}")
        result = a % b
        logger.debug(f"Modulo result: {result}")
        return result
    
    def get_operation_name(self) -> str:
        return "modulo"


# Optional: Uncomment to enable additional operations
# CalculationFactory.register_strategy("power", PowerStrategy)
# CalculationFactory.register_strategy("modulo", ModuloStrategy)
