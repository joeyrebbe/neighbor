from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class JobPost(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)
    date = models.DateField(("Date"), default=datetime.date.today)
    maxPeople = models.IntegerField()
    compensation = models.TextField(max_length = 250)
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index', kwargs={'post_id': self.id})
        # return reverse('index')
