from django.contrib import admin
from .models import BlogModel, BlogCategoryModel


admin.site.register(BlogModel)
admin.site.register(BlogCategoryModel)
