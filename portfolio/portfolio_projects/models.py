from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Project(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    link = models.URLField(null=True)
    image = models.ImageField(upload_to='.', null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)

    
    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    text = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )