from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model


class EmailAuthBackend(ModelBackend):
    """Authenticates using an email Address."""

    def authenticate(self, request, username=None, password=None,**kwargs):        
        User = get_user_model()

        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
