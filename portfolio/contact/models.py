from django.db import models

import uuid
# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=30,null=True)
    subject = models.CharField(max_length=50,null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(default=uuid.uuid4, unique=True, primary_key=True, editable=False, max_length=36)

    def __str__(self):
        return self.subject