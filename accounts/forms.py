from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username','email','password1', 'password2')

class SignInForm(AuthenticationForm):
    username = forms.CharField(
        label='Username or Email', 
        help_text='Provide a registered Email or Username to Sign In',        
    )
