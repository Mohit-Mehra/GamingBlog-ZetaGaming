from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-date_created',)

    def comment_count(self):
        return self.comments.all().count()

    def comments(self):
        return self.comments.all()

        
    def __str__(self):
        return self.title

    
    
class Commnent(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, related_name='comments',on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content







    