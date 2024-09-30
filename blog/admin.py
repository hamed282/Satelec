from django.contrib import admin
from .models import BlogModel, BlogCategoryModel, CommentBlogModel


admin.site.register(BlogModel)
admin.site.register(BlogCategoryModel)
admin.site.register(CommentBlogModel)
