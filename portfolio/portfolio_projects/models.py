from django.contrib.auth import get_user_model

from django.db import models

# Create your models here.

UserModel = get_user_model()


class Project(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    link = models.URLField(null=True)
    image = models.ImageField(upload_to='.', blank=True, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    
    def __str__(self):
        return f'{self.title}'
    

class Like(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)