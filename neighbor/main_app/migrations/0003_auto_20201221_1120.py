# Generated by Django 3.1.2 on 2020-12-21 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201221_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill',
            field=models.CharField(choices=[('1', 'Cleaning'), ('2', 'Gardening'), ('3', 'Electrical'), ('4', 'Babysitting'), ('5', 'Pest Control'), ('6', 'DJing'), ('7', 'General Labor'), ('8', 'Handyperson'), ('9', 'Computer Skills')], default='1', max_length=1),
        ),
    ]