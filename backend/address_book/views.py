from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Record, Person, City
from .serializers import AddressBookSerializer, PersonSerializer, CitySerializer


class AddressBookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Record.objects.prefetch_related(Prefetch('city'), Prefetch('person')).all()
    serializer_class = AddressBookSerializer


class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer

