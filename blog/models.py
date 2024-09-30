from django.contrib.auth.models import User
from django.db import models


class BlogCategoryModel(models.Model):
    category = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)


class BlogModel(models.Model):
    category = models.ForeignKey(BlogCategoryModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    cover = models.ImageField(upload_to='img/blog/cover/')
    alt_cover = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class CommentBlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercomment')
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='blogcomment')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replycomment', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=512)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'
