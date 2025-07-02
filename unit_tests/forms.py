from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 0:
            raise ValidationError('Age < 0')
        
    class Meta:
        model = User
        fields = ('user_name', 'email', 'age', 'birth_date')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())