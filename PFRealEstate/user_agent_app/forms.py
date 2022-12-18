from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import widgets

UserModel = get_user_model()

class CustomUserForms(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserForms, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Write username'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Write password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat password'

    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2')

class CustomAuthLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomAuthLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserModel
        fields = ('username', 'password')


