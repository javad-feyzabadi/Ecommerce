from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from . models import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ('email','phone_number','full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('Password Dont Match')
        return cd['password2']

    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()

    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text = "You Cant Change Password Using <a href =\"../password/\"> This Form </a>")

    class Meta:
        model = User
        fields = ('email','phone_number','full_name','password','last_login')