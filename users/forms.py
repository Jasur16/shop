from django import forms
from .models import UserModel, ProfileModel
from django.core.exceptions import ValidationError


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['user', 'created_at']


class LoginForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class RegistrationsForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=(
        forms.PasswordInput(attrs={'class': 'form-control'})
    ), required=True)

    def clean_confirm_password(self, *args, **kwargs):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Пароли не софпадают!')
        return self.cleaned_data

    class Meta:
        model = UserModel
        fields = ['username', 'phone_number', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control'
            })
        }
