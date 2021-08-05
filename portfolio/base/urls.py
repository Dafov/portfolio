from django.urls import path
from portfolio.base import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]