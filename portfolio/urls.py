from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.base.urls')),
    path('contact/', include('portfolio.contact.urls')),
    path('accounts/', include('portfolio.accounts.urls')),
    path('portfolio/', include('portfolio.portfolio_projects.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
