from django.urls import path
from apps.returns.views.return_view import ReturnRequestView, ReturnApproveView

urlpatterns = [
    path("", ReturnRequestView.as_view()),
    path("approve/", ReturnApproveView.as_view()),
]