# Python Package Template Configuration

This template uses placeholder variables that need to be replaced when creating a new package. Here are all the placeholders and their descriptions:

## Required Replacements

### Package Information
- `{PACKAGE_NAME}` - The package name (lowercase, underscores allowed, e.g., "my_awesome_package")
- `{PACKAGE_DISPLAY_NAME}` - The display name for the package (e.g., "My Awesome Package")
- `{PACKAGE_DESCRIPTION}` - A brief description of what the package does

### Author Information
- `{AUTHOR_NAME}` - The package author's full name
- `{AUTHOR_EMAIL}` - The package author's email address

### Repository Information
- `{GITHUB_USERNAME}` - GitHub username or organization name
- `{REPOSITORY_NAME}` - GitHub repository name

### Keywords (for PyPI)
- `{KEYWORD_1}` - First keyword tag
- `{KEYWORD_2}` - Second keyword tag
- `{KEYWORD_3}` - Third keyword tag
- `{KEYWORD_4}` - Fourth keyword tag

### Optional Customizations
- `{LEGAL_DISCLAIMER_TEXT}` - Custom legal disclaimer text (if needed)
- `{POWERED_BY_NAME}` - Name of the service/API the package wraps (if applicable)
- `{POWERED_BY_URL}` - URL of the service/API the package wraps (if applicable)

## Files to Update After Template Use

1. **Package Directory**: Rename `package_name/` to your actual package name
2. **Code Files**: Add your actual implementation in:
   - `package_name/__init__.py`
   - `package_name/client.py`
   - `package_name/config.py`
   - `package_name/exceptions.py`
   - `package_name/utils/`

3. **Documentation**: Update the docs/ folder with actual content:
   - `docs/index.md`
   - `docs/overview.md`
   - `docs/setup.md`
   - `docs/contributing.md`

4. **Dependencies**: Update `pyproject.toml` dependencies based on your package needs

## Usage Instructions

1. Find and replace all placeholder variables with your actual values
2. Rename the `package_name` directory to your actual package name
3. Update the package imports in `__init__.py` files
4. Add your implementation code
5. Update documentation
6. Test the package
7. Delete this `template-config.md` file

## Example Replacement

For a package called "weather-api-client":

```
{PACKAGE_NAME} → weather_api_client
{PACKAGE_DISPLAY_NAME} → Weather API Client
{PACKAGE_DESCRIPTION} → A Python client for accessing weather data APIs
{AUTHOR_NAME} → John Doe
{AUTHOR_EMAIL} → john.doe@example.com
{GITHUB_USERNAME} → johndoe
{REPOSITORY_NAME} → weather-api-client
{KEYWORD_1} → weather
{KEYWORD_2} → api
{KEYWORD_3} → client
{KEYWORD_4} → meteorology
```
