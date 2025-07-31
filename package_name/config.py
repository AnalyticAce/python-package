"""
Configuration management for {PACKAGE_DISPLAY_NAME}.
"""

import os
from typing import Optional
from dataclasses import dataclass


@dataclass
class Config:
    """Configuration class for {PACKAGE_DISPLAY_NAME}."""
    
    # API Configuration
    api_key: Optional[str] = None
    base_url: str = "https://api.example.com"
    timeout: int = 30
    
    # Debug settings
    debug: bool = False
    
    @classmethod
    def from_env(cls) -> "Config":
        """Create configuration from environment variables."""
        return cls(
            api_key=os.getenv("API_KEY"),
            base_url=os.getenv("BASE_URL", "https://api.example.com"),
            timeout=int(os.getenv("TIMEOUT", "30")),
            debug=os.getenv("DEBUG", "false").lower() == "true",
        )
    
    def validate(self) -> None:
        """Validate the configuration."""
        if not self.api_key:
            raise ValueError("API key is required")
        
        if self.timeout <= 0:
            raise ValueError("Timeout must be positive")


# Default configuration instance
default_config = Config()