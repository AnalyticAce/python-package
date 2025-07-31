"""
Tests for {PACKAGE_DISPLAY_NAME}.
"""

import pytest
from {PACKAGE_NAME} import Client
from {PACKAGE_NAME}.config import Config
from {PACKAGE_NAME}.exceptions import ValidationError, APIError


class TestConfig:
    """Test configuration management."""
    
    def test_config_creation(self):
        """Test creating a configuration object."""
        config = Config(
            api_key="test-key",
            base_url="https://test.example.com",
            timeout=60
        )
        
        assert config.api_key == "test-key"
        assert config.base_url == "https://test.example.com"
        assert config.timeout == 60
    
    def test_config_validation(self):
        """Test configuration validation."""
        config = Config(api_key=None)
        
        with pytest.raises(ValueError, match="API key is required"):
            config.validate()


class TestClient:
    """Test the main client class."""
    
    def test_client_creation(self):
        """Test creating a client instance."""
        config = Config(api_key="test-key")
        client = Client(config=config)
        
        assert client.config.api_key == "test-key"
        assert "Authorization" in client.session.headers
    
    def test_client_version(self):
        """Test getting the client version."""
        client = Client()
        version = client.get_version()
        
        assert isinstance(version, str)
        assert len(version) > 0


class TestExceptions:
    """Test custom exceptions."""
    
    def test_validation_error(self):
        """Test ValidationError exception."""
        with pytest.raises(ValidationError):
            raise ValidationError("Test validation error")
    
    def test_api_error(self):
        """Test APIError exception."""
        with pytest.raises(APIError):
            raise APIError("Test API error")


if __name__ == "__main__":
    pytest.main([__file__])
