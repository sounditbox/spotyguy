from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        email = username
        user_model = get_user_model()
        if email is None or password is None:
            return
        try:
            user = user_model.objects.get(email=email)
            if user.check_password(password):
                return user
            return
        except user_model.DoesNotExist:
            return

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
        return user

