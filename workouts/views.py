from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from workouts.forms import WorkoutForm
from workouts.models import Workout

class WorkoutListView(LoginRequiredMixin, ListView):
    model = Workout
    context_object_name = "workouts"
    template_name = "workouts/workout_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        visits = self.request.session.get("visits", 0)
        self.request.session["visits"] = visits + 1
        context["visits"] = visits + 1
        return context

class WorkoutDetailView(LoginRequiredMixin, DetailView):
    model = Workout
    template_name = "workouts/workout_detail.html"
    context_object_name = "workout"


class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = "workouts/workout_form.html"
    success_url = reverse_lazy("workouts:workout-list")


class WorkoutUpdateView(LoginRequiredMixin, UpdateView):
    model = Workout
    form_class = WorkoutForm
    template_name = "workouts/workout_form.html"
    success_url = reverse_lazy("workouts:workout-list")


class WorkoutDeleteView(LoginRequiredMixin, DeleteView):
    model = Workout
    template_name = "workouts/workout_form.html"
    success_url = reverse_lazy("workouts:workout-list")

@login_required
def toggle_workout_completion(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    workout.is_completed = not workout.is_completed
    workout.save()
    return redirect("workouts:workout-list")
