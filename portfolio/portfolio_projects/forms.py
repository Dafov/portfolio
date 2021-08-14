import os
from os.path import join

from django import forms
from django.conf import settings

from portfolio.portfolio_projects.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['title'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Enter Project Title',
            }
        )
        self.fields['description'].label = ''
        self.fields['description'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Enter Description',
            }
        )
        self.fields['image'].label = ''

        self.fields['link'].label = ''
        self.fields['link'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Enter URL Link',
            }
        )

class EditProjectForm(ProjectForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }

    def save(self, commit=True):
        db_project = Project.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_project.image))
            os.remove(image_path)
        return super().save(commit)
