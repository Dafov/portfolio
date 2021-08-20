from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from portfolio.portfolio_projects.forms import CommentForm, EditProjectForm, ProjectForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from portfolio.common.superuser_mixins import SuperUserRequiredMixin
from portfolio.portfolio_projects.models import Comment, Project
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


class ProjectDetailsView(DetailView):
    model = Project
    template_name = 'portfolio/portfolio_details.html'
    context_object_name = 'project'
        
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailsView, self).get_context_data(**kwargs)
        project = context['project']
        is_owner = project.user == self.request.user


        context['comment_form'] = CommentForm(
            initial={
                'project_pk': self.object.id,
            }
        )
        context['comments'] = project.comment_set.all()
        context['is_owner'] = is_owner
        return context


class DeleteProjectView(SuperUserRequiredMixin, DeleteView):
    template_name = 'portfolio/project_delete.html'
    model = Project
    success_url = reverse_lazy('list projects')


class EditProjectView(SuperUserRequiredMixin, UpdateView):
    model = Project
    template_name = 'portfolio/project_edit.html'
    form_class = EditProjectForm
    success_url = reverse_lazy('list projects')


class CommentProjectView(LoginRequiredMixin, View):
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, *args, **kwargs):
        project = Project.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            text=form.cleaned_data['text'],
            project=project,
            user=self.request.user,
        )
        comment.save()
        return redirect('details project', project.id)

    def form_invalid(self, form):
        pass


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    template_name = 'portfolio/comment_delete.html'
    model = Comment
    success_url = reverse_lazy('list projects')
