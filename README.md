# Flask Kickoff

A minimal Flask starter project with authentication, user management, and database migrations. Built for rapid prototyping and learning.

## Features

- **Flask 3** - Modern Python web framework
- **Authentication** - Login system with cookie-based sessions
- **User Management** - RESTful API for CRUD operations on users
- **Database** - SQLite with SQLAlchemy ORM and Flask-Migrate
- **Configuration** - Environment-based config (development, testing, production)
- **Testing** - Unit and functional tests with pytest
- **Templates** - Jinja2 templates with CSS styling

## Project Structure

```
flask-kickoff/
├── app.py                 # Application entry point
├── config.py              # Configuration classes
├── pyproject.toml         # Project metadata and dependencies
├── uv.lock                # Locked dependencies
├── README.md              # This file
├── LICENSE                # GPL-3.0 license
├── .gitignore
├── .python-version
├── app/
│   ├── __init__.py        # App factory pattern
│   ├── extensions.py      # Flask extensions (db, migrate)
│   ├── models/
│   │   └── user.py        # User model
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py        # Authentication routes
│   │   ├── hello.py       # Hello world route
│   │   └── users.py       # User management API
│   ├── static/
│   │   └── style.css      # Custom styles
│   └── templates/
│       ├── dashboard.html # Authenticated user dashboard
│       ├── hello.html     # Hello world template
│       └── login.html     # Login page
├── migrations/            # Database migrations (Alembic)
│   ├── env.py
│   ├── alembic.ini
│   ├── script.py.mako
│   └── versions/
└── tests/
    ├── conftest.py        # Pytest fixtures
    ├── unit/
    │   └── test_user.py   # Unit tests for User model
    └── functional/
        └── test_landing_page.py  # Functional tests
```

## Quick Start

### Prerequisites

- Python 3.14+
- uv (recommended) or pip

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd flask-kickoff

# Install dependencies with uv (recommended)
uv sync

# Or with pip
pip install -e .
```

### Configuration

Copy the example environment variables or set them directly:

```bash
export SECRET_KEY="your-secret-key-here"
export FLASK_ENV=development
```

### Database Setup

```bash
# Initialize the database
flask db init

# Create migration
flask db migrate -m "Initial migration"

# Apply migration
flask db upgrade
```

### Running the Application

```bash
# Development server
flask run

# Or directly with Python
python app.py
```

The app will be available at `http://localhost:5000`

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/unit/test_user.py
pytest tests/functional/test_landing_page.py
```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/auth/login` | Show login page |
| POST   | `/auth/login` | Process login |

### User Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/users` | List all users |
| POST   | `/users` | Create a new user |
| GET    | `/users/<id>` | Get user by ID |
| PATCH  | `/users/<id>` | Update user |

### Other

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/hello` | Simple hello world |

## Default Credentials

For testing purposes, the auth system includes these hardcoded users:

| Username | Password |
|----------|----------|
| admin    | secret123 |
| user1    | password125 |

## Configuration Environments

| Environment | Database | Debug |
|-------------|----------|-------|
| development | SQLite (`/tmp/foo.db`) | Enabled |
| testing     | SQLite (in-memory) | Enabled |
| production  | MySQL (configure in config.py) | Disabled |

Set the environment with `FLASK_ENV` or pass it to `create_app()`:

```python
from app import create_app
app = create_app("production")
```

## Extensions Used

- **Flask-SQLAlchemy** - Database ORM
- **Flask-Migrate** - Database migrations via Alembic
- **Werkzeug** - Security utilities (password hashing)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

*Generated as a Flask kickoff starter project*