from django.contrib import admin
from .models import JobPost, JobApplicationMap, Photo, Skill, Profile, ZipCode         

# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# from .models import CustomUser

# Register your models here.
admin.site.register(JobPost)
admin.site.register(JobApplicationMap)
admin.site.register(Photo)
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(ZipCode)

# class CustomUserInline(admin.StackedInline):
#     model = CustomUser
#     can_delete = True
#     verbose_name_plural = 'custom user'

# class UserAdmin(BaseUserAdmin):
#     inlines = (CustomUserInline,)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
