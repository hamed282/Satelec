from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import SitemapView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('tinymce/', include('tinymce.urls')),
    path('sitemap.xml', SitemapView.as_view(), name='sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
