# Generated by Django 5.0.7 on 2024-07-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(default='08:00')),
                ('end_time', models.TimeField(default='17:00')),
                ('course', models.CharField(default='General Studies', max_length=20)),
                ('classroom', models.CharField(default='Classroom A', max_length=20)),
                ('day_of_the_week', models.CharField(default='Monday', max_length=20)),
            ],
        ),
    ]
