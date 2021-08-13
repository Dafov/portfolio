from django.urls import path
from portfolio.contact import views

urlpatterns = [
    path('', views.CreateMessageView.as_view(), name='contact'),
    path('inbox/', views.InboxPageView.as_view(), name='inbox'),

    path('message/<str:id>/', views.MessageDetailView.as_view(), name='message'),
    path('message/delete/<slug:pk>/', views.DeleteMessageView.as_view(), name='delete message'),
]