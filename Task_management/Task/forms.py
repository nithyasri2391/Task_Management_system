from django import forms
from django.forms import ModelForm
from .models import *

class CreateForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
	description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter description...'}))
	due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Enter due date...'}))


	class Meta:
		model = Create
		fields = '__all__'