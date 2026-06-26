from django.test import TestCase
from django.urls import reverse
from users.models import FitnessLevel, Athlete


class FitnessLevelModelTest(TestCase):
    def test_str_returns_name(self):
        level = FitnessLevel.objects.create(name="test")
        self.assertEqual(str(level), "test")

class AthleteModelTest(TestCase):
    def setUp(self):
        self.level = FitnessLevel.objects.create(name="test")
        self.athlete = Athlete.objects.create_user(
            username="testathlete",
            password="testpass123",
            fitness_level=self.level,
        )

    def test_str_returns_username(self):
        self.assertEqual(str(self.athlete), "testathlete")

    def test_athlete_has_fitness_level(self):
        self.assertEqual(self.athlete.fitness_level, self.level)

class AthleteListViewTest(TestCase):
    def setUp(self):
        self.athlete = Athlete.objects.create_user(
            username="testathlete",
            password="testpass123",
        )
        self.client.login(username="testathlete", password="testpass123")

    def test_athlete_list_url_exists(self):
        response = self.client.get(reverse("users:athlete-list"))
        self.assertEqual(response.status_code, 200)

    def test_athlete_uses_correct_template(self):
        response = self.client.get(reverse("users:athlete-list"))
        self.assertTemplateUsed(response, "users/athlete_list.html")
