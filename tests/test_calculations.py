"""
Tests for Calculation model and related functionality.
"""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from pydantic import ValidationError
from app.database import Base
from app.models import User, Calculation
from app.schemas import CalculationCreate, CalculationResponse, CalculationUpdate
from app.calculation_factory import (
    CalculationFactory, 
    AdditionStrategy, 
    SubtractionStrategy,
    MultiplicationStrategy,
    DivisionStrategy,
    PowerStrategy,
    ModuloStrategy,
    CalculationStrategy
)
from app.operations import DivisionByZeroError
from datetime import datetime


# Create in-memory SQLite database for testing
engine = create_engine("sqlite:///:memory:")
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def db_session():
    """Create a new database session for each test."""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def sample_user(db_session: Session):
    """Create a sample user for testing."""
    user = User(
        username="testuser",
        email="test@example.com",
        password_hash="hashed_password"
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


class TestCalculationModel:
    """Test suite for Calculation SQLAlchemy model."""
    
    def test_calculation_model_creation(self, db_session: Session, sample_user: User):
        """Test creating a calculation model instance."""
        calculation = Calculation(
            user_id=sample_user.id,
            a=10.5,
            b=5.2,
            type="add",
            result=15.7
        )
        db_session.add(calculation)
        db_session.commit()
        db_session.refresh(calculation)
        
        assert calculation.id is not None
        assert calculation.user_id == sample_user.id
        assert calculation.a == 10.5
        assert calculation.b == 5.2
        assert calculation.type == "add"
        assert calculation.result == 15.7
        assert calculation.created_at is not None
    
    def test_calculation_user_relationship(self, db_session: Session, sample_user: User):
        """Test relationship between Calculation and User."""
        calculation = Calculation(
            user_id=sample_user.id,
            a=20.0,
            b=10.0,
            type="multiply",
            result=200.0
        )
        db_session.add(calculation)
        db_session.commit()
        db_session.refresh(calculation)
        
        # Test bidirectional relationship
        assert calculation.user.id == sample_user.id
        assert calculation.user.username == sample_user.username
        assert calculation in sample_user.calculations
    
    def test_calculation_cascade_delete(self, db_session: Session, sample_user: User):
        """Test that calculations are deleted when user is deleted."""
        calculation = Calculation(
            user_id=sample_user.id,
            a=100.0,
            b=50.0,
            type="subtract",
            result=50.0
        )
        db_session.add(calculation)
        db_session.commit()
        
        calc_id = calculation.id
        
        # Delete user
        db_session.delete(sample_user)
        db_session.commit()
        
        # Calculation should also be deleted
        deleted_calc = db_session.query(Calculation).filter(Calculation.id == calc_id).first()
        assert deleted_calc is None
    
    def test_calculation_repr(self, db_session: Session, sample_user: User):
        """Test string representation of Calculation."""
        calculation = Calculation(
            user_id=sample_user.id,
            a=15.0,
            b=3.0,
            type="divide",
            result=5.0
        )
        db_session.add(calculation)
        db_session.commit()
        db_session.refresh(calculation)
        
        repr_str = repr(calculation)
        assert "Calculation" in repr_str
        assert str(calculation.id) in repr_str
        assert "divide" in repr_str
        assert "15.0" in repr_str
        assert "3.0" in repr_str
        assert "5.0" in repr_str
    
    def test_calculation_multiple_per_user(self, db_session: Session, sample_user: User):
        """Test that a user can have multiple calculations."""
        calculations = [
            Calculation(user_id=sample_user.id, a=10, b=5, type="add", result=15),
            Calculation(user_id=sample_user.id, a=10, b=5, type="subtract", result=5),
            Calculation(user_id=sample_user.id, a=10, b=5, type="multiply", result=50),
            Calculation(user_id=sample_user.id, a=10, b=5, type="divide", result=2),
        ]
        
        for calc in calculations:
            db_session.add(calc)
        db_session.commit()
        
        db_session.refresh(sample_user)
        assert len(sample_user.calculations) == 4


class TestCalculationSchemas:
    """Test suite for Calculation Pydantic schemas."""
    
    def test_calculation_create_schema_valid(self):
        """Test valid CalculationCreate schema."""
        data = {
            "a": 10.5,
            "b": 5.2,
            "type": "add"
        }
        calc = CalculationCreate(**data)
        assert calc.a == 10.5
        assert calc.b == 5.2
        assert calc.type == "add"
    
    def test_calculation_create_invalid_operation_type(self):
        """Test CalculationCreate with invalid operation type."""
        data = {
            "a": 10.5,
            "b": 5.2,
            "type": "invalid_operation"
        }
        with pytest.raises(ValidationError) as exc_info:
            CalculationCreate(**data)
        assert "literal_error" in str(exc_info.value)
    
    def test_calculation_create_division_by_zero(self):
        """Test CalculationCreate prevents division by zero."""
        data = {
            "a": 10.0,
            "b": 0.0,
            "type": "divide"
        }
        with pytest.raises(ValueError, match="Division by zero"):
            CalculationCreate(**data)
    
    def test_calculation_create_all_operation_types(self):
        """Test CalculationCreate with all valid operation types."""
        operations = ["add", "subtract", "multiply", "divide"]
        for op in operations:
            data = {
                "a": 10.0,
                "b": 5.0 if op != "divide" or 5.0 != 0 else 5.0,
                "type": op
            }
            calc = CalculationCreate(**data)
            assert calc.type == op
    
    def test_calculation_response_schema(self):
        """Test CalculationResponse schema."""
        data = {
            "id": 1,
            "user_id": 1,
            "a": 10.5,
            "b": 5.2,
            "type": "add",
            "result": 15.7,
            "created_at": datetime.now()
        }
        calc = CalculationResponse(**data)
        assert calc.id == 1
        assert calc.user_id == 1
        assert calc.result == 15.7
    
    def test_calculation_update_schema(self):
        """Test CalculationUpdate schema with optional fields."""
        # All fields optional
        data = {"a": 20.0}
        calc = CalculationUpdate(**data)
        assert calc.a == 20.0
        assert calc.b is None
        assert calc.type is None
    
    def test_calculation_update_invalid_type(self):
        """Test CalculationUpdate with invalid operation type."""
        data = {"type": "invalid"}
        with pytest.raises(ValidationError) as exc_info:
            CalculationUpdate(**data)
        assert "literal_error" in str(exc_info.value)


class TestCalculationFactory:
    """Test suite for Calculation Factory pattern."""
    
    def test_factory_get_addition_strategy(self):
        """Test getting addition strategy from factory."""
        strategy = CalculationFactory.get_strategy("add")
        assert isinstance(strategy, AdditionStrategy)
        assert strategy.get_operation_name() == "add"
    
    def test_factory_get_subtraction_strategy(self):
        """Test getting subtraction strategy from factory."""
        strategy = CalculationFactory.get_strategy("subtract")
        assert isinstance(strategy, SubtractionStrategy)
        assert strategy.get_operation_name() == "subtract"
    
    def test_factory_get_multiplication_strategy(self):
        """Test getting multiplication strategy from factory."""
        strategy = CalculationFactory.get_strategy("multiply")
        assert isinstance(strategy, MultiplicationStrategy)
        assert strategy.get_operation_name() == "multiply"
    
    def test_factory_get_division_strategy(self):
        """Test getting division strategy from factory."""
        strategy = CalculationFactory.get_strategy("divide")
        assert isinstance(strategy, DivisionStrategy)
        assert strategy.get_operation_name() == "divide"
    
    def test_factory_invalid_operation(self):
        """Test factory with invalid operation type."""
        with pytest.raises(ValueError, match="Unsupported operation type"):
            CalculationFactory.get_strategy("invalid_op")
    
    def test_factory_calculate_addition(self):
        """Test factory calculate method with addition."""
        result = CalculationFactory.calculate(10.0, 5.0, "add")
        assert result == 15.0
    
    def test_factory_calculate_subtraction(self):
        """Test factory calculate method with subtraction."""
        result = CalculationFactory.calculate(10.0, 5.0, "subtract")
        assert result == 5.0
    
    def test_factory_calculate_multiplication(self):
        """Test factory calculate method with multiplication."""
        result = CalculationFactory.calculate(10.0, 5.0, "multiply")
        assert result == 50.0
    
    def test_factory_calculate_division(self):
        """Test factory calculate method with division."""
        result = CalculationFactory.calculate(10.0, 5.0, "divide")
        assert result == 2.0
    
    def test_factory_calculate_division_by_zero(self):
        """Test factory handles division by zero."""
        with pytest.raises(DivisionByZeroError):
            CalculationFactory.calculate(10.0, 0.0, "divide")
    
    def test_factory_get_supported_operations(self):
        """Test getting list of supported operations."""
        operations = CalculationFactory.get_supported_operations()
        assert "add" in operations
        assert "subtract" in operations
        assert "multiply" in operations
        assert "divide" in operations
        assert len(operations) >= 4
    
    def test_factory_register_new_strategy(self):
        """Test registering a new custom strategy."""
        # Register power strategy
        CalculationFactory.register_strategy("power", PowerStrategy)
        
        # Verify it's registered
        assert "power" in CalculationFactory.get_supported_operations()
        
        # Test using the new strategy
        result = CalculationFactory.calculate(2.0, 3.0, "power")
        assert result == 8.0
    
    def test_factory_register_modulo_strategy(self):
        """Test registering modulo strategy."""
        CalculationFactory.register_strategy("modulo", ModuloStrategy)
        
        assert "modulo" in CalculationFactory.get_supported_operations()
        result = CalculationFactory.calculate(10.0, 3.0, "modulo")
        assert result == 1.0
    
    def test_modulo_by_zero(self):
        """Test modulo strategy handles division by zero."""
        CalculationFactory.register_strategy("modulo", ModuloStrategy)
        
        with pytest.raises(DivisionByZeroError):
            CalculationFactory.calculate(10.0, 0.0, "modulo")


class TestCalculationStrategies:
    """Test individual calculation strategies."""
    
    def test_addition_strategy(self):
        """Test AdditionStrategy directly."""
        strategy = AdditionStrategy()
        result = strategy.execute(7.5, 2.5)
        assert result == 10.0
        assert strategy.get_operation_name() == "add"
    
    def test_subtraction_strategy(self):
        """Test SubtractionStrategy directly."""
        strategy = SubtractionStrategy()
        result = strategy.execute(10.0, 3.5)
        assert result == 6.5
        assert strategy.get_operation_name() == "subtract"
    
    def test_multiplication_strategy(self):
        """Test MultiplicationStrategy directly."""
        strategy = MultiplicationStrategy()
        result = strategy.execute(4.0, 2.5)
        assert result == 10.0
        assert strategy.get_operation_name() == "multiply"
    
    def test_division_strategy(self):
        """Test DivisionStrategy directly."""
        strategy = DivisionStrategy()
        result = strategy.execute(20.0, 4.0)
        assert result == 5.0
        assert strategy.get_operation_name() == "divide"
    
    def test_division_strategy_by_zero(self):
        """Test DivisionStrategy handles division by zero."""
        strategy = DivisionStrategy()
        with pytest.raises(DivisionByZeroError):
            strategy.execute(10.0, 0.0)
    
    def test_power_strategy(self):
        """Test PowerStrategy."""
        strategy = PowerStrategy()
        result = strategy.execute(3.0, 4.0)
        assert result == 81.0
        assert strategy.get_operation_name() == "power"
    
    def test_modulo_strategy(self):
        """Test ModuloStrategy."""
        strategy = ModuloStrategy()
        result = strategy.execute(17.0, 5.0)
        assert result == 2.0
        assert strategy.get_operation_name() == "modulo"


# Fixtures for tests
@pytest.fixture
def sample_user(db_session: Session):
    """Create a sample user for testing."""
    user = User(
        username="testuser",
        email="test@example.com",
        password_hash="hashed_password"
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user
