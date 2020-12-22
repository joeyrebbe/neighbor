from django.shortcuts import render, redirect
from .models import JobPost, Photo, JobApplicationMap, Profile
from .models import *
from .forms import SearchingForm, SkillForm
from django.http import HttpResponse

# Add the two imports below for Login New User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3

#these lines below for HandleErrors Functions
import json
import traceback 
import sys 

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollectoraleksei'

def signup(request):
  error_message = ""
  if request.method == "POST":
    #then we want to create user form object that includes the data from the browser
    form = UserCreationForm(request.POST) # < - object saved in memory
    if form.is_valid():
      # save user to DB
      user = form.save()
      # login our user (coming from auth)
      login(request, user) # <- this will create session cookie with sent back n forth on every request
      #redirect the user to the index
      return redirect('index') # index is coming frm name urls.py
    else: 
      error_message = 'Invalid sign up - try again'

  # A bad POST or a GET request, we'll render signup.html with an empty form 
  form = UserCreationForm()
  #^ this gives us the Blank Form
  context = {'form': form, 'error_message': error_message} # we injectin form and error to our html page
  return render(request, 'registration/signup.html', context) 

def home(request):
  return render(request, 'home.html') 

  # Define the ABOUT/ view
# def about(request):
#   return HttpResponse('<h1>This is About Page</h1>') # simmiluar to res.send

def about(request):
    return render(request, 'about.html') #instead of HTTPResponse we can use a template

  # A bad POST or a GET request, we'll render signup.html with an empty form 

class JobPostUpdate(LoginRequiredMixin, UpdateView): 
  model = JobPost
  fields = ['description', 'date', 'maxPeople', 'compensation', 'zipcode'] 

class JobPostDelete(LoginRequiredMixin, DeleteView):
  model = JobPost
  success_url = '/jobposts/'


class JobPostCreate(LoginRequiredMixin, CreateView):
  model = JobPost
  fields = ['name', 'description', 'date', 'maxPeople', 'compensation', 'zipcode']

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the job post. We're overriding the CreateView's form_valid method to assign the logged in user,
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UpdateView):
  model = Profile
  fields = ['name', 'bio', 'zipcode']

def profile(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  # skills = Skill.objects.filter(user=request.user)
  print(profile.skill_set)
  skill_form = SkillForm()
  return render(request, 'profile/detail.html', {
    'profile': profile, 'skill_form': skill_form
    })

# def assoc_skill(request, profile_id, skill_id):

#   Profile.objects.get(id=profile_id).skills.add(skill_id)
  
#   return redirect('profile_index', profile_id=profile_id)


def add_skill(request, profile_id):

  form = SkillForm(request.POST)

  if form.is_valid():

    new_skill = form.save(commit=False)
    new_skill.profile_id = profile_id
    new_skill.save()

  return redirect('profile_detail', profile_id=profile_id)


def jobposts_index(request):
  jobposts = JobPost.objects.all()

  form = SearchingForm(request.POST or None)
  context = {
    "jobposts": jobposts,
    "form": form,
  }
  
  if request.method == 'POST':
    jobposts = JobPost.objects.filter(name__icontains=form['name'].value())
    context = {
    "form": form,
    "jobposts": jobposts,
    }
  return render(request, 'jobposts/index.html', context)

def job_application_create(request):
  # print('CHECKPOINT 1 *****')
  # print(request.body)
  # print(request.POST['user_id'])
  # print(request.POST['job_post_id'])
  # print(request.POST.jobpost_id)
  try:
    user_id = request.POST['user_id']
    job_post_id = request.POST['job_post_id']
    JobApplicationMap.objects.create(user_id=user_id, jobPost_id=job_post_id)
    return redirect('index')
  except Exception as err:
    print(err)
    return render(request, 'jobposts/applied.html')

  

def jobposts_detail(request, jobpost_id):
  jobpost = JobPost.objects.get(id=jobpost_id)
 
  print('**************')
  print(jobpost)

  # job_applicant = JobPost.objects.get(id=user_id)
  # volonteer = volonteer.JobApplicationMap_set.all
  return render(request, 'jobposts/detail.html', {'jobpost': jobpost})

def jobposts_add_application(request, jobpost_id):
  jobpost = JobPost.objects.get(id=jobpost_id)
  return render(request, 'jobposts/apply.html', {
    'jobpost': jobpost,
    'user': request.user
  })



def add_photo(request, jobpost_id):
  #<input type="file" name="photo-file"> <-- the client input
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None) # if there is no photo-file, the property will be NONE
  if photo_file:
    s3 = boto3.client('s3')
    # initiating connection db and aws
    # uuid.uuid4().hex[:6] <- generate an unique "key" for S3 and append photo file name
    # if you want to specify which photo extention you allow, do it here in the key
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):] # ":]" - slicer that cut rest after dot
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # if I want to delete Photo
      # print(dir(s3)) - if we want to see all available methods
      # s.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=f"media/{item.file.name}")

      # generate url string to save in our db
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # Create Photo we can assign to jobpost_id or jobpost (if you have a jobpost object)
      Photo.objects.create(url=url, jobpost_id=jobpost_id)
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', jobpost_id=jobpost_id)


