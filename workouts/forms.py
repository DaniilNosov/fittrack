from django import forms

from workouts.models import Workout


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = [
            "name",
            "description",
            "scheduled_date",
            "is_completed",
            "workout_type",
            "participants",
        ]
        widgets = {
            "scheduled_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "participants": forms.CheckboxSelectMultiple(),
        }
