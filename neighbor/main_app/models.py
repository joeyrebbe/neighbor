from django.db import models
import datetime
from django.contrib.auth.models import User 
from django.urls import reverse

# might need: from localflavor.models import USStateField

# Create your models here.

# class CustomUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     zip_code = models.CharField(max_length = 5) # if not working, try pip install django-localflavor
    # if pip install, change params to (_("zip code"), max_length=5, default=43701)
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
        return reverse('detail', kwargs={'jobpost_id': self.id})
        # return reverse('index')

class Photo(models.Model):
    url = models.CharField(max_length=200) #we store url where it hosted (AWS)
    jobpost = models.ForeignKey(JobPost, on_delete=models.CASCADE) #on_delete - means if we delete this it will delete the chain
    
    def __str__(self):
        #cat_id will referrence cat property above
        return f"Photo for jobpost_id: {self.jobpost_id} @{self.url}" 


# class Profile(models.Model):
#   name = models.CharField(max_length=50)
  
#   def __str__(self):
#       return self.name

#   def get_absolute_url(self):
#       return reverse('volonteer_detail', kwargs={'pk': self.id})

class JobApplicationMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobPost = models.ForeignKey(JobPost, on_delete=models.CASCADE)
# <<<<<<< HEAD
    
    def __str__(self):
        return f"user_id: {self.user_id}; jobPost_id: {self.jobPost_id}" 
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'jobPost_id'],
                name='useri_id_job_post_id_unique',
            ),
        ]

class Skill(models.Model):
    value = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)
       
    def __str__(self):
        return self.value
# =======




# >>>>>>> main
