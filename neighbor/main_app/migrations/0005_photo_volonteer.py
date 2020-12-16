# Generated by Django 3.1.4 on 2020-12-16 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_jobpost_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volonteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('jobpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.jobpost')),
            ],
        ),
    ]
