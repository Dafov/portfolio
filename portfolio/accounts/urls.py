from django.urls import path
from portfolio.accounts import views
urlpatterns = (
    path('login/', views.LoginUserView.as_view(), name='log in user'),
    path('logout/', views.logout_user, name='log out user'),
    path('register/', views.RegisterView.as_view(), name='register user'),
)