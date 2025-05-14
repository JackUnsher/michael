from setuptools import setup, find_packages

__version__ = '1.0.0'

setup(
    name="megahash",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "Flask==2.2.5",
        "Flask-SQLAlchemy==3.0.3",
        "SQLAlchemy==2.0.9",
        "Flask-Migrate==4.0.4",
        "Flask-WTF==1.1.1",
        "WTForms==3.0.1",
        "Flask-Login==0.6.2",
        "Flask-Babel==3.1.0",
        "Flask-Admin==1.6.1",
        "python-dotenv==1.0.0",
        "email-validator==2.0.0",
        "Werkzeug==2.2.3",
        "Jinja2==3.1.2",
        "psycopg2-binary==2.9.6",
        "pytz==2023.3",
        "Babel==2.12.1",
        "Flask-Moment==1.0.5",
        "Pillow==9.5.0",
        "gunicorn==20.1.0",
    ],
    python_requires='>=3.8',
)
