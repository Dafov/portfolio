from django.urls import path
from portfolio.contact import views

urlpatterns = [
    path('', views.ContactTempalteView.as_view(), name='contact'),
    # path('inbox/', views.inbox_page, name='inbox'),
    path('inbox/', views.InboxPageView.as_view(), name='inbox'),

    path('message/<str:id>/', views.MessageDetailView.as_view(), name='message'),

    # path('inbox/', views.InboxPageView.as_view(), name='inbox'),

]