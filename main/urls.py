from django.urls import path
from .views import TestTableAPIView

urlpatterns = [
    path("home/", TestTableAPIView.as_view(), name="главная"),
]
