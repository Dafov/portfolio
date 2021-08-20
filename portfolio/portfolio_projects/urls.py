from django.urls import path

from portfolio.portfolio_projects import views

urlpatterns = [
    path('', views.ListProjectsView.as_view(), name='list projects'),
    path('create/', views.CreateProjectView.as_view(), name='create project'),
    path('delete/<int:pk>/', views.DeleteProjectView.as_view(), name='delete project'),
    path('edit/<int:pk>/', views.EditProjectView.as_view(), name='edit project'),
    path('details/<int:pk>', views.ProjectDetailsView.as_view(), name='details project'),

    path('comment/<int:pk>', views.CommentProjectView.as_view(), name='comment project'),
    path('comment/delete/<int:pk>', views.DeleteCommentView.as_view(), name='delete comment'),
]
