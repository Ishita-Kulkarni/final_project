"""
Unit tests for operations.py
Tests all calculator functions individually
"""
import pytest
import math
from app.operations import (
    add, subtract, multiply, divide, power, modulus, square_root, nth_root, calculate,
    DivisionByZeroError, InvalidOperationError, NegativeRootError, InvalidExponentError
)


class TestAddition:
    """Test cases for add function"""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        assert add(5, 3) == 8
        assert add(10.5, 2.5) == 13.0
        
    def test_add_negative_numbers(self):
        """Test adding two negative numbers"""
        assert add(-5, -3) == -8
        assert add(-10.5, -2.5) == -13.0
        
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers"""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
        
    def test_add_with_zero(self):
        """Test adding with zero"""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0
        
    def test_add_large_numbers(self):
        """Test adding large numbers"""
        assert add(1000000, 2000000) == 3000000
        
    def test_add_decimal_numbers(self):
        """Test adding decimal numbers"""
        result = add(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10


class TestSubtraction:
    """Test cases for subtract function"""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(10, 3) == 7
        assert subtract(5.5, 2.5) == 3.0
        
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -15) == 5
        
    def test_subtract_mixed_numbers(self):
        """Test subtracting with mixed signs"""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8
        
    def test_subtract_with_zero(self):
        """Test subtracting with zero"""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0
        
    def test_subtract_same_numbers(self):
        """Test subtracting same numbers"""
        assert subtract(7, 7) == 0
        assert subtract(-5, -5) == 0


class TestMultiplication:
    """Test cases for multiply function"""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers"""
        assert multiply(5, 3) == 15
        assert multiply(2.5, 4) == 10.0
        
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        assert multiply(-5, -3) == 15
        assert multiply(-2, -4) == 8
        
    def test_multiply_mixed_signs(self):
        """Test multiplying with mixed signs"""
        assert multiply(5, -3) == -15
        assert multiply(-5, 3) == -15
        
    def test_multiply_with_zero(self):
        """Test multiplying with zero"""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0
        
    def test_multiply_with_one(self):
        """Test multiplying with one"""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5
        
    def test_multiply_decimals(self):
        """Test multiplying decimal numbers"""
        assert multiply(2.5, 4) == 10.0
        assert multiply(0.5, 0.5) == 0.25


class TestDivision:
    """Test cases for divide function"""
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5
        assert divide(7.5, 2.5) == 3.0
        
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers"""
        assert divide(-10, -2) == 5
        assert divide(-15, -3) == 5
        
    def test_divide_mixed_signs(self):
        """Test dividing with mixed signs"""
        assert divide(10, -2) == -5
        assert divide(-10, 2) == -5
        
    def test_divide_by_zero(self):
        """Test division by zero raises exception"""
        with pytest.raises(DivisionByZeroError) as exc_info:
            divide(10, 0)
        assert "Cannot divide by zero" in str(exc_info.value)
        
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number"""
        assert divide(0, 5) == 0
        assert divide(0, -5) == 0
        
    def test_divide_by_one(self):
        """Test dividing by one"""
        assert divide(5, 1) == 5
        assert divide(-5, 1) == -5
        
    def test_divide_decimals(self):
        """Test dividing decimal numbers"""
        assert divide(5, 2) == 2.5
        assert divide(1, 3) == pytest.approx(0.333333, rel=1e-5)


class TestPower:
    """Test cases for power function"""
    
    def test_power_positive_base_positive_exponent(self):
        """Test power with positive base and exponent"""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(10, 3) == 1000
        
    def test_power_positive_base_negative_exponent(self):
        """Test power with positive base and negative exponent"""
        assert power(2, -1) == 0.5
        assert power(10, -2) == 0.01
        
    def test_power_negative_base_positive_exponent(self):
        """Test power with negative base"""
        assert power(-2, 3) == -8
        assert power(-2, 2) == 4
        
    def test_power_zero_base(self):
        """Test power with zero base"""
        assert power(0, 5) == 0
        assert power(0, 100) == 0
        
    def test_power_exponent_zero(self):
        """Test any number to the power of zero"""
        assert power(5, 0) == 1
        assert power(100, 0) == 1
        assert power(-5, 0) == 1
        
    def test_power_exponent_one(self):
        """Test any number to the power of one"""
        assert power(5, 1) == 5
        assert power(-10, 1) == -10
        
    def test_power_decimal_exponent(self):
        """Test power with decimal exponent (roots)"""
        assert power(4, 0.5) == pytest.approx(2.0)
        assert power(27, 1/3) == pytest.approx(3.0, rel=1e-5)
        
    def test_power_overflow_protection(self):
        """Test that very large exponents raise error"""
        with pytest.raises(InvalidExponentError):
            power(2, 10000)


