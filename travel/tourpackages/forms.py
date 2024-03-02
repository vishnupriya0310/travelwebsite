# forms.py
from django import forms

class IntegerDateForm(forms.Form):
    integer_value = forms.IntegerField()
    date_value = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)