from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Record, City, Person


class PersonSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Person.objects.all())])
    fax = serializers.CharField(required=False)

    class Meta:
        model = Person
        fields = '__all__'

    # def create(self, validated_data):
    #     return Person.objects.create(email=validated_data['email'])


class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = City
        fields = '__all__'

    def create(self, validated_data):
        if city := City.objects.filter(name=validated_data['name']).first():
            return city
        return City.objects.create(name=validated_data['name'])


class AddressBookSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    person = PersonSerializer()

    class Meta:
        model = Record
        fields = ('id', 'city', 'person', 'address', 'zipcode')

    def create(self, validated_data):
        city = City.objects.get_or_create(**validated_data['city'])[0]
        person = Person.objects.get_or_create(**validated_data['person'])[0]
        return Record.objects.create(city=city, person=person, address=validated_data['address'],
                                     zipcode=validated_data['zipcode'])
