from django.contrib.auth import get_user_model


UserModel = get_user_model()


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)