from rest_framework import serializers
from django.db import transaction
from rest_framework.validators import UniqueValidator

from .models import Record, City, Person


class PersonSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = Person
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = City
        fields = ('name', )


class AddressBookSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    person = PersonSerializer()

    class Meta:
        model = Record
        fields = ('id', 'city', 'person', 'address', 'zipcode')

    def create(self, validated_data):
        print(validated_data)


class AddressBookCompactSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city', required=True)
    person_first_name = serializers.CharField(source='person.first_name', required=True)
    person_last_name = serializers.CharField(source='person.last_name', required=True)
    person_email = serializers.CharField(source='person.email', required=True,
                                         validators=[UniqueValidator(queryset=Person.objects.all())])
    address = serializers.CharField(required=True)
    zipcode = serializers.CharField(required=True)

    class Meta:
        model = Record
        fields = ('id', 'city_name', 'person_first_name', 'person_last_name', 'address', 'person_email', 'zipcode')

    def create(self, validated_data):
        with transaction.atomic():
            city = City.objects.get_or_create(validated_data['city_name'])
            person = Person.objects.get_or_create(first_name=validated_data['person_first_name'],
                                                  last_name=validated_data['person_last_name'],
                                                  email=validated_data['email'],
                                                  fax=validated_data['fax'],
                                                  home_phone=validated_data['home_phone'],
                                                  work_phone=validated_data['work_home'])
            return Record.objects.create(city=city, person=person, address=validated_data['address'],
                                         zipcode=validated_data['zipcode'])
