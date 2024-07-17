from django.db import models
# from django.utils import timezone

# from django.db.models.manager import BaseManager

# Create your models here.
class Classroom(models.Model):
    name_of_class = models.CharField(max_length=255, default='', null=False)   
    number_of_students = models.IntegerField()
    number_of_tables = models.IntegerField()
    number_of_chairs = models.IntegerField(default=0)
    number_of_boards = models.IntegerField()
    class_trainer =  models.CharField(max_length = 20)
    class_prefect = models.CharField(max_length = 20)
    number_of_laptops = models.IntegerField()
    number_of_televisions = models.IntegerField()
    number_of_windows = models.IntegerField()

    # objects : BaseManager ["Classroom"]

    def __str__(self):
        return f"{self.name_of_class} {self.number_of_students}"
