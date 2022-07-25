from django.db.models import Prefetch
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Record
from .serializers import AddressBookCompactSerializer, AddressBookSerializer


class AddressBookCompactViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Record.objects.prefetch_related(Prefetch('city'), Prefetch('person')).all()
    serializer_class = AddressBookCompactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city__name', 'person__first_name', 'person__last_name', 'address']


class AddressBookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Record.objects.prefetch_related(Prefetch('city'), Prefetch('person')).all()
    serializer_class = AddressBookSerializer


