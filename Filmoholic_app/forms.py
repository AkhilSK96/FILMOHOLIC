from django import forms
from .models import User
from .models import Movies


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone']
        widgets = {
            'password': forms.PasswordInput(), 
        }


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'