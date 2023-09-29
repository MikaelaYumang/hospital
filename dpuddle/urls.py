from django.contrib import admin
from django.urls import path, include
from core.views import index, contact, doctor, privacypolicy, userPage

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('doctor/', doctor, name='doctor'),
    path('admin/', admin.site.urls),
    path('about/', index, name='about'),
    path('privacypolicy/', privacypolicy, name='privacypolicy'),
    path('contact/', contact, name='contact'),
    # path('accounts/', include('allauth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
