# Python Package Template

A comprehensive boilerplate for creating Python packages with modern tooling and best practices.

## 🚀 Features

- **Modern Python packaging** with `pyproject.toml`
- **UV package manager** support for fast dependency management
- **MkDocs** documentation with Material theme
- **GitHub Actions** ready configuration placeholders
- **Pre-configured** project structure
- **Automated setup script** for easy customization

## 📁 Project Structure

```
├── package_name/           # Main package directory (rename this)
│   ├── __init__.py
│   ├── client.py
│   ├── config.py
│   ├── exceptions.py
│   └── utils/
├── docs/                   # Documentation
│   ├── index.md
│   ├── overview.md
│   ├── setup.md
│   └── contributing.md
├── scripts/
│   └── deploy-package.sh   # Deployment script
├── tests/                  # Test directory
├── pyproject.toml         # Project configuration
├── mkdocs.yml            # Documentation configuration
├── README.md             # This file (will be replaced)
├── CONTRIBUTING.md       # Contribution guidelines
├── template-config.md    # Template documentation
└── setup_template.py     # Setup script
```

## 🛠️ Quick Setup

### Option 1: Interactive Setup (Recommended)

Run the interactive setup script:

```bash
python setup_template.py
```

This will prompt you for all necessary information and automatically configure the template.

### Option 2: Manual Setup

1. **Replace all placeholder variables** in the following files:
   - `README.md`
   - `pyproject.toml`
   - `mkdocs.yml`
   - `scripts/deploy-package.sh`
   - `CONTRIBUTING.md`

2. **Rename the package directory**:
   ```bash
   mv package_name/ your_package_name/
   ```

3. **Update imports** in `__init__.py` files if needed

## 🔧 Template Variables

The template uses the following placeholder variables:

| Placeholder | Description | Example |
|------------|-------------|---------|
| `{PACKAGE_NAME}` | Package name (PyPI) | `my_awesome_package` |
| `{PACKAGE_DISPLAY_NAME}` | Display name | `My Awesome Package` |
| `{PACKAGE_DESCRIPTION}` | Package description | `A Python package for awesome things` |
| `{AUTHOR_NAME}` | Author name | `John Doe` |
| `{AUTHOR_EMAIL}` | Author email | `john@example.com` |
| `{GITHUB_USERNAME}` | GitHub username | `johndoe` |
| `{REPOSITORY_NAME}` | Repository name | `my-awesome-package` |
| `{KEYWORD_1-4}` | PyPI keywords | `python`, `package`, etc. |

See `template-config.md` for a complete list of variables.

## 📦 Package Development

After setup, develop your package by:

1. **Adding implementation** in your package directory
2. **Writing tests** in the `tests/` directory
3. **Updating documentation** in `docs/`
4. **Managing dependencies** with UV:
   ```bash
   uv add your-dependency
   uv remove unwanted-dependency
   ```

## 🔐 Environment Variables

### GitHub Actions Workflows

For publishing your package to PyPI, you'll need to configure the `PYPI_API_TOKEN` in your GitHub repository:

#### Setting up PYPI_API_TOKEN

1. **Create a PyPI API Token:**
   - Go to [PyPI Account Settings](https://pypi.org/manage/account/)
   - Navigate to "API tokens"
   - Click "Add API token"
   - Set scope to "Entire account" or specific to your project
   - Copy the generated token (starts with `pypi-`)

2. **Add to GitHub Repository Secrets:**
   - Go to your repository Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `PYPI_API_TOKEN`
   - Value: Your PyPI token (e.g., `pypi-xxxxxxxxxxxx`)

## 🚀 Deployment

Use the included deployment script:

```bash
./scripts/deploy-package.sh
```

This script handles:
- Building the package with UV
- Running tests
- Publishing to PyPI

## 📚 Documentation

Generate documentation with MkDocs:

```bash
mkdocs serve  # Local development
mkdocs build  # Build static files
```

## 🧹 Cleanup

After setting up your package, you can remove template files:

```bash
rm template-config.md setup_template.py .github/README.md
```

## 📄 License

This template is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🤝 Contributing

Contributions to improve this template are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

**Happy coding! 🎉**
