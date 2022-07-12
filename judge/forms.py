from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True, label='Email',
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(max_length=20, label='Username',
                    widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    
    # Django Meta class used to transfer information about the model to the Django forms
    class Meta:
        model = User
        fields = ('username','email','password')