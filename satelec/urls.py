from django.contrib import admin
from django.urls import path, include
from home.views import SitemapView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('sitemap.xml', SitemapView.as_view(), name='sitemap'),
] 