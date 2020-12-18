from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

# might need: from localflavor.models import USStateField

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
        return reverse('detail', kwargs={'jobpost_id': self.id})
        # return reverse('index')

class Photo(models.Model):
    url = models.CharField(max_length=200) #we store url where it hosted (AWS)
    jobpost = models.ForeignKey(JobPost, on_delete=models.CASCADE) #on_delete - means if we delete this it will delete the chain
    
    def __str__(self):
        #cat_id will referrence cat property above
        return f"Photo for jobpost_id: {self.jobpost_id} @{self.url}" 


class Skill(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)
            
    def __str__(self):
        return self.name

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  bio = models.CharField(max_length=255, default='Enter your bio here!')
  skills = models.ManyToManyField(Skill)
  zipcode = models.CharField(max_length=5, default=12345)

  def __str__(self):
      return self.name

  def get_absolute_url(self):
      return reverse('profile_detail', kwargs={'profile_id': self.id})
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class JobApplicationMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobPost = models.ForeignKey(JobPost, on_delete=models.CASCADE)

    
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

