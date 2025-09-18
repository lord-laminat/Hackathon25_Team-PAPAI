from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """
    Basic User model
    """

    email = models.EmailField(verbose_name='email address', unique=True)
    points = models.IntegerField(verbose_name='points', default=0)

    # TODO: UsersGroup Foreign Key
    # users_group = models.ForeignKey()