from django import forms
from django.forms.models import ModelForm

from .models import Tasks


class TaskForm(ModelForm):
    class Meta:

        model = Tasks

        fields = ["title", "content", "end_by"]

        widgets = {"end_by": forms.DateInput(attrs={"type": "datetime-local"})}
