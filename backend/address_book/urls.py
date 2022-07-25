from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AddressBookViewSet, AddressBookCompactViewSet


router = DefaultRouter()
router.register(r'address_book_compact', AddressBookCompactViewSet, basename='address_book_compact')
router.register(r'address_book', AddressBookViewSet, basename='address_book')


urlpatterns = [
    path('', include(router.urls))
]
