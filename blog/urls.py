from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('<str:blog_slug>/', views.BlogSingleView.as_view(), name='blog_item'),
    path('category/<str:category_slug>/', views.BlogCategoryView.as_view(), name='blog_category'),
]

