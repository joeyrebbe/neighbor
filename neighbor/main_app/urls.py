from django.urls import path 
# . import everything
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('posts/', views.posts_index, name='index'), 
    # path('posts/<int:post_id>/', views.posts_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('volunteer/', views.volunteer_index, name='volunteer_index'),
    # path('profile/', views.profile, name='profile'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'), #handle GET & POST 
]