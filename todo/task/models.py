from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Task(models.Model):
	title = models.CharField(max_length=100)
	details = models.TextField()
	due_date = models.DateField()
	priority = models.CharField(max_length=20)
	created_at = models.DateTimeField(default=timezone.now)
	is_complete = models.BooleanField(default=False)

	def __str__(self):
		return self.title

