from django import forms
from portfolio.portfolio_projects.models import Comment, Project


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
        exclude = ('user', )
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
            super(CommentForm, self).__init__(*args, **kwargs)
            self.fields['text'].label = ''
            self.fields['text'].widget.attrs.update(
                {
                    'class': 'form-control',
                    'rows': '3',
                    'placeholder': 'Enter Your Comment',
                }
            )


class EditCommentForm(ProjectForm):
    class Meta:
        model = Comment
        exclude = ('user', )
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }