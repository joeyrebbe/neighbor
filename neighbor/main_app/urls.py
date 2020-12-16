from django.urls import path 
# . import everything
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('job-posts/', views.job_posts_index, name='index'), 
    path('job-posts/create/', views.JobPostCreate.as_view(), name='job_posts_create'), #handle GET & POST 
    path('accounts/signup/', views.signup, name='signup'),
]