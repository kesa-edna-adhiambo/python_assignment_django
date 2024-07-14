# Generated by Django 5.0.7 on 2024-07-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='class_equipment',
            new_name='class_prefect',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='class_size',
            new_name='number_of_boards',
        ),
        migrations.RemoveField(
            model_name='class',
            name='color_of_chairs',
        ),
        migrations.RemoveField(
            model_name='class',
            name='name_of_class',
        ),
        migrations.AddField(
            model_name='class',
            name='class_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='class',
            name='number_of_chairs',
            field=models.IntegerField(default=0),
        ),
    ]