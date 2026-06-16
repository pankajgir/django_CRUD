from django import forms
from .models import student

class addstudentform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student Name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email Address'
            }),

            'course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Course'
            }),

            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter City'
            }),
        }
