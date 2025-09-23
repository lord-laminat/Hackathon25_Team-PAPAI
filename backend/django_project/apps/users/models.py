from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MinLengthValidator


class CustomUser(AbstractUser):
    """
    Basic implementation of **CustomUser** model for *Django ORM*.
    It inherits from `django.contrib.auth.models.AbstractUser`
    and using all fields from it.

    Args:
        email: Unique `EmailField` 
    """

    email = models.EmailField(verbose_name='email address', unique=True)

    @property
    def total_exp(self):
        return self.progress.exp if self.progress else 0


    @property
    def total_mana(self):
        return self.progress.mana if self.progress else 0


    def __str__(self):
        rank_str = f" (Rank: {self.progress.current_rank.name if hasattr(self, 'progress') else 'No rank'})" if self.progress else ""
        return f"User: {self.get_full_name()} - {self.email} {rank_str}"


    class Meta:
        default_related_name = 'custom_users'

        permissions = [
            # ('see_rank_beginner', 'Can see tasks for Beginner rank')
            # ('see_rank_intermediate', 'Can see tasks for Intermediate rank')
            # ('see_rank_advanced', 'Can see tasks for Advanced rank')
        ] # TODO: add permissions


class Rank(models.Model):
    level = models.PositiveSmallIntegerField(verbose_name='level', default=0, unique=True)
    name = models.CharField(max_length=100, unique=True)
    required_exp = models.PositiveIntegerField(verbose_name='required exp', default=0)
    # required_missions = models.ManyToManyField('Mission', through='RankMission', blank=True)
    # required_competences = models.ManyToManyField(Competence, through='RankCompetence', blank=True)


    class Meta:
        ordering = ['required_exp']


    def __str__(self):
        return f'{self.name}'


class Competence(models.Model):
    name = models.CharField(verbose_name='name', max_length=100, unique=True, validators=[MinLengthValidator(2)])
    description = models.CharField(verbose_name='description', blank=True)


    class Meta:
        verbose_name = 'Competence'
        verbose_name_plural = 'Competences'
        indexes = [models.Index(fields=['name'])]
        ordering = ['name']
    

    def __str__(self):
        return f'{self.name}'


class UserProgress(models.Model):
    """
    Args:
        exp: `PositiveIntegerField` that contains XP
        mana: `PositiveIntegerField` that contains mana points for exchanging onto merch and other awards
        rank: `ForeignKey` referencing to the Rank table and describes current user's rank
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='progress')
    exp = models.PositiveIntegerField(verbose_name='exp', default=0, validators=[MinValueValidator])
    mana = models.PositiveIntegerField(verbose_name='mana_points', default=0, validators=[MinValueValidator])
    rank = models.ForeignKey(Rank, verbose_name='rank', on_delete=models.PROTECT, blank=True, null=True)
    compenteces = models.ManyToManyField(Competence, verbose_name='Competences', through='UserCompetence', related_name='progress_users')


class UserCompetence(models.Model):
    progress = models.ForeignKey('UserProgress', on_delete=models.CASCADE, related_name='competences_levels')
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0, validators=[MinLengthValidator(0)])


    class Meta:
        unique_together = ('progress', 'competence')
