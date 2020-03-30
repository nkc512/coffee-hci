# Generated by Django 2.1.1 on 2018-10-11 11:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20181011_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blend',
            name='city',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^a-zA-Z]*$', 'only alphabet')]),
        ),
        migrations.AlterField(
            model_name='blend',
            name='state',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^a-zA-Z]*$', 'only alphabet')]),
        ),
    ]