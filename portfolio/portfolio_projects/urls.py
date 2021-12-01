from django.urls import path

from portfolio.portfolio_projects import views

urlpatterns = [
    path('', views.ListProjectsView.as_view(), name='list projects'),
    path('create/', views.CreateProjectView.as_view(), name='create project'),
    path('delete/<slug:pk>/', views.DeleteProjectView.as_view(), name='delete project'),
    path('edit/<slug:pk>/', views.EditProjectView.as_view(), name='edit project'),
    path('details/<slug:pk>', views.ProjectDetailsView.as_view(), name='details project'),

    path('comment/<slug:pk>', views.CommentProjectView.as_view(), name='comment project'),
    path('comment/delete/<slug:pk>', views.DeleteCommentView.as_view(), name='delete comment'),
]
