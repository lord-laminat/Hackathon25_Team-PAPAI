from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # user_fields = UserAdmin.user_fields + ('email', 'skills', 'experience_points', 'mana_points', 'rank', )

    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('skills', 'experience_points', 'mana_points', 'rank', )}),
    )
