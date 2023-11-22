from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        userModel = get_user_model()
        try:
            user = userModel.objects.get(email=username)
        except userModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None