from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author: next time...

    def __str__(self):
        return f'[{self.pk}] {self.title}'  # change to admin title like this.
# Create your models here.
