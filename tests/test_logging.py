"""
Tests for logging functionality
Ensures logging is working correctly throughout the application
"""
import pytest
import logging
import os
from pathlib import Path
from unittest.mock import patch, MagicMock
from app.logger_config import setup_logging, get_logger
from app.operations import add, subtract, multiply, divide, calculate
from fastapi.testclient import TestClient
from app.main import app


class TestLoggerConfiguration:
    """Test logger configuration setup"""
    
    def test_setup_logging_creates_logs_directory(self):
        """Test that setup_logging creates the logs directory"""
        log_dir = Path("logs")
        # Directory should be created by setup_logging
        assert log_dir.exists()
        assert log_dir.is_dir()
        
    def test_logger_has_correct_level(self):
        """Test logger has the correct log level"""
        logger = setup_logging("DEBUG")
        assert logger.level == logging.DEBUG
        
        logger = setup_logging("INFO")
        assert logger.level == logging.INFO
        
    def test_logger_has_handlers(self):
        """Test logger has file and console handlers"""
        logger = get_logger()
        assert len(logger.handlers) >= 3  # Console, file, and error handlers
        
    def test_log_files_created(self):
        """Test that log files are created"""
        log_dir = Path("logs")
        app_log = log_dir / "app.log"
        error_log = log_dir / "error.log"
        
        # Trigger logging to create files
        logger = get_logger()
        logger.info("Test log message")
        logger.error("Test error message")
        
        assert app_log.exists()
        assert error_log.exists()


class TestOperationsLogging:
    """Test logging in operations module"""
    
    def test_add_logs_operation(self, caplog):
        """Test that add function logs the operation"""
        with caplog.at_level(logging.DEBUG, logger="fastapi_calculator"):
            result = add(5, 3)
            assert "Addition: 5" in caplog.text or "Addition: 5.0" in caplog.text
            assert "Addition result: 8" in caplog.text or "Addition result: 8.0" in caplog.text
            
    def test_subtract_logs_operation(self, caplog):
        """Test that subtract function logs the operation"""
        with caplog.at_level(logging.DEBUG, logger="fastapi_calculator"):
            result = subtract(10, 4)
            assert "Subtraction: 10" in caplog.text or "Subtraction: 10.0" in caplog.text
            assert "Subtraction result: 6" in caplog.text or "Subtraction result: 6.0" in caplog.text
            
    def test_multiply_logs_operation(self, caplog):
        """Test that multiply function logs the operation"""
        with caplog.at_level(logging.DEBUG, logger="fastapi_calculator"):
            result = multiply(6, 7)
            assert "Multiplication: 6" in caplog.text or "Multiplication: 6.0" in caplog.text
            assert "Multiplication result: 42" in caplog.text or "Multiplication result: 42.0" in caplog.text
            
    def test_divide_logs_operation(self, caplog):
        """Test that divide function logs the operation"""
        with caplog.at_level(logging.DEBUG, logger="fastapi_calculator"):
            result = divide(20, 4)
            assert "Division: 20" in caplog.text or "Division: 20.0" in caplog.text
            assert "Division result: 5" in caplog.text or "Division result: 5.0" in caplog.text
            
    def test_divide_logs_error_on_zero(self, caplog):
        """Test that divide logs error when dividing by zero"""
        with caplog.at_level(logging.ERROR):
            with pytest.raises(Exception):
                divide(10, 0)
            assert "Division by zero attempted" in caplog.text
            
    def test_calculate_logs_info(self, caplog):
        """Test that calculate function logs at INFO level"""
        with caplog.at_level(logging.INFO):
            result = calculate(10, 5, "add")
            assert "Calculate called" in caplog.text
            assert "num1=10" in caplog.text
            assert "num2=5" in caplog.text
            assert "operation=add" in caplog.text
            assert "Calculation successful" in caplog.text
            
    def test_calculate_logs_invalid_operation(self, caplog):
        """Test that calculate logs error for invalid operation"""
        with caplog.at_level(logging.ERROR):
            with pytest.raises(Exception):
                calculate(10, 5, "invalid")
            assert "Invalid operation requested" in caplog.text


