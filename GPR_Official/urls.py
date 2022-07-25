from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('wines/', include('wines.urls')),
    path('offers/', include('offers.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('contact/', include('contact.urls')),
    path('requirements/', include('security.urls')),
    path('profiles/', include('profiles.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
