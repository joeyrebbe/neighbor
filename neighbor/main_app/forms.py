from django import forms
from .models import JobPost, Skill
from django.forms import ModelForm
class SearchingForm(forms.ModelForm):
  class Meta:
    model = JobPost
    fields = ['name', 'zipcode']

class SkillForm(ModelForm):

  class Meta: 
    model = Skill
    fields = ['skill']