from django.urls import path
from portfolio.contact import views

urlpatterns = [
    path('', views.ContactView.as_view(), name='contact'),
]