class TestModulus:
    """Test cases for modulus function"""
    
    def test_modulus_positive_numbers(self):
        """Test modulus with positive numbers"""
        assert modulus(10, 3) == 1
        assert modulus(17, 5) == 2
        assert modulus(20, 4) == 0
        
    def test_modulus_negative_dividend(self):
        """Test modulus with negative dividend"""
        assert modulus(-10, 3) == 2  # Python's modulus behavior
        assert modulus(-17, 5) == 3
        
    def test_modulus_negative_divisor(self):
        """Test modulus with negative divisor"""
        assert modulus(10, -3) == -2
        
    def test_modulus_both_negative(self):
        """Test modulus with both negative"""
        assert modulus(-10, -3) == -1
        
    def test_modulus_by_zero(self):
        """Test modulus by zero raises exception"""
        with pytest.raises(DivisionByZeroError) as exc_info:
            modulus(10, 0)
        assert "modulus with zero divisor" in str(exc_info.value).lower()
        
    def test_modulus_decimal_numbers(self):
        """Test modulus with decimal numbers"""
        assert modulus(10.5, 3) == pytest.approx(1.5)
        assert modulus(7.5, 2.5) == pytest.approx(0.0)


class TestSquareRoot:
    """Test cases for square_root function"""
    
    def test_square_root_perfect_squares(self):
        """Test square root of perfect squares"""
        assert square_root(4, 0) == 2
        assert square_root(9, 0) == 3
        assert square_root(16, 0) == 4
        assert square_root(25, 0) == 5
        
    def test_square_root_non_perfect_squares(self):
        """Test square root of non-perfect squares"""
        assert square_root(2, 0) == pytest.approx(1.414213, rel=1e-5)
        assert square_root(3, 0) == pytest.approx(1.732050, rel=1e-5)
        
    def test_square_root_zero(self):
        """Test square root of zero"""
        assert square_root(0, 0) == 0
        
    def test_square_root_one(self):
        """Test square root of one"""
        assert square_root(1, 0) == 1
        
    def test_square_root_decimal(self):
        """Test square root of decimal numbers"""
        assert square_root(0.25, 0) == 0.5
        assert square_root(6.25, 0) == 2.5
        
    def test_square_root_negative_number(self):
        """Test square root of negative number raises exception"""
        with pytest.raises(NegativeRootError) as exc_info:
            square_root(-4, 0)
        assert "Cannot calculate square root of negative number" in str(exc_info.value)
        
    def test_square_root_large_number(self):
        """Test square root of large number"""
        assert square_root(1000000, 0) == 1000


class TestNthRoot:
    """Test cases for nth_root function"""
    
    def test_nth_root_square_root(self):
        """Test nth_root with n=2 (square root)"""
        assert nth_root(4, 2) == pytest.approx(2.0)
        assert nth_root(9, 2) == pytest.approx(3.0)
        
    def test_nth_root_cube_root(self):
        """Test nth_root with n=3 (cube root)"""
        assert nth_root(8, 3) == pytest.approx(2.0)
        assert nth_root(27, 3) == pytest.approx(3.0)
        
    def test_nth_root_fourth_root(self):
        """Test nth_root with n=4"""
        assert nth_root(16, 4) == pytest.approx(2.0)
        assert nth_root(81, 4) == pytest.approx(3.0)
        
    def test_nth_root_negative_odd_root(self):
        """Test nth_root with negative number and odd root"""
        assert nth_root(-8, 3) == pytest.approx(-2.0)
        assert nth_root(-27, 3) == pytest.approx(-3.0)
        
    def test_nth_root_negative_even_root(self):
        """Test nth_root with negative number and even root raises exception"""
        with pytest.raises(NegativeRootError) as exc_info:
            nth_root(-4, 2)
        assert "even root of negative number" in str(exc_info.value).lower()
        
    def test_nth_root_zero_root(self):
        """Test nth_root with n=0 raises exception"""
        with pytest.raises(DivisionByZeroError) as exc_info:
            nth_root(8, 0)
        assert "zeroth root" in str(exc_info.value).lower()
        
    def test_nth_root_one(self):
        """Test nth_root with n=1"""
        assert nth_root(5, 1) == pytest.approx(5.0)
        assert nth_root(100, 1) == pytest.approx(100.0)
        
    def test_nth_root_decimal(self):
        """Test nth_root with decimal numbers"""
        assert nth_root(0.25, 2) == pytest.approx(0.5)


