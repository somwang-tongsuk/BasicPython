from django import forms
from .models import Questions

class QA(forms.ModelForm):
	class Meta:
		model = Questions
		fields = ('name','category','title','detail')