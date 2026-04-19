# Custom Flask Boilerplate

A robust, reusable Flask starter template designed for scalable web applications. This boilerplate is pre-configured with PostgreSQL for local development and sets the foundation for custom UI design without the bloat of utility frameworks.

## 🚀 Tech Stack

* **Framework:** Flask
* **Database ORM:** SQLAlchemy
* **Database:** PostgreSQL (Local & Production)
* **Migrations:** Flask-Migrate (Alembic)
* **Templating:** Jinja2
* **Frontend:** Custom CSS architecture (No Flask-Bootstrap or utility frameworks)

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
* Python 3.10+
* PostgreSQL (running locally)
* `psycopg2-binary` or `psycopg` (included in requirements)

## 🛠️ Local Development Setup

**1. Clone the repository for your new project:**
```bash
git clone <your-repo-url> my-new-project
cd my-new-project
```

**2. Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables:**

Create a .env file in the root directory and add your PostgreSQL credentials:
```bash
FLASK_APP=run.py
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://username:password@localhost:5432/your_database_name
```

**5. Initialize and run database migrations:**
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

**6. Run the application:**
```bash
flask run
```

Your app will be available at http://127.0.0.1:5000.