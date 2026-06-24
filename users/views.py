from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from users.forms import AthleteCreationForm
from users.models import Athlete


class AthleteListView(ListView):
    model = Athlete
    context_object_name = "athletes"
    template_name = "users/athlete_list.html"


class AthleteDetailView(DetailView):
    model = Athlete
    context_object_name = "athlete"
    template_name = "users/athlete_detail.html"


class RegisterView(CreateView):
    model = Athlete
    form_class = AthleteCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("workouts:workout-list")

    def form_valid(self, form):
        athlete = form.save()
        login(self.request, athlete)
        return redirect(self.success_url)
