from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    CATEGORY_CHOICES = [
        ('Gaming', 'Gaming'),
        ('Entertainment', 'Entertainment'),
        ('Sports', 'Sports'),
        ('News', 'News'),
        ('SocialMedia', 'Social Media'),
        ('Travel', 'Travel'),
    ]
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Gaming')

    class Meta:
        ordering = ('-date_created',)

    def comment_count(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
