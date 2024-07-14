# Generated by Django 5.0.7 on 2024-07-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_name',
            field=models.CharField(default='Lovelace ', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='enrollment_year',
            field=models.PositiveSmallIntegerField(default=2024),
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.CharField(default='JavaScript', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='code',
            field=models.PositiveSmallIntegerField(default=12345),
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(default='USA', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='john.doe@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='John', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='Doe', max_length=20),
        ),
    ]
