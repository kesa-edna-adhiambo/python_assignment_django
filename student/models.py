from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20, default='John')
    last_name = models.CharField(max_length=20, default='Doe')
    email = models.EmailField(default='john.doe@example.com')
    country = models.CharField(max_length=20, default='USA')
    date_of_birth = models.DateField(default='2000-01-01') 
    code = models.PositiveSmallIntegerField(default=12345)
    class_name = models.CharField(max_length=20, default='Lovelace ')
    subject = models.CharField(max_length=20, default='JavaScript')
    enrollment_year = models.PositiveSmallIntegerField(default=2024)
    # student_image = models.ImageField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



