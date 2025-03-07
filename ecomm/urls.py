from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('product/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path("accounts/", include("allauth.urls")),
    path('consultations/', include('consultations.urls')),
    path('diagnosis/', include('diagnosis.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
