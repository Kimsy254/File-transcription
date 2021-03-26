from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User,Client,Worker

## User Login Form (Applied in both worker and client login)
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1','password2']
        widgets = {
                'username': forms.TextInput(attrs={'class':'answer'}),
                'password1': forms.PasswordInput(attrs={'class':'answer'}),
                'password2': forms.PasswordInput(attrs={'class':'answer'}),
                }
        
## Client Registration Form 
class ClientProfileForm(forms.ModelForm):
    class Meta():
        model =  Client
        fields = ['email']
        widgets = {
                'email': forms.EmailInput(attrs={'class':'answer'}),
                }

## Client Profile Update Form
class ClientProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Client
        fields = ['client_profile_pic']

## Worker Registration Form
class WorkerProfileForm(forms.ModelForm):
    class Meta():
        model =  Worker
        fields = ['email']
        widgets = {
                'email': forms.EmailInput(attrs={'class':'answer'}),
                }

## Worker profile update form
class WorkerProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Worker
        fields = ['worker_profile_pic']
        
