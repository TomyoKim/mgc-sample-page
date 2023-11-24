from django.urls import path

from . import views

app_name = "attendance"

urlpatterns = [
    path("", views.Attendance.as_view(), name="index"),
]