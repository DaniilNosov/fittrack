from django.urls import path

from users import views

app_name = "users"
urlpatterns = [
    path("", views.AthleteListView.as_view(), name="athlete-list"),
    path("<int:pk>/", views.AthleteDetailView.as_view(), name="athlete-detail"),
    path("register/", views.RegisterView.as_view(), name="register"),
]