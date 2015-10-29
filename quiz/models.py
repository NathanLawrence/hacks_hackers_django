import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Quiz(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	creator = models.CharField(max_length=100)

	def __str__(self):
		return self.title

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Question(models.Model):
	quiz = models.ForeignKey(Quiz)
	text = models.CharField(max_length=255)
	order = models.IntegerField()

	def __str__(self):
		return self.text

class Choice(models.Model):
	question = models.ForeignKey(Question)
	letter = models.CharField(max_length=1)
	text = models.CharField(max_length=255)
	is_correct = models.BooleanField(default = False)

	def __str__(self):
		return self.text