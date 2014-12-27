__author__ = 'cybran'
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password')