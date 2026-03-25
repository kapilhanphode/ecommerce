
from django.urls import path
from apps.accounts.views.auth_view import RegisterView, LoginView, RefreshView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("refresh/", RefreshView.as_view()),
]