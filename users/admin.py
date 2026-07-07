from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import FitnessLevel, Athlete


@admin.register(FitnessLevel)
class FitnessLevelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Athlete)
class AthleteAdmin(UserAdmin):
    list_display = ["username", "email", "first_name", "last_name", "fitness_level"]
    list_filter = ["fitness_level"]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("fitness_level", "bio")}),
    )
