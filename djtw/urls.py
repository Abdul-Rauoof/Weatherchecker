

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('appname.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
