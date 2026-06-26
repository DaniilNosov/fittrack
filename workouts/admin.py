from django.contrib import admin

from workouts.models import Workout, WorkoutType


@admin.register(WorkoutType)
class WorkoutTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ["name", "workout_type", "scheduled_date", "is_completed"]
    list_filter = ["workout_type", "is_completed"]
    search_fields = ["name"]
    filter_horizontal = ["participants"]
