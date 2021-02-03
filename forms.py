from django import forms
from django.forms import ModelForm
from .models import Location

class LocationForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Location
        fields = '__all__'