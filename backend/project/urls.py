import project.settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('address_book.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

if project.settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
