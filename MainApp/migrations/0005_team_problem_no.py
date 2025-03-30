# Generated by Django 5.0 on 2023-12-30 08:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_alter_customuser_usn'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='problem_no',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(25), django.core.validators.MinValueValidator(1)]),
        ),
    ]
