from portfolio.accounts.manager import PortfolioUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class PortfolioUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, )

    USERNAME_FIELD = 'email'

    objects = PortfolioUserManager()
