from django import forms
from todo.models import todomodel
class todoform(forms.ModelForm):
	class Meta:
	fields='_all_'