from django.conf import settings
from django.db import models

class WorkoutType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    scheduled_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.PROTECT, related_name="workouts")
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="workouts",
        blank=True,
    )

    class Meta:
        ordering = ["scheduled_date"]

    def __str__(self):
        return self.name
