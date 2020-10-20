from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _

class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username','email','password1', 'password2')

class SignInForm(AuthenticationForm):
    username = forms.CharField(
        label=_('Username or Email'), 
        help_text=_('Provide a registered Email or Username to Sign In'),        
    )

class MyUserChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on
    the user
    """    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'is_active','is_staff')
