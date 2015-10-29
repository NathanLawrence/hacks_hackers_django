import datetime

from django.db import models
from django.utils import timezone

# Each class is a subclass of django.db.models.Model so that it maps to a table in our database
# Each atribute of each class maps to a column on that table

class Quiz(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published', null=True)
	creator = models.CharField(max_length=100)

	# __str__ is a built-in class method that we are overriding
	def __str__(self):
		# now the string version of the quiz will appear as the title
		return self.title

	# we can also custom class methods, for example, to perform some calculation on our data
	# this method returns true if the publication date is within the last day
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Question(models.Model):
	# establishes a one-to-many relationship between quiz and questions
	quiz = models.ForeignKey(Quiz)
	text = models.CharField(max_length=255)
	order = models.IntegerField()

	def __str__(self):
		return self.text

class Choice(models.Model):
	# establishes a one-to-many relationship between question and choices
	question = models.ForeignKey(Question)
	letter = models.CharField(max_length=1)
	text = models.CharField(max_length=255)
	is_correct = models.BooleanField(default = False)

	def __str__(self):
		return self.text