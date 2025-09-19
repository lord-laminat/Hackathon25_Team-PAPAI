from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    """
    Basic User model
    """

    email = models.EmailField(verbose_name='email address', unique=True)
    points = models.IntegerField(verbose_name='points', default=0)

    # TODO: UsersGroup Foreign Key
    # users_group = models.ForeignKey()

    
    def __str__(self):
        return f"User: {self.get_full_name()} - {self.email} ({self.points} points)"


    class Meta:
        default_related_name = 'custom_users'

        permissions = [] # TODO: add permisions