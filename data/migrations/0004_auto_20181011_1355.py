# Generated by Django 2.1.1 on 2018-10-11 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20181011_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blend',
            name='img',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
    ]