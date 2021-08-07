from django.urls import path
from portfolio.contact import views

urlpatterns = [
    path('', views.ContactTempalteView.as_view(), name='contact'),
    path('inbox/', views.inbox_page, name='inbox'),

]