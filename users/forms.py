from django import forms

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from django.contrib.auth.forms import PasswordChangeForm 

 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

 

class MessageForm(forms.Form):
    recipient = forms.CharField(label='To', max_length=100)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    file_upload = forms.FileField(label='Attach file', required=False)


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password= forms.CharField(
        label="Ancien mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'mot de passe actuel'}),
        error_messages={'required': "Veuillez entrer votre ancien mot de passe."}
    )
    new_password1 = forms.CharField(
        label="Nouveau mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'nouveau mot de passe'}),
        error_messages={'required': "Veuillez entrer votre nouveau mot de passe."}
    )
    new_password2 = forms.CharField(
        label="Confirmez le nouveau mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer votre nouveau mot de passe'}),
        error_messages={'required': "Veuillez confirmer votre nouveau mot de passe."})
    
    