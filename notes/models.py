

from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    #Vulnerable 2: content is not encrypted
    content=models.TextField()
    #Fix 2: encrypt content before storing it

    def __str__(self):
        return self.title
