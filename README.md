hacks_hackers_django
====================

A starter Django project for Hacks / Hackers IRE (Columbia, MO).

Overview
--------

Django is a popular, full-featured Python framework. We're going to be learning the basics by creating simple quiz app.

Concepts we will cover:

1.	The model layer (including migrations)
2.	The admin
3.	The view layer
4.	The template layer

This walk-through borrows liberally from the [Write your first Django app](https://docs.djangoproject.com/en/1.8/intro/tutorial01/) tutorial, which is published by the makers of Django, and is a good a place as any for first-timers to dive in.

Set-up
------

We'll assume you've already [installed](https://docs.djangoproject.com/en/1.8/intro/install/) Django. The [recommended set-up](https://docs.djangoproject.com/en/1.8/topics/install/#installing-an-official-release-with-pip) suggests installing Django into an isolated Python environment. To do that:

1.	Install [virtualenv](https://virtualenv.pypa.io/en/latest/)
2.	Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)
3.	Set up a virtual environment:
		
		$ mkvirtualenv hacks_hackers_django

	Whereas 'hacks_hackers_django' can be substituted for whatever you want you want to call your virtual environment. This will give you:

		New python executable in hacks_hackers_django/bin/python2.7
		Also creating executable in hacks_hackers_django/bin/python
		Installing setuptools, pip...done.

4.	Then install Django:

		$ pip install django

	Which gives you:

		Downloading/unpacking django
		  Downloading Django-1.8.5-py2.py3-none-any.whl (6.2MB): 6.2MB downloaded
		Installing collected packages: django
		Successfully installed django
		Cleaning up...

If you were starting a new Django project from scratch, you would have to run several other commands to set up the project's directory with default files and settings. That's all really well documented [here](https://docs.djangoproject.com/en/1.8/intro/tutorial01/#creating-a-project), but if you are just cloning/forking this repo, you can skip all of that.

Note that we're using SQLite for our database, which is Django's default, so nothing to change there.

The Model Layer
---------------

By using Django's object-relational mapper, we can define the structure of our app's data in one place, instead of defining in both SQL and Python, with the possibility of conflicts. 

First, let's establish some basic requirements for our app:

*	The app can have multiple quizes;
*	Each quiz can have multiple questions;
*	Each question can have multiple possible choices;
*	Each question must have at least one answer.

The outline for this data structure belongs in [quiz/models.py](https://github.com/gordonje/hacks_hackers_django/blob/master/quiz/models.py). Each class in this file is a subclass of django.db.models.Model so that it maps to a table in our database. Each attribute of the class maps to a column in our database, and we set the data type for these columns by choosing from which Field subclass (e.g., CharField, IntegerField, BooleanField) the attribute will inherit.

Check the Django documentation for more about the [models syntax](https://docs.djangoproject.com/en/1.8/topics/db/models/) and [field types and options](https://docs.djangoproject.com/en/1.8/ref/models/fields/#module-django.db.models.fields).

We can also override or add new methods to these classes in case we want to perform some convenient calculations using our data. For example, we added a method to Quiz, which will return True if the quiz was published within the last 24 hours.

We also have to [activate our models](https://docs.djangoproject.com/en/1.8/intro/tutorial01/#activating-models) by adding our app's name to the list of installed app's for our Django project. This setting is found in [hacks_hackers_django/settings.py](https://github.com/gordonje/hacks_hackers_django/blob/master/hacks_hackers/hacks_hackers_django/settings.py:

	INSTALLED_APPS = (
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    'quiz',
	)

One feature that makes Django extremely popular as a web framework is how well it handles database [migrations](https://docs.djangoproject.com/en/1.8/topics/migrations/). If we ever needed to change our models, for exmaple, to add new tables or fields, here are the steps we follow:

1.	Make whatever changes we like in quiz/models.py
2.	Make the instructions for the pending migration:

		$ python manage.py makemigrations quiz

	Which will give you:

		Migrations for 'polls':
		  0001_initial.py:
		    - Create model Question
		    - Create model Choice
		    - Add field question to choice

	And will also create (if necessary) a new directory -- quiz/migrations -- where are these instructions will be logged.
3.	Apply the changes:

		$  python manage.py migrate

	Which will give you:

		Operations to perform:
		  Synchronize unmigrated apps: staticfiles, messages
		  Apply all migrations: admin, contenttypes, sessions, auth, quiz
		Synchronizing apps without migrations:
		  Creating tables...
		    Running deferred SQL...
		  Installing custom SQL...
		Running migrations:
		  Rendering model states... DONE
		  Applying quiz.0002_auto_20151029_1641... OK


