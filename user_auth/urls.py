from django.urls import path

from . import views

app_name = "user_auth"
urlpatterns = [
    path("login", views.Login.as_view(), name="login"),
    path("logout", views.Logout.as_view(), name="logout"),
    path("signup", views.SignUp.as_view(), name="signup"),
    path("changepassword", views.ChangePassword.as_view(), name="changepassword"),
]