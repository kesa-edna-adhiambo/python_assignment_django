from django.db import models

# Create your models here.
class Class(models.Model):
    name_of_class = models.CharField(max_length = 20)
    number_of_students = models.IntegerField()
    number_of_tables = models.IntegerField()
    class_size = models.IntegerField()
    class_equipment = models.CharField(max_length = 20)
    class_trainer =  models.CharField(max_length = 20)
    color_of_chairs = models.CharField(max_length = 20)
    number_of_laptops = models.IntegerField()
    number_of_televisions = models.IntegerField()
    number_of_windows = models.IntegerField()

    def __str__(self):
        return f"{self.name_of_class} {self.number_of_students}"
