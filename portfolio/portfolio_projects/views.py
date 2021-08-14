from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from portfolio.portfolio_projects.forms import ProjectForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from portfolio.common.superuser_mixins import SuperUserRequiredMixin
from portfolio.portfolio_projects.models import Like, Project
from django.views.generic import  ListView

# Create your views here.

class ListProjectsView(ListView):
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    model = Project
    

class CreateProjectView(SuperUserRequiredMixin, CreateView):
    form_class = ProjectForm
    success_url = reverse_lazy('list projects')
    template_name = 'portfolio/project_create.html'


    def form_valid(self, form):
        project = form.save(commit=False)
        project.user = self.request.user
        project.save()
        return super().form_valid(form)
 
    # def get_queryset(self):
    #     projects = Project.objects.all()
    #     return projects


class ProjectDetailsView(DetailView):
    model = Project
    template_name = 'portfolio/portfolio_details.html'
    context_object_name = 'project'
        
    def get_object(self):
        id_ = self.kwargs.get("id")
        project = get_object_or_404(Project, id=id_)
        return project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = context['project']

        is_owner = project.user == self.request.user
        context['is_owner'] = is_owner

        return context        

class DeleteProjectView(SuperUserRequiredMixin, DeleteView):
    template_name = 'portfolio/project_delete.html'
    model = Project
    success_url = reverse_lazy('list projects')