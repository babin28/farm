from django import forms
from .models import LoginEntry

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginEntry
        fields = ['username', 'phone']
