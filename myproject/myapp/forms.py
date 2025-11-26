from django import forms
from .models import Person

class StudentForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'place']

