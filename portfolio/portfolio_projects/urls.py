from django.urls import path

from portfolio.portfolio_projects import views

urlpatterns = [
    path('', views.ListProjectsView.as_view(), name='list projects'),
    path('create/', views.CreateProjectView.as_view(), name='create project'),
    path('delete/<int:pk>/', views.DeleteProjectView.as_view(), name='delete project'),

    path('details/<slug:title>', views.ProjectDetailsView.as_view(), name='details project'),

]