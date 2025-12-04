# Useful commands to setup a Django Project

Here's a few commands to make your Django project setup easier

## Configure Django

```shell
django-admin start-project project .
```

- "project" is the standard name of the project, you can change it if you
want

```shell
python manage.py startapp contact
```
- When creating an app, always update the installed apps in the project
settings.py

## Migrate Django database

```shell
python manage.py makemigrations
```

- Everytime you make an alteration in your models you have to run this command
and after, to applicate this changes, you run 'migrate' bellow

```shell
python manage.py migrate
```

- Django has some migrations that have to be applied, that means none of the
default tables are not yet created (admin, auth, contenttypes, sessions)

- Migrations are files that come together with your created app, each time you
make a change in models, your are working with a database.

## Creating and modifying a Django superuser password

```shell
python manage.py createsuperuser
```

- superuser has full access to all Django databases

```shell
python manage.py changepassword username
```

- If you forgot your password you can change it with this command

## Django Shell Commands

- Here are some usefull CRUD django shell commands to use in the terminal

```python
# Import module
from contact.models import Contact
# Create contact (Lazy)
# Returns contact
contact = Contact(**fields)
contact.save()
# Create contact (Não lazy)
# Returns contact
contact = Contact.objects.create(**fields)
# Select contact with id 10
# Returns contact
contact = Contact.objects.get(pk=10)
# Edit contact
# Returns contact
contact.field_name1 = 'New value 1'
contact.field_name2 = 'New value 2'
contact.save()
# Delete contact
# Depends of the database, generally returns the number of values manipulated
# in the database
contact.delete()
# Select all the data by id (descending)
# Returns QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Select contact using filters
# Returns QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')
```

## Static Files

```shell
python manage.py collectstatic
```