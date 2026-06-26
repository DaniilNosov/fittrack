from django.contrib.auth.forms import UserCreationForm

from users.models import Athlete


class AthleteCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Athlete
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "fitness_level",
            "bio",
        )
