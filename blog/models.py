from tinymce.models import HTMLField
from django.db import models
from home.models import TimeStampedModel


class BlogCategoryModel(models.Model):
    category = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'


class BlogModel(TimeStampedModel):
    category = models.ForeignKey(BlogCategoryModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    cover = models.ImageField(upload_to='img/blog/cover/')
    alt_cover = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
    body = HTMLField()
    slug = models.SlugField(unique=True)

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
