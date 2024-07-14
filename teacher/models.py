from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=20, default='John')
    last_name = models.CharField(max_length=20, default='Doe')
    email = models.EmailField(default='john.doe@example.com')
    country = models.CharField(max_length=20, default='USA')
    date_of_birth = models.DateField(default='2000-01-01')
    class_name = models.CharField(max_length=20, default='Class A')
    year_of_employment = models.PositiveSmallIntegerField(default=2024)
    subject = models.CharField(max_length=20, default='Mathematics')
    id_number = models.PositiveSmallIntegerField(default=12345)
    mode_of_payment = models.CharField(max_length=20, default='Cash')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