class TestCalculate:
    """Test cases for the main calculate function"""
    
    def test_calculate_add(self):
        """Test calculate with add operation"""
        assert calculate(5, 3, "add") == 8
        assert calculate(5, 3, "ADD") == 8  # Test case insensitivity
        
    def test_calculate_subtract(self):
        """Test calculate with subtract operation"""
        assert calculate(10, 3, "subtract") == 7
        assert calculate(10, 3, "SUBTRACT") == 7
        
    def test_calculate_multiply(self):
        """Test calculate with multiply operation"""
        assert calculate(5, 3, "multiply") == 15
        assert calculate(5, 3, "MULTIPLY") == 15
        
    def test_calculate_divide(self):
        """Test calculate with divide operation"""
        assert calculate(10, 2, "divide") == 5
        assert calculate(10, 2, "DIVIDE") == 5
        
    def test_calculate_power(self):
        """Test calculate with power operation"""
        assert calculate(2, 3, "power") == 8
        assert calculate(5, 2, "POWER") == 25
        
    def test_calculate_modulus(self):
        """Test calculate with modulus operation"""
        assert calculate(10, 3, "modulus") == 1
        assert calculate(17, 5, "MODULUS") == 2
        
    def test_calculate_square_root(self):
        """Test calculate with square_root operation"""
        assert calculate(9, 0, "square_root") == 3
        assert calculate(16, 0, "SQUARE_ROOT") == 4
        
    def test_calculate_nth_root(self):
        """Test calculate with nth_root operation"""
        assert calculate(8, 3, "nth_root") == pytest.approx(2.0)
        assert calculate(27, 3, "NTH_ROOT") == pytest.approx(3.0)
        
    def test_calculate_invalid_operation(self):
        """Test calculate with invalid operation"""
        with pytest.raises(InvalidOperationError) as exc_info:
            calculate(5, 3, "invalid_op")
        assert "Invalid operation" in str(exc_info.value)
        
    def test_calculate_division_by_zero(self):
        """Test calculate with division by zero"""
        with pytest.raises(DivisionByZeroError):
            calculate(10, 0, "divide")
            
    def test_calculate_modulus_by_zero(self):
        """Test calculate with modulus by zero"""
        with pytest.raises(DivisionByZeroError):
            calculate(10, 0, "modulus")
            
    def test_calculate_negative_square_root(self):
        """Test calculate with negative square root"""
        with pytest.raises(NegativeRootError):
            calculate(-4, 0, "square_root")
            
    def test_calculate_empty_operation(self):
        """Test calculate with empty operation"""
        with pytest.raises(InvalidOperationError):
            calculate(5, 3, "")


class TestEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def test_very_large_numbers(self):
        """Test operations with very large numbers"""
        large_num = 10**100
        assert add(large_num, large_num) == 2 * large_num
        assert subtract(large_num, large_num) == 0
        
    def test_very_small_numbers(self):
        """Test operations with very small numbers"""
        small_num = 1e-10
        assert add(small_num, small_num) == pytest.approx(2e-10)
        
    def test_negative_zero(self):
        """Test operations with negative zero"""
        assert add(-0, 5) == 5
        assert multiply(-0, 5) == 0
        
    def test_power_fractional_results(self):
        """Test power operations that result in fractions"""
        assert power(2, -3) == pytest.approx(0.125)
        
    def test_modulus_smaller_dividend(self):
        """Test modulus when dividend is smaller than divisor"""
        assert modulus(3, 10) == 3
        
    def test_nth_root_identity(self):
        """Test that (x^n)^(1/n) = x"""
        x = 5
        n = 3
        result = nth_root(power(x, n), n)
        assert result == pytest.approx(x, rel=1e-5)


class TestNewOperationsIntegration:
    """Integration tests for new operations working together"""
    
    def test_power_and_square_root(self):
        """Test that power and square root are inverses"""
        assert square_root(power(5, 2), 0) == pytest.approx(5.0)
        
    def test_modulus_after_division(self):
        """Test modulus and division relationship"""
        a, b = 17, 5
        quotient = int(divide(a, b))
        remainder = modulus(a, b)
        assert quotient * b + remainder == a
        
    def test_chained_operations(self):
        """Test multiple operations in sequence"""
        result = add(power(2, 3), modulus(10, 3))
        assert result == 9  # 8 + 1
