from django import forms
from .models import Student


class CustomStudentForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    school = forms.CharField(max_length=100)
    place = forms.CharField(max_length=100)
    class_choice = forms.IntegerField()

    class Meta:
        model = Student
        fields = {'name', 'school', 'place', 'class_choice'}


class CustomResultsForm(forms.ModelForm):
    accuracy = forms.FloatField()
    cpm = forms.FloatField()
    wpm = forms.FloatField()

    class Meta:
        model = Student
        fields = {'accuracy', 'cpm', 'wpm'}
