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
  python manage.py migrate --database=admin
  ```


# Database Routing
Once you've got your databases defined in the DATABASES setting, now we'll need to handle automatic routing.

Create a folder called 'routers'
Inside the folder create a file called router.py
Create a database router called AuthRouter to control all database operations on models in the auth and contenttypes - add the following code inside the router.py file:

```bash
class ReplicationRouterUser:
    route_app_labels = {'core'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'user'
        return None


class ReplicationRouterAdmin:
    route_app_labels = {'core'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'admin'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'admin'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'admin'
        return None
```  

# Connecting the routers
Database routers are installed using the DATABASE_ROUTERS setting. This setting defines a list of class names, each specifying a router that should be used by the master router.

```bash
DATABASE_ROUTERS = [
    'core.router.ReplicationRouterUser',
    'core.router.ReplicationRouterAdmin'
]
```

# Selecting a database

You can select the database for a QuerySet at any point in the QuerySet “chain.” Call using() on the QuerySet to get another QuerySet that uses the specified database.

using() takes a single argument: the alias of the database on which you want to run the query.

For Example:

>>> # This will run on the 'default' database.
>>> CustomerInformation.objects.all()

>>> # This will fetch the details using 'user' DataBase
>>> CustomerInformation.objects.using('user').all()

>>> # This will run on the 'admin' database.
>>> CustomerSupport.objects.using('admin').all()