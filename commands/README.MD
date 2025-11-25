# Useful commands to setup a Django Project

Here's a few commands to make your Django project setup easier

## Configure Django

```
django-admin start-project project .
```

- "project" is the standard name of the project, you can change it if you
want

```
python manage.py startapp contact
```
- When creating an app, always update the installed apps in the project
settings.py

## Migrate Django database

```
python manage.py migrate
```

- Django has some migrations that have to be applied, that means none of the
default tables are not yet created (admin, auth, contenttypes, sessions)

- Migrations are files that come together with your created app, each time you
make a change in models, your are working with a database.

```
python manage.py makemigrations
```

- Everytime you make an alteration in your models you have to run this command
and after, to applicate this changes, you run 'migrate' again

## Creating and modifying a Django superuser password

```
python manage.py createsuperuser
```

- superuser has full access to all Django databases

```
python manage.py changepassword username
```

- If you forgot your password you can change it with this command