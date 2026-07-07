from django.test import TestCase
from django.urls import reverse

from users.models import Athlete
from workouts.models import Workout, WorkoutType
from workouts.forms import WorkoutForm


class WorkoutTypeModelTest(TestCase):
    def test_str_returns_name(self):
        workout_type = WorkoutType.objects.create(name="Cardio")
        self.assertEqual(str(workout_type), "Cardio")


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout_type = WorkoutType.objects.create(name="Strength")
        self.workout = Workout.objects.create(
            name="Morning Workout",
            scheduled_date="2026-06-26",
            workout_type=self.workout_type,
        )

    def test_str_returns_name(self):
        self.assertEqual(str(self.workout), "Morning Workout")

    def test_default_is_completed_false(self):
        self.assertFalse(self.workout.is_completed)


class WorkoutFormTest(TestCase):
    def setUp(self):
        self.workout_type = WorkoutType.objects.create(name="Cardio")

    def test_valid_form(self):
        form = WorkoutForm(data={
            "name": "Evening Run",
            "description": "Easy run",
            "scheduled_date": "2026-06-26",
            "is_completed": False,
            "workout_type": self.workout_type.pk,
            "participants": [],
        })
        self.assertTrue(form.is_valid())

    def test_form_missing_name(self):
        form = WorkoutForm(data={
            "name": "",
            "scheduled_date": "2026-06-26",
            "workout_type": self.workout_type.pk,
        })
        self.assertFalse(form.is_valid())


class WorkoutListViewTest(TestCase):
    def setUp(self):
        self.athlete = Athlete.objects.create_user(
            username="testathlete",
            password="testpass123",
        )
        self.client.login(username="testathlete", password="testpass123")
        self.workout_type = WorkoutType.objects.create(name="Cardio")
        self.workout = Workout.objects.create(
            name="Morning Workout",
            scheduled_date="2026-06-26",
            workout_type=self.workout_type,
        )

    def test_workout_list_url_exists(self):
        response = self.client.get(reverse("workouts:workout-list"))
        self.assertEqual(response.status_code, 200)

    def test_workout_list_uses_correct_template(self):
        response = self.client.get(reverse("workouts:workout-list"))
        self.assertTemplateUsed(response, "workouts/workout_list.html")

    def test_toggle_workout_completion(self):
        response = self.client.get(
            reverse("workouts:workout-toggle", args=[self.workout.pk])
        )
        self.workout.refresh_from_db()
        self.assertTrue(self.workout.is_completed)
        self.assertEqual(response.status_code, 302)
