from django.contrib.auth.models import AbstractUser
from django.db import models


class FitnessLevel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Athlete(AbstractUser):
    fitness_level = models.ForeignKey(
        FitnessLevel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="athletes",
    )
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
