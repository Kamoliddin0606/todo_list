from dataclasses import fields
from django import forms
from .models import ToDoList
from django.contrib.admin import widgets
class ToDoForm(forms.ModelForm):
    start_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    end_time = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    class Meta:
        model = ToDoList
        fields = ['title', 'body', 'start_time', 'end_time']
        