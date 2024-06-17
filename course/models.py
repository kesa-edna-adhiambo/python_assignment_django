from django.db import models

# Create your models here.
class Course(models.Model):
    name_of_course = models.CharField(max_length = 20)
    number_of_units = models.IntegerField()
    number_of_students = models.IntegerField()
    course_code = models.IntegerField()
    qualification = models.CharField(max_length = 20)
    registration_characteristic =  models.CharField(max_length = 20)
    number_of_trainers = models.IntegerField()
    scheduled_time = models.TimeField()
    course_requirements = models.CharField(max_length = 20)
    year_introduced = models.IntegerField()

    def __str__(self):
        return f"{self.name_of_course} {self.number_of_units}"