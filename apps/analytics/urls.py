from django.urls import path
from apps.analytics.views.analytics_viewset import DashboardView

urlpatterns = [
    path("dashboard/", DashboardView.as_view()),
]