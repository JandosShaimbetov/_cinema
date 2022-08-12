from django.urls import path

from user.views import FeedbackList, LoginView, RegisterView

urlpatterns = [
    path("reg/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("feedback/", FeedbackList.as_view(), name="feedback"),
]
