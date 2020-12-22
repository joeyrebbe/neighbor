from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


SKILLS = (
    ('1', 'Cleaning'), 
    ('2', 'Gardening'),
    ('3', 'Electrical'),
    ('4', 'Babysitting'),
    ('5', 'Pest Control'),
    ('6', 'DJing'),
    ('7', 'General Labor'),
    ('8', 'Handyperson'),
    ('9', 'Computer Skills'),
    ('10', 'Auto Mechanic'),
    ('11', 'Carpentry'),
    ('12', 'Power Tools'),
    ('13', 'Organizer'),
    ('14', 'Music Teaching'),
    ('15', 'Animal Handling'),
    ('16', 'Photography'),
    ('17', 'Writing'),
    ('18', 'Art'),
    ('19', 'Doomsday Prepping'),
    ('20', 'Cooking'),
    ('21', 'Sewing'),
    ('22', 'Plumbing'),
    ('23', 'Welding'),
    ('24', 'Quantum Physics'),
    ('25', 'Intimidation')
)

class JobPost(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)
    date = models.DateField(("Date"), default=datetime.date.today)
    maxPeople = models.IntegerField()
    compensation = models.TextField(max_length = 250)
    zipcode = models.CharField(max_length=5, default=12345)
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


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  bio = models.CharField(max_length=255, default='Enter your bio here!')
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

class Skill(models.Model):
    skill = models.CharField(
        max_length=2,
        choices=SKILLS,
        default=SKILLS[0][0]
    )  
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.get_skill_display()}"
class JobApplicationMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobPost = models.ForeignKey(JobPost, on_delete=models.CASCADE)

    jobPost = models.ForeignKey(JobPost, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"user_id: {self.user_id}; jobPost_id: {self.jobPost_id}" 
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'jobPost_id'],
                name='user_id_job_post_id_unique',
            ),
        ]
