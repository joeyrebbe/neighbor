from django.contrib import admin
from .models import JobPost, JobApplicationMap, Skill, Photo            

# Register your models here.
admin.site.register(JobPost)
admin.site.register(JobApplicationMap)
admin.site.register(Photo)
admin.site.register(Skill)
