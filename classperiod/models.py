from django.db import models
# from django.db.models.manager import BaseManager


# Create your models here.
class ClassPeriod(models.Model):
    start_time = models.TimeField(default='08:00')
    end_time = models.TimeField(default='17:00')
    course = models.CharField(max_length=20, default='General Studies')
    classroom = models.CharField(max_length=20, default='Classroom A')
    day_of_the_week = models.CharField(max_length=20, default='Monday')

    # objects : BaseManager ["ClassPeriod"]

    def __str__(self):
        return f"{self.start_time} {self.end_time}"
