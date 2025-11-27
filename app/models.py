"""
SQLAlchemy models for the application.
"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class User(Base):
    """
    User model for storing user information.
    
    Attributes:
        id: Primary key, auto-incrementing integer
        username: Unique username for the user
        email: Unique email address for the user
        password_hash: Hashed password (never store plain text passwords)
        created_at: Timestamp when the user was created
        updated_at: Timestamp when the user was last updated
        is_active: Flag to indicate if the user account is active
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # Relationship to calculations
    calculations = relationship("Calculation", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        """String representation of User model."""
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

    def __str__(self):
        """Human-readable string representation."""
        return f"User: {self.username} ({self.email})"


class Calculation(Base):
    """
    Calculation model for storing calculation history.
    
    Attributes:
        id: Primary key, auto-incrementing integer
        user_id: Foreign key to the user who created the calculation
        a: First operand (float)
        b: Second operand (float)
        type: Type of operation (add, subtract, multiply, divide)
        result: Computed result of the operation (stored for historical tracking)
        created_at: Timestamp when the calculation was created
    """
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    type = Column(String(20), nullable=False)  # add, subtract, multiply, divide
    result = Column(Float, nullable=False)  # Store result for historical tracking
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationship to user
    user = relationship("User", back_populates="calculations")

    def __repr__(self):
        """String representation of Calculation model."""
        return f"<Calculation(id={self.id}, type='{self.type}', a={self.a}, b={self.b}, result={self.result})>"

    def __str__(self):
        """Human-readable string representation."""
        return f"Calculation: {self.a} {self.type} {self.b} = {self.result}"
