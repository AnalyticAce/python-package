#!/usr/bin/env python3
"""
Template Setup Script for Python Package Boilerplate

This script helps configure the template by replacing placeholder variables
with actual values for your new Python package.
"""

import os
import re
import shutil
from pathlib import Path


def replace_in_file(file_path: Path, replacements: dict) -> bool:
    """Replace placeholders in a file with actual values."""
    try:
        content = file_path.read_text(encoding='utf-8')
        modified = False
        
        for placeholder, value in replacements.items():
            if placeholder in content:
                content = content.replace(placeholder, value)
                modified = True
        
        if modified:
            file_path.write_text(content, encoding='utf-8')
            print(f"✅ Updated: {file_path}")
            return True
        return False
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False


def rename_package_directory(old_name: str, new_name: str, base_path: Path) -> bool:
    """Rename the package directory."""
    old_path = base_path / old_name
    new_path = base_path / new_name
    
    if old_path.exists() and old_path.is_dir():
        try:
            shutil.move(str(old_path), str(new_path))
            print(f"✅ Renamed directory: {old_name} → {new_name}")
            return True
        except Exception as e:
            print(f"❌ Error renaming directory: {e}")
            return False
    return False


def collect_user_input() -> dict:
    """Collect configuration values from user."""
    print("🚀 Python Package Template Setup")
    print("=" * 40)
    
    replacements = {}
    
    # Required fields
    replacements['{PACKAGE_NAME}'] = input("📦 Package name (e.g., my_awesome_package): ").strip()
    replacements['{PACKAGE_DISPLAY_NAME}'] = input("✨ Display name (e.g., My Awesome Package): ").strip()
    replacements['{PACKAGE_DESCRIPTION}'] = input("📝 Package description: ").strip()
    replacements['{AUTHOR_NAME}'] = input("👤 Author name: ").strip()
    replacements['{AUTHOR_EMAIL}'] = input("📧 Author email: ").strip()
    replacements['{GITHUB_USERNAME}'] = input("🐙 GitHub username: ").strip()
    replacements['{REPOSITORY_NAME}'] = input("📁 Repository name: ").strip()
    
    # Keywords
    print("\n🏷️  Enter 4 keywords for PyPI (press Enter for defaults):")
    replacements['{KEYWORD_1}'] = input("  Keyword 1: ").strip() or "python"
    replacements['{KEYWORD_2}'] = input("  Keyword 2: ").strip() or "package"
    replacements['{KEYWORD_3}'] = input("  Keyword 3: ").strip() or "library"
    replacements['{KEYWORD_4}'] = input("  Keyword 4: ").strip() or "api"
    
    # Optional fields
    print("\n⚙️  Optional configurations (press Enter to skip):")
    disclaimer = input("⚠️  Legal disclaimer text: ").strip()
    if disclaimer:
        replacements['{LEGAL_DISCLAIMER_TEXT}'] = disclaimer
    else:
        replacements['{LEGAL_DISCLAIMER_TEXT}'] = "Please review applicable laws and regulations."
    
    powered_by_name = input("⚡ 'Powered by' name: ").strip()
    powered_by_url = input("🔗 'Powered by' URL: ").strip()
    
    if powered_by_name and powered_by_url:
        replacements['{POWERED_BY_NAME}'] = powered_by_name
        replacements['{POWERED_BY_URL}'] = powered_by_url
    else:
        replacements['{POWERED_BY_NAME}'] = "Open Source Community"
        replacements['{POWERED_BY_URL}'] = "https://github.com"
    
    return replacements


def main():
    """Main setup function."""
    base_path = Path(__file__).parent
    
    # Collect user input
    replacements = collect_user_input()
    
    print(f"\n🔄 Configuring template...")
    
    # Files to update
    files_to_update = [
        'README.md',
        'pyproject.toml',
        'mkdocs.yml',
        'scripts/deploy-package.sh',
        'CONTRIBUTING.md',
        'package_name/__init__.py',
        'package_name/client.py',
        'package_name/config.py',
        'package_name/exceptions.py',
        'package_name/utils/__init__.py',
        'docs/index.md',
        'docs/overview.md',
        'docs/setup.md',
        'tests/test_template.py'
    ]
    
    # Update files
    updated_count = 0
    for file_name in files_to_update:
        file_path = base_path / file_name
        if file_path.exists():
            if replace_in_file(file_path, replacements):
                updated_count += 1
    
    # Rename package directory
    package_name = replacements['{PACKAGE_NAME}']
    if rename_package_directory('package_name', package_name, base_path):
        updated_count += 1
    
    print(f"\n✨ Setup complete! Updated {updated_count} items.")
    print(f"📁 Your package directory is now: {package_name}/")
    print("\n📋 Next steps:")
    print("1. Add your implementation code")
    print("2. Update documentation in docs/")
    print("3. Run tests")
    print("4. Delete template-config.md and setup_template.py")
    print("5. Commit your changes")


if __name__ == "__main__":
    main()
