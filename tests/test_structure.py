"""
Basic tests for the package template.
This file tests the template structure after setup.
"""

import pytest


def test_template_structure():
    """Test that the template has the expected structure."""
    import os
    
    # Check that key files exist
    expected_files = [
        "pyproject.toml",
        "README.md",
        "mkdocs.yml",
    ]
    
    for file_name in expected_files:
        assert os.path.exists(file_name), f"Missing file: {file_name}"


def test_can_import_package():
    """Test that the package can be imported."""
    try:
        # This will work after the package is renamed and configured
        import package_name
        assert hasattr(package_name, '__version__')
    except ImportError:
        # This is expected in the template state
        pass


if __name__ == "__main__":
    pytest.main([__file__])
