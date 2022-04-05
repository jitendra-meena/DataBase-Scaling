# DataBase-Scaling
Scaling in DBMS is the ability to expand the capacity of a database system in order to support larger amounts or requests and/or store more data without sacrificing performance


# Basic Setup

1. Create your virtual environment
2. Create a Django project
3. Create your database servers

# Install Dependencies
  ```bash
  pip install -r requirements.txt
  ```


# Defining your databases
The first step to using more than one database with Django is to tell Django about the database servers you’ll be using. This is done using the 'DATABASES' setting. Databases can have any alias you choose. However, the alias default has special significance. Django uses the database with the alias of default when no other database has been selected.

The following is an example settings.py snippet defining two databases – a default PostgreSQL database and a SQLite database called users_db:


# DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'user': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'UserDB',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost'
    },
    'admin': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'AdminDB',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost'
    }
}


# Migrate Database
  
  ```bash
  python manage.py migrate 
  python manage.py migrate --database=user
  ```