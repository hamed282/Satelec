from django.shortcuts import render
from django.views import View
from .models import BlogModel, BlogCategoryModel


class BlogView(View):
    def get(self, request):
        return render(request, 'blog/index.html')


class BlogSingleView(View):
    def get(self, request, blog_slug):
        blogs = BlogModel.objects.all()[:3]
        blog = BlogModel.objects.get(slug=blog_slug)
        categories = BlogCategoryModel.objects.all()
        comments = CommentBlogModel.objects.filter(blog=blog, is_reply=False, is_active=True)
        replies = CommentBlogModel.objects.filter(blog=blog, is_reply=True, is_active=True)
        return render(request, 'blog/blog-single/index.html', context={'blog': blog,
                                                                       'categories': categories,
                                                                       'blogs': blogs,
                                                                       'comments': comments, 'replies': replies})


class BlogCategoryView(View):
    def get(self, request):
        return render(request, '')