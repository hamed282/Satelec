from django.shortcuts import render
from django.views import View
from .models import BlogModel, BlogCategoryModel
from home.models import HomeModel


class BlogView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        blogs = BlogModel.objects.all()
        categories = BlogCategoryModel.objects.all()
        context = {'data': data,
                   'blogs': blogs,
                   'categories': categories}
        return render(request, 'blog/index.html', context=context)


class BlogSingleView(View):
    def get(self, request, blog_slug):
        data = HomeModel.objects.all().first()
        blogs = BlogModel.objects.all()[:3]
        blog = BlogModel.objects.get(slug=blog_slug)
        categories = BlogCategoryModel.objects.all()
        context = {'blog': blog,
                   'categories': categories,
                   'blogs': blogs,
                   'data': data}
        return render(request, 'blog/blog-single/index.html', context=context)


class BlogCategoryView(View):
    def get(self, request):
        return render(request, '')