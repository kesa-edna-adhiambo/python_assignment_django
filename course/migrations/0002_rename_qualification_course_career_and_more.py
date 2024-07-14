# Generated by Django 5.0.7 on 2024-07-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='qualification',
            new_name='career',
        ),
        migrations.RemoveField(
            model_name='course',
            name='registration_characteristic',
        ),
        migrations.AddField(
            model_name='course',
            name='amount_per_semester',
            field=models.IntegerField(default=0),
        ),
    ]
