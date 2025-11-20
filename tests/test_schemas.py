"""
Unit tests for Pydantic schemas.
"""
import pytest
from pydantic import ValidationError
from datetime import datetime
from schemas import (
    UserCreate, UserResponse, UserLogin, UserUpdate, 
    UserRead, Token, Message
)


class TestUserCreateSchema:
    """Test UserCreate schema validation."""
    
    def test_valid_user_create(self):
        """Test creating a valid UserCreate instance."""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
        user = UserCreate(**user_data)
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.password == "password123"
    
    def test_username_too_short(self):
        """Test that username less than 3 characters is invalid."""
        user_data = {
            "username": "ab",
            "email": "test@example.com",
            "password": "password123"
        }
        with pytest.raises(ValidationError) as exc_info:
            UserCreate(**user_data)
        assert "username" in str(exc_info.value)
    
    def test_username_too_long(self):
        """Test that username longer than 50 characters is invalid."""
        user_data = {
            "username": "a" * 51,
            "email": "test@example.com",
            "password": "password123"
        }
        with pytest.raises(ValidationError) as exc_info:
            UserCreate(**user_data)
        assert "username" in str(exc_info.value)
    
    def test_invalid_email(self):
        """Test that invalid email format is rejected."""
        user_data = {
            "username": "testuser",
            "email": "not-an-email",
            "password": "password123"
        }
        with pytest.raises(ValidationError) as exc_info:
            UserCreate(**user_data)
        assert "email" in str(exc_info.value)
    
    def test_password_too_short(self):
        """Test that password less than 8 characters is invalid."""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "pass123"
        }
        with pytest.raises(ValidationError) as exc_info:
            UserCreate(**user_data)
        assert "password" in str(exc_info.value)
    
    def test_missing_required_fields(self):
        """Test that missing required fields raises ValidationError."""
        with pytest.raises(ValidationError):
            UserCreate(username="testuser")
        
        with pytest.raises(ValidationError):
            UserCreate(email="test@example.com")
        
        with pytest.raises(ValidationError):
            UserCreate(password="password123")


class TestUserResponseSchema:
    """Test UserResponse schema."""
    
    def test_user_response_from_dict(self):
        """Test creating UserResponse from dictionary."""
        user_data = {
            "id": 1,
            "username": "testuser",
            "email": "test@example.com",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
            "is_active": True
        }
        user = UserResponse(**user_data)
        assert user.id == 1
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.is_active is True
    
    def test_user_response_no_password_field(self):
        """Test that UserResponse doesn't include password field."""
        user_data = {
            "id": 1,
            "username": "testuser",
            "email": "test@example.com",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
            "is_active": True,
            "password_hash": "hashed_password"  # Should be ignored
        }
        user = UserResponse(**user_data)
        assert not hasattr(user, "password")
        assert not hasattr(user, "password_hash")
    
    def test_user_read_alias(self):
        """Test that UserRead is an alias for UserResponse."""
        assert UserRead is UserResponse


class TestUserLoginSchema:
    """Test UserLogin schema."""
    
    def test_valid_login(self):
        """Test creating a valid UserLogin instance."""
        login_data = {
            "username": "testuser",
            "password": "password123"
        }
        login = UserLogin(**login_data)
        assert login.username == "testuser"
        assert login.password == "password123"
    
    def test_missing_username(self):
        """Test that missing username raises ValidationError."""
        with pytest.raises(ValidationError):
            UserLogin(password="password123")
    
    def test_missing_password(self):
        """Test that missing password raises ValidationError."""
        with pytest.raises(ValidationError):
            UserLogin(username="testuser")


class TestUserUpdateSchema:
    """Test UserUpdate schema."""
    
    def test_update_all_fields(self):
        """Test updating all fields."""
        update_data = {
            "username": "newusername",
            "email": "newemail@example.com",
            "password": "newpassword123"
        }
        update = UserUpdate(**update_data)
        assert update.username == "newusername"
        assert update.email == "newemail@example.com"
        assert update.password == "newpassword123"
    
    def test_update_partial_fields(self):
        """Test updating only some fields."""
        update = UserUpdate(username="newusername")
        assert update.username == "newusername"
        assert update.email is None
        assert update.password is None
    
    def test_update_empty(self):
        """Test creating empty update (all None)."""
        update = UserUpdate()
        assert update.username is None
        assert update.email is None
        assert update.password is None
    
    def test_update_invalid_email(self):
        """Test that invalid email in update is rejected."""
        with pytest.raises(ValidationError):
            UserUpdate(email="not-an-email")


class TestTokenSchema:
    """Test Token schema."""
    
    def test_valid_token(self):
        """Test creating a valid Token instance."""
        token_data = {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            "token_type": "bearer"
        }
        token = Token(**token_data)
        assert token.access_token == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        assert token.token_type == "bearer"
    
    def test_token_default_type(self):
        """Test that token_type defaults to 'bearer'."""
        token = Token(access_token="test_token")
        assert token.token_type == "bearer"


class TestMessageSchema:
    """Test Message schema."""
    
    def test_valid_message(self):
        """Test creating a valid Message instance."""
        message = Message(message="Operation successful")
        assert message.message == "Operation successful"
    
    def test_missing_message(self):
        """Test that missing message raises ValidationError."""
        with pytest.raises(ValidationError):
            Message()
