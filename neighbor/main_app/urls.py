from django.urls import path 
# . import everything
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('jobposts/', views.jobposts_index, name='index'), 
    path('jobposts/<int:jobpost_id>/', views.jobposts_detail, name='detail'),
    path('jobposts<int:pk>/update/', views.JobPostUpdate.as_view(), name='jobposts_update'),
    path('jobposts/<int:pk>/delete/', views.JobPostDelete.as_view(), name='jobposts_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('jobposts/create/', views.JobPostCreate.as_view(), name='jobposts_create'), #handle GET & POST 
    # path('volunteer/', views.volunteer_index, name='volunteer_index'),
    # path('profile/', views.profile, name='profile'),
]