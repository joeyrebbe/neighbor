# Generated by Django 3.1.2 on 2020-12-21 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20201221_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='zipcode',
            field=models.CharField(default=12345, max_length=5),
        ),
    ]
