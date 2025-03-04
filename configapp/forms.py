from django import forms
from .models import Student, Fanlar

class FanlarForm(forms.ModelForm):
    class Meta:
        model = Fanlar
        fields = ['title']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['photo', 'full_name', 'phone_number', 'address', 'fan']
