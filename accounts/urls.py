from django.urls import path
from django.contrib.auth import views as auth_views

from . import views, forms

app_name = 'accounts'

urlpatterns = [
    # Index
    path('', views.IndexView.as_view(), name='index'),

    # login
    path('login/', auth_views.LoginView.as_view(
            template_name='accounts/authenticate.html',
            redirect_authenticated_user=True,
            extra_context={
                'title': 'Login'
            },
            authentication_form = forms.SignInForm,
        ), 
        name='login',        
    ),

    # logout
    path('logout/', auth_views.LogoutView.as_view(
        template_name='accounts/logout.html'), 
        name='logout',        
    ),

    # signup
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
