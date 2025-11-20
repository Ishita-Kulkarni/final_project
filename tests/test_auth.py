"""
Unit tests for authentication and password hashing functions.
"""
import pytest
from auth import hash_password, verify_password, get_password_hash


class TestPasswordHashing:
    """Test password hashing functionality."""
    
    def test_hash_password_returns_string(self):
        """Test that hash_password returns a string."""
        password = "testpassword123"
        hashed = hash_password(password)
        assert isinstance(hashed, str)
        assert len(hashed) > 0
    
    def test_hash_password_produces_different_hashes(self):
        """Test that same password produces different hashes (due to salt)."""
        password = "testpassword123"
        hash1 = hash_password(password)
        hash2 = hash_password(password)
        assert hash1 != hash2  # Different salts
    
    def test_hash_password_starts_with_bcrypt_prefix(self):
        """Test that hashed password starts with bcrypt identifier."""
        password = "testpassword123"
        hashed = hash_password(password)
        assert hashed.startswith("$2b$")
    
    def test_verify_password_correct_password(self):
        """Test that verify_password returns True for correct password."""
        password = "testpassword123"
        hashed = hash_password(password)
        assert verify_password(password, hashed) is True
    
    def test_verify_password_incorrect_password(self):
        """Test that verify_password returns False for incorrect password."""
        password = "testpassword123"
        wrong_password = "wrongpassword"
        hashed = hash_password(password)
        assert verify_password(wrong_password, hashed) is False
    
    def test_verify_password_empty_password(self):
        """Test verify_password with empty password."""
        password = "testpassword123"
        hashed = hash_password(password)
        assert verify_password("", hashed) is False
    
    def test_verify_password_case_sensitive(self):
        """Test that password verification is case-sensitive."""
        password = "TestPassword123"
        hashed = hash_password(password)
        assert verify_password("testpassword123", hashed) is False
        assert verify_password("TestPassword123", hashed) is True
    
    def test_get_password_hash_alias(self):
        """Test that get_password_hash works as alias."""
        password = "testpassword123"
        hashed = get_password_hash(password)
        assert isinstance(hashed, str)
        assert verify_password(password, hashed) is True
    
    def test_hash_special_characters(self):
        """Test hashing passwords with special characters."""
        password = "p@$$w0rd!#%&*()_+"
        hashed = hash_password(password)
        assert verify_password(password, hashed) is True
    
    def test_hash_unicode_characters(self):
        """Test hashing passwords with unicode characters."""
        password = "пароль密码🔒"
        hashed = hash_password(password)
        assert verify_password(password, hashed) is True
    
    def test_hash_long_password(self):
        """Test hashing very long passwords."""
        password = "a" * 200
        hashed = hash_password(password)
        assert verify_password(password, hashed) is True
    
    def test_verify_with_invalid_hash(self):
        """Test verify_password with invalid hash format."""
        password = "testpassword123"
        invalid_hash = "not_a_valid_hash"
        with pytest.raises(ValueError):
            verify_password(password, invalid_hash)
