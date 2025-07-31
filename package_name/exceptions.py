"""
Custom exceptions for {PACKAGE_DISPLAY_NAME}.
"""


class PackageError(Exception):
    """Base exception class for {PACKAGE_DISPLAY_NAME}."""
    pass


class ValidationError(PackageError):
    """Raised when input validation fails."""
    pass


class APIError(PackageError):
    """Raised when API requests fail."""
    pass


class AuthenticationError(PackageError):
    """Raised when authentication fails."""
    pass


class ConfigurationError(PackageError):
    """Raised when configuration is invalid."""
    pass