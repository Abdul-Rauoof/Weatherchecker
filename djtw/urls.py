

from django.urls import path, include

urlpatterns = [
    path('',include('appname.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
]
