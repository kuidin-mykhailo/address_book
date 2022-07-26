from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PersonViewSet, CityViewSet, AddressBookViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
router.register(r'city', CityViewSet, basename='city')
router.register(r'address_book', AddressBookViewSet, basename='address_book')

urlpatterns = [
    path('', include(router.urls))
]
