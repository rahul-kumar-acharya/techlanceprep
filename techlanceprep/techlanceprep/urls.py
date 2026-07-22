from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from practice.sitemaps import StaticViewSitemap, TopicSitemap, QuestionSitemap
from django.views.generic import RedirectView

sitemaps = {
    'static': StaticViewSitemap,
    'topics': TopicSitemap,
    'questions': QuestionSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tech-admin/', include('admin_panel.urls')),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('practice/', include('practice.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