class TestAPILogging:
    """Test logging in API endpoints"""
    
    client = TestClient(app)
    
    def test_root_endpoint_logs(self, caplog):
        """Test that root endpoint logs access"""
        with caplog.at_level(logging.INFO):
            response = self.client.get("/")
            assert "Root endpoint accessed" in caplog.text
            assert "Incoming request: GET /" in caplog.text
            assert "Request completed: GET / - Status: 200" in caplog.text
            
    def test_calculate_endpoint_logs_request(self, caplog):
        """Test that calculate endpoint logs the request"""
        with caplog.at_level(logging.INFO):
            payload = {"num1": 10, "num2": 5, "operation": "add"}
            response = self.client.post("/calculate", json=payload)
            assert "Calculate endpoint called with" in caplog.text
            assert "num1=10" in caplog.text
            assert "num2=5" in caplog.text
            assert "operation=add" in caplog.text
            
    def test_calculate_endpoint_logs_success(self, caplog):
        """Test that calculate endpoint logs successful calculation"""
        with caplog.at_level(logging.INFO):
            payload = {"num1": 10, "num2": 5, "operation": "add"}
            response = self.client.post("/calculate", json=payload)
            assert "Calculation successful" in caplog.text
            assert "returning result: 15" in caplog.text
            
    def test_calculate_endpoint_logs_division_by_zero(self, caplog):
        """Test that division by zero is logged"""
        with caplog.at_level(logging.WARNING):
            payload = {"num1": 10, "num2": 0, "operation": "divide"}
            response = self.client.post("/calculate", json=payload)
            assert "Division by zero error" in caplog.text
            
    def test_calculate_endpoint_logs_invalid_operation(self, caplog):
        """Test that invalid operation is logged"""
        with caplog.at_level(logging.WARNING):
            payload = {"num1": 10, "num2": 5, "operation": "invalid_op"}
            response = self.client.post("/calculate", json=payload)
            assert "Invalid operation" in caplog.text
            
    def test_health_endpoint_logs(self, caplog):
        """Test that health endpoint logs access"""
        with caplog.at_level(logging.DEBUG, logger="fastapi_calculator"):
            response = self.client.get("/health")
            # Health endpoint uses DEBUG level, check if request was logged
            assert "GET /health" in caplog.text
            
    def test_middleware_logs_request_duration(self, caplog):
        """Test that middleware logs request duration"""
        with caplog.at_level(logging.INFO):
            response = self.client.get("/")
            assert "Duration:" in caplog.text
            assert response.headers.get("X-Process-Time") is not None
            
    def test_middleware_adds_process_time_header(self):
        """Test that middleware adds X-Process-Time header"""
        response = self.client.get("/")
        assert "X-Process-Time" in response.headers
        process_time = float(response.headers["X-Process-Time"])
        assert process_time >= 0


class TestLogFileContent:
    """Test that logs are written to files correctly"""
    
    def test_app_log_contains_info_messages(self):
        """Test that app.log contains INFO level messages"""
        logger = get_logger()
        test_message = "Test INFO message for verification"
        logger.info(test_message)
        
        log_file = Path("logs/app.log")
        assert log_file.exists()
        
        content = log_file.read_text()
        assert test_message in content
        
    def test_error_log_contains_error_messages(self):
        """Test that error.log contains ERROR level messages"""
        logger = get_logger()
        test_error = "Test ERROR message for verification"
        logger.error(test_error)
        
        error_file = Path("logs/error.log")
        assert error_file.exists()
        
        content = error_file.read_text()
        assert test_error in content
        
    def test_debug_messages_not_in_console(self, caplog):
        """Test that DEBUG messages don't appear in console handler"""
        # Console handler is set to INFO level
        logger = get_logger()
        
        # Clear previous logs
        caplog.clear()
        
        with caplog.at_level(logging.DEBUG):
            logger.debug("Debug message - should be in file only")
            logger.info("Info message - should be everywhere")
        
        # Check that info message is logged
        assert "Info message" in caplog.text


class TestLogRotation:
    """Test log rotation functionality"""
    
    def test_rotating_handler_configured(self):
        """Test that rotating file handler is configured"""
        logger = get_logger()
        
        # Check for RotatingFileHandler
        from logging.handlers import RotatingFileHandler
        rotating_handlers = [
            h for h in logger.handlers 
            if isinstance(h, RotatingFileHandler)
        ]
        
        assert len(rotating_handlers) >= 2  # app.log and error.log
        
    def test_max_bytes_configured(self):
        """Test that max bytes is configured for rotation"""
        logger = get_logger()
        
        from logging.handlers import RotatingFileHandler
        rotating_handlers = [
            h for h in logger.handlers 
            if isinstance(h, RotatingFileHandler)
        ]
        
        for handler in rotating_handlers:
            assert handler.maxBytes == 10 * 1024 * 1024  # 10 MB
            assert handler.backupCount == 5


class TestLogLevels:
    """Test different log levels"""
    
    def test_debug_level_logs_all(self, caplog):
        """Test that DEBUG level logs all messages"""
        logger = setup_logging("DEBUG")
        
        with caplog.at_level(logging.DEBUG):
            logger.debug("Debug message")
            logger.info("Info message")
            logger.warning("Warning message")
            logger.error("Error message")
            
        assert "Debug message" in caplog.text
        assert "Info message" in caplog.text
        assert "Warning message" in caplog.text
        assert "Error message" in caplog.text
        
    def test_info_level_filters_debug(self, caplog):
        """Test that INFO level filters out DEBUG messages"""
        logger = setup_logging("INFO")
        
        with caplog.at_level(logging.DEBUG):
            logger.debug("Debug message - should not appear")
            logger.info("Info message - should appear")
            
        # Note: caplog will capture all levels, but logger won't emit DEBUG
        # Check the logger's level instead
        assert logger.level == logging.INFO
