from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"
    title = models.CharField(max_length=200) 
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()
    def __str__(self):
        return self.title
    