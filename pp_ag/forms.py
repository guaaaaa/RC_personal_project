from django import forms
from .models import User, Case
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .grade_ten_student_data import Twenty_Twenty_Grade_Ten_Student_Data
from django.core.exceptions import ValidationError
from django.contrib.auth import models

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True,
                            help_text='Required. Please use a valid Ridley College Email.')
    class Meta:
        model = models.User
        fields = ('username','email', 'password1', 'password2')
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Please use Firstname_Lastname as your username'
        self.fields['email'].widget.attrs['placeholder'] = 'Firstname_lastname@Ridleycollege.com'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

        
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if email not in Twenty_Twenty_Grade_Ten_Student_Data:
            ValidationError("Please make sure you are a grade 10 student and use valid Ridley College Email.")
        return email


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields=('__all__')
    
    
        widgets = {
            'project_name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter description here'}),
        }