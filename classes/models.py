from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Classroom(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=120)
    grade = models.IntegerField()
    year = models.IntegerField()

    def get_absolute_url(self):
        return reverse('classroom-detail', kwargs={'classroom_id': self.id})


class Student(models.Model):
    male = "M"
    female = "F"
    name = models.CharField(max_length=120)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=[(male, "male"), (female, "female")])
    exam_grade = models.IntegerField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
