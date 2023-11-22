from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import AnonymousUser
from .models import User

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        userModel = User
        try:
            user = userModel.objects.get(email=username)
        except userModel.DoesNotExist:
            return AnonymousUser()
        else:
            if user.check_password(password):
                return user
        return AnonymousUser()