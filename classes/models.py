from django.db import models
from django.urls import reverse

class Classroom(models.Model):
	subject = models.CharField(max_length=120)
	grade = models.IntegerField()
	year = models.IntegerField()

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})
