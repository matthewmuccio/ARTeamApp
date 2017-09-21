import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# With this code, Django can:
# Create a database schema (CREATE TABLE statements).
# Create a Python database-access API for accessing Question and Choice objs.

# Migrations are how Django stores changes to your models (and your database schema).
# They're just files on disk.

# Define models, essentially the database layout, with additional metadata.
# A model is the single, definitive source of truth about the data.
# It contains the essential fields and behaviors of the data you're storing.
# Goal: to define your data model in one place and automatically derive things from it.

# Each model is represented by a class that subclasses django.db.models.Model.
# Each has a number of class variables, which represents a database field in the model.

# Question model
# A Question model has a question and a publication date.
@python_2_unicode_compatible # Allows for support for Python 2.
class Question(models.Model):
    # Each field is represented by an instance of a Field class, tells Django the data type it holds.
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# Choice model
# A Choice model has two fields: the text of the choice and a vote tally.
# Each Choice is to be associated with a Question.
@python_2_unicode_compatible # Allows for support for Python 2.
class Choice(models.Model):
	# A relationship is defined here, using ForeignKey, which tells Django that each
	# Choice is related to a single Question.
	# Django supports all the common DB relationships: one-to-one, many-to-many.
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
