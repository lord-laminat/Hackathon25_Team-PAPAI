from django.db import models
from django.contrib.auth.models import AbstractUser
from .enums import Rank


class CustomUser(AbstractUser):
    """
    Basic implementation of **CustomUser** model for *Django ORM*.
    It inherits from `django.contrib.auth.models.AbstractUser`
    and using all fields from it.

    Args:
        email: Unique `EmailField` 
        skills: `JSONField` that contains json object describing the user's skills
        experience_points: `PositiveIntegerField` that contains XP
        mana_points: `PositiveIntegerField` that contains mana points for exchanging onto merch and other awards
        rank: `PositiveSmallIntegerField` created via Rank enum in `enums.py` and describes current user's rank
    """

    email = models.EmailField(verbose_name='email address', unique=True)
    skills = models.JSONField(verbose_name='skills', default=dict())
    experience_points = models.PositiveIntegerField(verbose_name='experience_points', default=0)
    mana_points = models.PositiveIntegerField(verbose_name='mana_points', default=0)
    rank = models.PositiveSmallIntegerField(verbose_name='rank', choices=Rank.choices(), default=Rank.BEGINNER.value)


    def __str__(self):
        return f"User: {self.get_full_name()} - {self.email} | {self.experience_points} points ({self.rank} rank)"


    class Meta:
        default_related_name = 'custom_users'

        permissions = [
            # ('see_rank_beginner', 'Can see tasks for Beginner rank')
            # ('see_rank_intermediate', 'Can see tasks for Intermediate rank')
            # ('see_rank_advanced', 'Can see tasks for Advanced rank')
        ] # TODO: add permissions