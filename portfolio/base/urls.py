from django.urls import path
from portfolio.base import views

urlpatterns = [
    # path('', views.IndexView.as_view(), name="index"),
    path('', views.HomeView.as_view(), name='hero'),
    path('resume/', views.ResumeView.as_view(), name="resume"),
]